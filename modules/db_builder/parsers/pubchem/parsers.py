import json
import re
from collections import defaultdict

from core.dal import PubChemData
from modules.db_builder.parsers.lib import strip_attr, force_list, force_flatten_extra_refs, flatten_refs
from modules.db_builder.parsers.pubchem.utils import split_pubchem_ids

_mapping = {
    #'InChIKey': ('inchikey', 'sval'),
    #'InChI': ('inchi', 'sval'),

    'IUPAC Name': ('names', 'sval'),
    'Molecular Formula': ('formula', 'sval'),

    'Molecular Weight': ('mass', 'fval'),
    'Mass': ('monoisotopic_mass', 'fval'),
    'Log P': ('logp', 'fval'),
}


def metajson_transform(me):
    flatten_refs(me)

    strip_attr(me, 'chebi_id', 'CHEBI:')
    strip_attr(me, 'hmdb_id', 'HMDB')
    strip_attr(me, 'lipidmaps_id', 'LM')
    strip_attr(me, 'inchi', 'InChI=')

    force_list(me, 'names')
    force_list(me, 'smiles')

    #split_pubchem_ids(me)

    # force non-scalars into extra refs
    force_flatten_extra_refs(me, _except=('smiles',))


def parse_pubchem(db_id, c0,c1):
    """
    Parses API response for PubChem

    :param db_id:
    :param c0:
    :param c1:
    :return:
    """

    data = defaultdict(list)
    _refs = defaultdict(list)

    content = json.loads(c0)
    cont_refs = json.loads(c1)

    # parse xrefs:
    _links = cont_refs['InformationList']['Information'][0]['SBURL']

    # guess xref IDs
    for link in _links:
        link = link.lower()

        if 'ebi.ac.uk/chebi' in link:
            # http://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:18102
            db_id = link.split('chebiid=chebi:')[1].upper()
            db_tag = 'chebi_id'
        elif 'chemspider.com' in link:
            # http://www.chemspider.com/Chemical-Structure.10128115.html
            db_id = link.split('.')[-2]
            db_tag = 'chemspider_id'
        elif 'lipidmaps.org' in link:
            # http://www.lipidmaps.org/data/LMSDRecord.php?LM_ID=LMFA07070002
            db_id = link.split('LM_ID=')[1].upper()
            db_tag = 'lipidmaps_id'
        elif 'hmdb.ca' in link:
            # http://www.hmdb.ca/metabolites/HMDB0000791
            db_id = link.split('metabolites/')[1].upper()
            db_tag = 'hmdb_id'
        else:
            # unrecognized XREF
            continue

        _refs[db_tag].append(db_id)


        # "http://mona.fiehnlab.ucdavis.edu/spectra/browse?inchikey=CXTATJFJDMJMIY-CYBMUJFWSA-N",
        # "http://www.chemscene.com/25243-95-2.html",
        # "http://www.genome.jp/dbget-bin/www_bget?cpd:C02838",
        # "http://www.metabolomicsworkbench.org/data/StructureData.php?RegNo=4482",
        # "http://www.nextbio.com/b/search/ov/Octanoylcarnitine?id=5454504&type=compound&synonym=Octanoylcarnitine",
        # "https://app.collaborativedrug.com/public/structures/1016697",
        # "https://biocyc.org/compound?orgid=META&id=L-OCTANOYLCARNITINE",
        # "https://chem-space.com/CSSB00161152344",
        # "https://chem.nlm.nih.gov/chemidplus/id/0025243952",
        # "https://massbank.eu/MassBank/Result.jsp?inchikey=CXTATJFJDMJMIY-CYBMUJFWSA-N",
        # "https://patents.google.com/?q=CXTATJFJDMJMIY-CYBMUJFWSA-N",
        # "https://patentscope.wipo.int/search/en/result.jsf?inchikey=CXTATJFJDMJMIY-CYBMUJFWSA-N",
        # "https://tools.wmflabs.org/scholia/Q27102821",
        # "https://www.discoverygate.com/interlink/search?KeyName=EXTREG&KeyValue=11953814&Database=INDEX&Source=PUBCHEM",
        # "https://www.enovationchem.com/ProductDetails.asp?ProductID=D771037",
        # "https://www.fda.gov/ForIndustry/DataStandards/SubstanceRegistrationSystem-UniqueIngredientIdentifierUNII/",
        # "https://www.keyorganics.net/bionet/catalog/product/view/id/1428262",
        # "https://www.medchemexpress.com/L-Octanoylcarnitine.html",
        # "https://www.molport.com/shop/molecule-link/MolPort-046-683-346",
        # "https://www.sigmaaldrich.com/catalog/product/sigma/50892?utm_source=pubchem&utm_campaign=pubchem_2017&utm_medium=referral",
        # "https://www.smolecule.com/products/s640464",
        # "https://www.surechembl.org/chemical/SCHEMBL2915508",
        # "https://www.thebiotek.com/product/others/bt-448172"

    data.update(content['PC_Compounds'][0])
    props = data.pop('props')
    pubchem_id = data['id']['id']['cid']

    hat_geci = []

    for prop in props:
        label = prop['urn']['label']

        attr, valt = _mapping.get(label, (label, None))
        attr = attr.lower()

        if isinstance(prop['value'], dict):
            if valt is None:
                if 'sval' in prop['value']:
                    valt = 'sval'
                else:
                    # skip attr as it's not mapped
                    hat_geci.append((attr, valt, prop['value']))
                    continue
            data[attr] = prop['value'][valt]
        else:
            data[attr] = prop['value']

    # merge and transform to standard json
    data.update(_refs)
    metajson_transform(data)

    return PubChemData(pubchem_id=pubchem_id, **data)
