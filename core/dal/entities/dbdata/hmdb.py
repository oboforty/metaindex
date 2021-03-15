from eme.data_access import JSON_GEN

from core.dal.base.sqlite import EntityBase

from sqlalchemy import Column, String, Float, Text, ARRAY, ForeignKey

# Dizzy: Prince of the Yolkfolk
class HMDBData(EntityBase):
    __tablename__ = 'hmdb_data'

    # Primary Ids
    hmdb_id = Column(String(20), primary_key=True)

    # Reference Ids
    kegg_id = Column(String(24)) #ForeignKey('kegg_data.kegg_id', ondelete='SET NULL'))
    pubchem_id = Column(String(24)) #ForeignKey('pubchem_data.pubchem_id'), ondelete='SET NULL')
    chebi_id = Column(String(24)) #ForeignKey('chebi_data.chebi_id'), ondelete='SET NULL')
    cas_id = Column(String(24))

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
    description = Column(Text)
    avg_mol_weight = Column(Float)
    monoisotopic_mol_weight = Column(Float)

    # Structure
    formula = Column(Text)
    smiles = Column(Text)
    inchi = Column(Text)
    inchikey = Column(Text)

    # Other Fun Facts
    state = Column(String(32))

    # biofluid_locations = Column(ARRAY(String(64)))
    # tissue_locations = Column(ARRAY(String(64)))
    #
    # # Complex data
    # taxonomy = Column(JSON_GEN)
    # ontology = Column(JSON_GEN)
    # proteins = Column(JSON_GEN)
    # diseases = Column(JSON_GEN)

    # synthesis_reference = Column(TEXT)

    def __init__(self, **kwargs):
        self.hmdb_id = kwargs.get('hmdb_id')
        self.hmdb_id_alt = kwargs.get('hmdb_id_alt')
        self.kegg_id = kwargs.get('kegg_id')
        self.pubchem_id = kwargs.get('pubchem_id')
        self.chebi_id = kwargs.get('chebi_id')
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
        self.description = kwargs.get('description')
        self.avg_mol_weight = kwargs.get('avg_mol_weight')
        self.monoisotopic_mol_weight = kwargs.get('monoisotopic_mol_weight')
        self.formula = kwargs.get('formula')
        self.smiles = kwargs.get('smiles')
        self.inchi = kwargs.get('inchi')
        self.inchikey = kwargs.get('inchikey')
        self.state = kwargs.get('state')

        if isinstance(self.avg_mol_weight, str):
            if not self.avg_mol_weight:
                self.avg_mol_weight = None
            else:
                self.avg_mol_weight = str(self.avg_mol_weight)

        if isinstance(self.monoisotopic_mol_weight, str):
            if not self.monoisotopic_mol_weight:
                self.monoisotopic_mol_weight = None
            else:
                self.monoisotopic_mol_weight = str(self.monoisotopic_mol_weight)
