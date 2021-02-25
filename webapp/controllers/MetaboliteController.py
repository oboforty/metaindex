from flask import render_template

from core.dal import MetaboliteScalar


class MetaboliteController:
    def __init__(self, server):
        pass

    def get(self, meta_id='ABDE'):
        # fixme: temporal: test entity
        metabolite = MetaboliteScalar(
            meta_id = meta_id,

            chebi_id = '73244',
            kegg_id = None,
            hmdb_id = 'HMDB0029703',
            lipidmaps_id = None,
            pubchem_id = '8635',
            cas_id = '134-20-3',
            ref_etc = {},

            primary_name = 'methyl anthranilate',
            names = [
                'methyl anthranilate',
                '2-(Methoxycarbonyl)aniline',
                '2-Aminobenzoic acid methyl ester',
                '2-Carbomethoxyaniline',
                'Anthranilic acid methyl ester',
                'Methyl o-aminobenzoate',
                'o-Aminobenzoic acid methyl ester',
                'o-Carbomethoxyaniline',
                'O-methyl anthranilate'
            ],
            description = 'Methyl 2-aminobenzoate is found in alcoholic beverages. Methyl 2-aminobenzoate is found in essential oils, including bergamot, orange peel, lemon peel, jasmine, ylang-ylang and neroli. Also present in concord grape, strawberry, star fruit, wines, cocoa, black tea and rice bran. Methyl 2-aminobenzoate is a flavouring agent',
            charge = 0,
            mass = 151.16260,
            monoisotopic_mass = 151.063328537,

            smiles = 'COC(=O)c1ccccc1N',
            inchi = '1S/C8H9NO2/c1-11-8(10)6-4-2-3-5-7(6)9/h2-5H,9H2,1H3',
            inchikey = 'VAMXMNNIEUEQDV-UHFFFAOYSA-N',
            formula = 'C8H9NO2',
        )

        return render_template('/metabolite/view.html', meta_id=meta_id, metabolite=metabolite)

    def get_upload(self):
        return render_template('/metabolite/upload.html')

    def get_edit(self):
        return render_template('/metabolite/edit.html')

    def get_curate(self):
        return render_template('/metabolite/curate.html')
