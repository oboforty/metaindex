from eme.data_access import JSON_GEN
from sqlalchemy import Column, String, Float, TEXT, ARRAY, Integer, ForeignKey

from core.dal.base.sqlite import EntityBase


class LipidMapsData(EntityBase):
    __tablename__ = 'lipidmaps_data'

    # Primary Ids
    lipidmaps_id = Column(String(20), primary_key=True)

    # Reference Ids
    kegg_id = Column(String(20), ForeignKey('kegg_data.kegg_id'))
    hmdb_id = Column(String(20), ForeignKey('hmdb_data.hmdb_id'))
    chebi_id = Column(String(20), ForeignKey('chebi_data.chebi_id'))
    pubchem_id = Column(String(20), ForeignKey('pubchem_data.pubchem_id'))
    lipidbank_id = Column(String(20))
    cas_id = Column(String(20))
    ref_etc = Column(JSON_GEN())     # Extra ref Refs

    # Shared metadata
    names = Column(ARRAY(TEXT))
    mass = Column(Float)

    # Structure
    smiles = Column(TEXT)
    inchi = Column(TEXT)
    inchikey = Column(String(TEXT))
    formula = Column(String(TEXT))

    # Other Fun Facts
    category = Column(String(32))
    main_class = Column(String(64))
    sub_class = Column(String(128))
    lvl4_class = Column(String(128))


    def __init__(self, **kwargs):
        self.lipidmaps_id = kwargs.get('lipidmaps_id')
        self.names = kwargs.get('names')
        self.category = kwargs.get('category')
        self.main_class = kwargs.get('main_class')
        self.sub_class = kwargs.get('sub_class')
        self.lvl4_class = kwargs.get('lvl4_class')
        self.mass = kwargs.get('mass')
        self.smiles = kwargs.get('smiles')
        self.inchi = kwargs.get('inchi')
        self.inchikey = kwargs.get('inchikey')
        self.formula = kwargs.get('formula')
        self.kegg_id = kwargs.get('kegg_id')
        self.hmdb_id = kwargs.get('hmdb_id')
        self.chebi_id = kwargs.get('chebi_id')
        self.pubchem_id = kwargs.get('pubchem_id')
        self.lipidbank_id = kwargs.get('lipidbank_id')

        if isinstance(self.mass, str):
            if not self.mass:
                self.mass = None
            else:
                self.mass = float(self.mass)
