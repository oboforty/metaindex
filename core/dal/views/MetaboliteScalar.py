from dataclasses import dataclass


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
