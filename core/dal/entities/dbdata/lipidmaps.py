from eme.data_access import JSON_GEN
from sqlalchemy import Column, String, Float, Text, ARRAY, Integer, ForeignKey

from core.dal.base.sqlite import EntityBase


class LipidMapsData(EntityBase):
    __tablename__ = 'lipidmaps_data'

    # Primary Ids
    lipidmaps_id = Column(String(20), primary_key=True)

    # Reference Ids
    kegg_id = Column(String(20)) # ForeignKey('kegg_data.kegg_id', ondelete='SET NULL'))
    hmdb_id = Column(String(20)) # ForeignKey('hmdb_data.hmdb_id', ondelete='SET NULL'))
    chebi_id = Column(String(20)) # ForeignKey('chebi_data.chebi_id', ondelete='SET NULL'))
    pubchem_id = Column(String(20)) # ForeignKey('pubchem_data.pubchem_id', ondelete='SET NULL'))
    lipidbank_id = Column(String(20))
    cas_id = Column(String(20))

    ref_etc = Column(JSON_GEN())     # Extra ref Refs
    chemspider_id = Column(String(24))
    metlin_id = Column(String(24))
    pubchem_sub_id = Column(String(24))
    wiki_id = Column(String(256))
    drugbank_id = Column(String(24))
    pdb_id = Column(String(24))
    pubmed_id = Column(String(24))

    # Shared metadata
    names = Column(ARRAY(Text))
    mass = Column(Float)

    # Structure
    smiles = Column(Text)
    inchi = Column(Text)
    inchikey = Column(Text)
    formula = Column(Text)

    # Other Fun Facts
    category = Column(String(32))
    main_class = Column(String(64))
    sub_class = Column(String(128))
    lvl4_class = Column(String(128))


    def __init__(self, **kwargs):
        self.lipidmaps_id = kwargs.get('lipidmaps_id')
        self.kegg_id = kwargs.get('kegg_id')
        self.hmdb_id = kwargs.get('hmdb_id')
        self.chebi_id = kwargs.get('chebi_id')
        self.pubchem_id = kwargs.get('pubchem_id')
        self.lipidbank_id = kwargs.get('lipidbank_id')
        self.cas_id = kwargs.get('cas_id')
        self.ref_etc = kwargs.get('ref_etc')
        self.chemspider_id = kwargs.get('chemspider_id')
        self.metlin_id = kwargs.get('metlin_id')
        self.pubchem_sub_id = kwargs.get('pubchem_sub_id')
        self.wiki_id = kwargs.get('wiki_id')
        self.drugbank_id = kwargs.get('drugbank_id')
        self.pdb_id = kwargs.get('pdb_id')
        self.pubmed_id = kwargs.get('pubmed_id')
        self.names = kwargs.get('names')
        self.mass = kwargs.get('mass')
        self.smiles = kwargs.get('smiles')
        self.inchi = kwargs.get('inchi')
        self.inchikey = kwargs.get('inchikey')
        self.formula = kwargs.get('formula')
        self.category = kwargs.get('category')
        self.main_class = kwargs.get('main_class')
        self.sub_class = kwargs.get('sub_class')
        self.lvl4_class = kwargs.get('lvl4_class')

        if isinstance(self.mass, str):
            if not self.mass:
                self.mass = None
            else:
                self.mass = float(self.mass)
