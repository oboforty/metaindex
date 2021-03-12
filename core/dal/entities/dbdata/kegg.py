from core.dal.base.sqlite import EntityBase

from sqlalchemy import Column, String, Float, Text, ARRAY, Integer, ForeignKey
from eme.data_access import JSON_GEN


class KeggData(EntityBase):
    __tablename__ = 'kegg_data'

    # Primary Ids
    kegg_id = Column(String(20), primary_key=True)

    # Reference Ids
    chebi_id = Column(String(20)) #ForeignKey('chebi_data.chebi_id', ondelete='SET NULL'))
    lipidmaps_id = Column(String(20)) #ForeignKey('lipidmaps_data.lipidmaps_id', ondelete='SET NULL'))
    pubchem_id = Column(String(20)) #ForeignKey('pubchem_data.pubchem_id', ondelete='SET NULL'))
    cas_id = Column(String(20))

    ref_etc = Column(JSON_GEN())     # Extra ref Refs
    pdb_id = Column(String(24))

    # Shared metadata
    names = Column(ARRAY(Text))
    monoisotopic_mass = Column(Float)
    mass = Column(Float)

    # Structure
    formula = Column(String(256))

    # Other Fun Facts
    comments = Column(Text)

    def __init__(self, **kwargs):
        self.kegg_id = kwargs.get('kegg_id')
        self.names = kwargs.get('names')
        self.monoisotopic_mass = kwargs.get('monoisotopic_mass')
        self.mass = kwargs.get('mass')
        self.comments = kwargs.get('comments')
        self.formula = kwargs.get('formula')
        self.cas_id = kwargs.get('cas_id')
        self.kegg_id = kwargs.get('kegg_id')
        self.chebi_id = kwargs.get('chebi_id')
        self.lipidmaps_id = kwargs.get('lipidmaps_id')
        self.pubchem_id = kwargs.get('pubchem_id')
        self.ref_etc = kwargs.get('ref_etc')

        if isinstance(self.monoisotopic_mass, str):
            if not self.monoisotopic_mass:
                self.monoisotopic_mass = None
            else:
                self.monoisotopic_mass = float(self.monoisotopic_mass)

        if isinstance(self.mass, str):
            if not self.mass:
                self.mass = None
            else:
                self.mass = float(self.mass)

