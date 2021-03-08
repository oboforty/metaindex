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

    @property
    def view(self):
        return self.__dict__.copy()

    @property
    def primary_name(self):
        return "ehh"

    def update(self, df):
        if df.chebi_id is not None:
            self.chebi_id.update(df.chebi_id)
        if df.kegg_id is not None:
            self.kegg_id.update(df.kegg_id)
        if df.hmdb_id is not None:
            self.hmdb_id.update(df.hmdb_id)
        if df.lipidmaps_id is not None:
            self.lipidmaps_id.update(df.lipidmaps_id)
        if df.pubchem_id is not None:
            self.pubchem_id.update(df.pubchem_id)
        if df.cas_id is not None:
            self.cas_id.update(df.cas_id)
        if df.ref_etc is not None:
            self.ref_etc.update(df.ref_etc)
        if df.names is not None:
            self.names.extend(df.names)
        if df.description is not None:
            self.description.update(df.description)
        if df.charge is not None:
            self.charge.update(df.charge)
        if df.mass is not None:
            self.mass.update(df.mass)
        if df.monoisotopic_mass is not None:
            self.monoisotopic_mass.update(df.monoisotopic_mass)
        if df.smiles is not None:
            self.smiles.update(df.smiles)
        if df.inchi is not None:
            self.inchi.update(df.inchi)
        if df.inchikey is not None:
            self.inchikey.update(df.inchikey)
        if df.formula is not None:
            self.formula.update(df.formula)

    def __repr__(self):
        return self.names[0]