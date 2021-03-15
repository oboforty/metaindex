from sqlalchemy import Column, String, Float, Text, ARRAY, Integer, ForeignKey
from eme.data_access import JSON_GEN

from core.dal.base.sqlite import EntityBase


class ChEBIData(EntityBase):
    __tablename__ = 'chebi_data'

    # Primary Ids
    chebi_id = Column(String(20), primary_key=True)

    # Reference Ids
    # from database_accession.tsv  # todo: add Foreign Keys!
    kegg_id = Column(String(24)) #ForeignKey('kegg_data.kegg_id', ondelete='SET NULL'))
    hmdb_id = Column(String(24)) #ForeignKey('hmdb_data.hmdb_id', ondelete='SET NULL'))
    lipidmaps_id = Column(String(32)) #ForeignKey('lipidmaps_data.lipidmaps_id', ondelete='SET NULL'))
    pubchem_id = Column(String(24)) #ForeignKey('pubchem_data.pubchem_id', ondelete='SET NULL'))
    cas_id = Column(String(24))

    ref_etc = Column(JSON_GEN())     # Extra ref Refs
    chemspider_id = Column(String(24))
    metlin_id = Column(String(24))
    pubchem_sub_id = Column(String(24))
    wiki_id = Column(String(256))
    drugbank_id = Column(String(24))
    pdb_id = Column(String(24))
    #pubmed_id = Column(String(24))
    uniprot_id = Column(String(24))

    # Shared metadata
    names = Column(ARRAY(Text))
    description = Column(Text)
    charge = Column(Float) # from chemical_data.tsv
    mass = Column(Float)
    monoisotopic_mass = Column(Float)

    # Structure
    smiles = Column(Text)
    inchi = Column(Text)
    inchikey = Column(Text)
    formula = Column(Text)

    # Other Fun Facts
    quality = Column(Integer) # from compounds.tsv
    comments = Column(Text) # from comments.tsv

    def __init__(self, **kwargs):
        self.chebi_id = kwargs.get('chebi_id')
        self.kegg_id = kwargs.get('kegg_id')
        self.hmdb_id = kwargs.get('hmdb_id')
        self.lipidmaps_id = kwargs.get('lipidmaps_id')
        self.pubchem_id = kwargs.get('pubchem_id')
        self.cas_id = kwargs.get('cas_id')
        self.ref_etc = kwargs.get('ref_etc')
        self.chemspider_id = kwargs.get('chemspider_id')
        self.metlin_id = kwargs.get('metlin_id')
        self.pubchem_sub_id = kwargs.get('pubchem_sub_id')
        self.wiki_id = kwargs.get('wiki_id')
        self.drugbank_id = kwargs.get('drugbank_id')
        self.pdb_id = kwargs.get('pdb_id')
        #self.pubmed_id = kwargs.get('pubmed_id')
        self.uniprot_id = kwargs.get('uniprot_id')
        self.names = kwargs.get('names')
        self.description = kwargs.get('description')
        self.charge = kwargs.get('charge')
        self.mass = kwargs.get('mass')
        self.monoisotopic_mass = kwargs.get('monoisotopic_mass')
        self.smiles = kwargs.get('smiles')
        self.inchi = kwargs.get('inchi')
        self.inchikey = kwargs.get('inchikey')
        self.formula = kwargs.get('formula')
        self.quality = kwargs.get('quality')
        self.comments = kwargs.get('comments')

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

        if isinstance(self.charge, str):
            if not self.charge:
                self.charge = None
            else:
                self.charge = float(self.charge)

        if isinstance(self.quality, str):
            if not self.quality:
                self.quality = None
            else:
                self.quality = int(self.quality)
