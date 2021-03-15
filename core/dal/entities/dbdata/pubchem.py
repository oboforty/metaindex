from core.dal.base.sqlite import EntityBase

from sqlalchemy import Column, String, Float, Text, ARRAY, Integer, ForeignKey
from eme.data_access import JSON_GEN


class PubChemData(EntityBase):
    __tablename__ = 'pubchem_data'

    # Primary Ids
    pubchem_id = Column(String(20), primary_key=True)
    #pubchem_sub_id = Column(String(24)) #ForeignKey('pubchem_substrate_data.pubchem_id', ondelete='SET NULL'))

    # Reference Ids
    chebi_id = Column(String(24)) #ForeignKey('chebi_data.chebi_id', ondelete='SET NULL'))
    kegg_id = Column(String(24)) #ForeignKey('kegg_data.kegg_id', ondelete='SET NULL'))
    hmdb_id = Column(String(24)) #ForeignKey('hmdb_data.hmdb_id', ondelete='SET NULL'))
    cas_id = Column(String(24))

    ref_etc = Column(JSON_GEN())     # Extra ref Refs
    chemspider_id = Column(String(24))
    #metlin_id = Column(String(24))
    #wiki_id = Column(String(24))
    #drugbank_id = Column(String(24))
    #pdb_id = Column(String(24))
    #pubmed_id = Column(String(24))

    # Shared metadata
    names = Column(ARRAY(Text))
    mass = Column(Float)
    monoisotopic_mass = Column(Float)

    # Structure
    smiles = Column(ARRAY(Text))
    inchi = Column(Text)
    inchikey = Column(String(27))
    formula = Column(String(256))

    # Other Fun Facts
    logp = Column(Float)

    def __init__(self, **kwargs):
        self.pubchem_id = kwargs.get('pubchem_id')
        self.pubchem_sub_id = kwargs.get('pubchem_sub_id')
        self.chebi_id = kwargs.get('chebi_id')
        self.kegg_id = kwargs.get('kegg_id')
        self.hmdb_id = kwargs.get('hmdb_id')
        self.cas_id = kwargs.get('cas_id')
        self.ref_etc = kwargs.get('ref_etc')
        self.chemspider_id = kwargs.get('chemspider_id')
        self.metlin_id = kwargs.get('metlin_id')
        self.wiki_id = kwargs.get('wiki_id')
        self.drugbank_id = kwargs.get('drugbank_id')
        self.pdb_id = kwargs.get('pdb_id')
        self.pubmed_id = kwargs.get('pubmed_id')
        self.names = kwargs.get('names')
        self.mass = kwargs.get('mass')
        self.weight = kwargs.get('weight')
        self.monoisotopic_mass = kwargs.get('monoisotopic_mass')
        self.smiles = kwargs.get('smiles')
        self.inchi = kwargs.get('inchi')
        self.inchikey = kwargs.get('inchikey')
        self.formula = kwargs.get('formula')
        self.logp = kwargs.get('logp')


        print("TODO: pubchem handle synonyms and description")