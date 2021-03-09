from dataclasses import dataclass, field


@dataclass
class MetaboliteScalar:
    meta_id: str

    # Reference Ids
    chebi_id: str = None
    kegg_id: str = None
    hmdb_id: str = None
    lipidmaps_id: str = None
    pubchem_id: str = None
    cas_id: str = None

    ref_etc: dict = None

    # Metadata
    primary_name: str = None
    names: list = None
    description: str = None
    charge: float = None
    mass: float = None
    monoisotopic_mass: float = None

    # Structure
    smiles: str = None
    inchi: str = None
    inchikey: str = None
    formula: str = None

    @property
    def view(self):
        return self.__dict__.copy()


@dataclass
class MetaboliteView:
    meta_id: str = None

    # Reference Ids
    chebi_id: set = field(default_factory=set)
    kegg_id: set = field(default_factory=set)
    hmdb_id: set = field(default_factory=set)
    lipidmaps_id: set = field(default_factory=set)
    pubchem_id: set = field(default_factory=set)
    cas_id: set = field(default_factory=set)
    metlin_id: set = field(default_factory=set)

    ref_etc: dict = field(default_factory=dict)

    # Metadata
    names: list = field(default_factory=list)
    description: set = field(default_factory=set)
    charge: set = field(default_factory=set)
    mass: set = field(default_factory=set)
    monoisotopic_mass: set = field(default_factory=set)

    # Structure
    smiles: set = field(default_factory=set)
    inchi: set = field(default_factory=set)
    inchikey: set = field(default_factory=set)
    formula: set = field(default_factory=set)

    def update(self, df):
        for ref_tag, _ref_ids in self.refs:
            _ref_ids.update(getattr(df, ref_tag))

        for attr, val in self.attributes:
            if attr == 'names': continue

            val.update(getattr(df, attr))

        if df.names is not None:
            self.names.extend(df.names)

    @property
    def view(self):
        return self.__dict__.copy()

    @property
    def primary_name(self):
        return "ehh"

    @property
    def refs(self):
        yield 'chebi_id', self.chebi_id
        yield 'hmdb_id', self.hmdb_id
        yield 'lipidmaps_id', self.lipidmaps_id
        yield 'pubchem_id', self.pubchem_id
        yield 'cas_id', self.cas_id
        yield 'kegg_id', self.kegg_id
        yield 'metlin_id', self.metlin_id

        # todo: should we care about refs? the relevant IDs should already been merged to the ids above!
        # for _ref_tag, _xtra_refs in self.ref_etc.items():
        #     for _ref_id in _xtra_refs:
        #         yield _ref_tag, _ref_id

    @property
    def refs_flat(self):
        # yield only the references that are present as flat (tag, id) enumerable
        for _tag, _ids in self.refs:
            if _ids:
                for _id in _ids:
                    if _id: # this should be checked because {None} sets are possible... boo
                        yield _tag, _id

    @property
    def attributes(self):
        yield 'names', self.names
        yield 'description', self.description
        yield 'charge', self.charge
        yield 'mass', self.mass
        yield 'monoisotopic_mass', self.monoisotopic_mass
        yield 'smiles', self.smiles
        yield 'inchi', self.inchi
        yield 'inchikey', self.inchikey
        yield 'formula', self.formula

    def __repr__(self):
        return self.names[0]
