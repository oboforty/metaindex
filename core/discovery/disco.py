from queue import Queue
from typing import Tuple

from core.dal import MetaboliteView
from .db_handler import get_db_ids, getdb
from .utils import depad_id, pad_id
from .managers.ManagerBase import ManagerBase


attr_refs = set(get_db_ids())
attr_meta = attr_refs | {
  "inchi", "inchikey", "smiles",
  "names", "formula",
  "charge", "mass", "monoisotopic_mass"
}


def resolve_metabolites(df: MetaboliteView, verbose: bool = False, cache: bool = True) -> Tuple[MetaboliteView, dict]:
    # data used in the algorithm:
    #df_disc = transform_df(df)     # discovered Metabolite views
    # todo: @temporal
    df_disc = df
    undiscovered = set()
    secondary_ids = set()
    ambigous = []
    Q = Queue()
    discovered = set()

    #L = nrow(df_disc)

    # todo: @later: how to filter which attributes to use
    # todo: @temporal: for now, all is requested
    #attr_df = filter_requested_attr(names(df_disc), attr_meta)
    #attr_df = attr_meta
    #refids_req = intersect(attr_df, attr_refs)
    refids_req = attr_refs

    # queue initial items for the discover algorithm
    for db_tag, db_id in df_disc.refs_flat:
        # insert all reference IDs to the queue
        Q.put((db_tag, depad_id(db_id, db_tag), "root", "-"))

    while Q.qsize() > 0:
        # Keep getting IDs out of the queue while it's not empty
        db_tag, db_id, db_ref, db_ref_id = Q.get()
        hand: ManagerBase = getdb(db_tag)

        if not hand:
            # unknown database type
            undiscovered.add((db_tag, db_id, db_ref, db_ref_id))
            continue

        # Query metabolite record from local database or web api
        if verbose:
            print(f"{db_ref}[{db_ref_id}] -> {db_tag}[{db_id}]")

        df_result: MetaboliteView = hand.get_metabolite(db_id, cache=cache)

        if not df_result:
            # check if we get a hit treating 'db_id' as a secondary id
            db_id_primary = hand.resolve_secondary_id(db_id)

            if db_id_primary:
                # put the primary ID in the queue again to be resolved
                Q.put((db_tag, db_id_primary, "2nd_"+db_tag, db_id))

                # exclude secondary ids from output dataframe
                ids = getattr(df_disc, db_tag)
                setattr(df_disc, db_tag, ids - {db_id})

                # and add it to a special list
                secondary_ids.add((db_tag, db_id))
            else:
                # none of the fallback strategies have worked, mark as 'undiscovered'
                undiscovered.add((db_tag,db_id,db_ref,db_ref_id))

            continue

        # df_result != null => mark discovered
        # todo: this is not needed (see 100th line)
        discovered.add((db_tag, db_id))

        # @temp: debug {None} cases
        # if None in df_result.chebi_id:
        #     grr = None in df_disc.chebi_id
        #     print(db_id, db_tag, grr)

        # merge result with previously discovered data
        df_disc.update(df_result)

        # parse novel reference IDs found in the API result and add them to queue
        for new_db_tag, new_db_id in df_result.refs_flat:
            # check if such dbid is present in the record
            if (new_db_tag, new_db_id) not in discovered:
                if new_db_id != db_id or new_db_tag != db_tag:
                    # enqueue for exploration, but only if it hasn't occured before
                    # Format: (db_tag, db_id, db_tag that referenced this id)
                    Q.put((new_db_tag, new_db_id, db_tag, db_id))
                    discovered.add((new_db_tag, new_db_id))

        if not Q:
            # once we ran out of ids to explore, try reverse queries
            for db_tag_missing in refids_req:
                if not getattr(df_disc, db_tag_missing):

                    if verbose:
                        print(f'Reverse-querying: {db_tag_missing}')

                    # this db reference is still missing, try querying in reverse
                    hand = getdb(db_tag_missing)
                    db_ids = hand.query_reverse(df_disc)

                    for db_id_missing in db_ids:
                        # put these newly discovered ids to the queue
                        if (db_tag_missing, db_id_missing) not in discovered:
                            Q.put((db_tag_missing, db_id_missing, "reversed", "-"))

    # post parse data
    # todo: find ambigous data

    # TODO: ITT: trim data n shit

    # TODO: smart_trim ? return scalars as scalars instead of sets with len 1

    # Return complex output of everything
    resp = dict(
        # discovered = lapply(discovered, as_vector),
        undiscovered=undiscovered,
        secondary=secondary_ids,
        ambigous=ambigous
    )

    # if (verbose & & length(resp$undiscovered) > 0):
    #     warning("You have undiscovered metabolite IDs! Check return$undiscovered for details_")

    return df_disc, resp


def resolve_single_id(start_db_tag, start_db_id, verbose=False, cache=True):
    if isinstance(start_db_id, (list, tuple, set)):
        if len(start_db_id) != 1:
            raise Exception("can't resolve list of db_ids")
        start_db_id = list(start_db_id)[0]

    # Create initial dataframe from user input:
    df_res = MetaboliteView()
    setattr(df_res, start_db_tag, {start_db_id})

    # call the resolve algorithm
    return resolve_metabolites(df_res, verbose=verbose, cache=cache)
