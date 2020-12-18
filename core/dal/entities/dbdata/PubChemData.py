from core.dal.base.sqlite import EntityBase

from sqlalchemy import Column, String, Float, TEXT, ARRAY, Integer, ForeignKey
from eme.data_access import JSON_GEN


class PubChemData(EntityBase):
    __tablename__ = 'pubchem_data'

    # Primary Ids
    pubchem_id = Column(String(20), primary_key=True)

    # Reference Ids
    chebi_id = Column(String(20), ForeignKey('chebi_data.chebi_id'))
    kegg_id = Column(String(20), ForeignKey('kegg_data.kegg_id'))
    hmdb_id = Column(String(20), ForeignKey('hmdb_data.hmdb_id'))
    chemspider_id = Column(String(20))
    cas_id = Column(String(20))
    ref_etc = Column(JSON_GEN())     # Extra ref Refs

    # Shared metadata
    names = Column(ARRAY(TEXT))
    mass = Column(Float)
    #weight = Column(Float)
    monoisotopic_mass = Column(Float)

    # Structure
    smiles = Column(ARRAY(TEXT))
    inchi = Column(TEXT)
    inchikey = Column(String(27))
    formula = Column(String(256))

    # Other Fun Facts
    logp = Column(Float)


    def __init__(self, **kwargs):
        pass