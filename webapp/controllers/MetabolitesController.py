from flask import render_template

from core.dal.views.metabolites import MetaboliteView
from core.metabolite import get_metabolite


class MetabolitesController:
    def __init__(self, server):
        pass

    def get(self, meta_id):
        metabolite: MetaboliteView = get_metabolite(meta_id)

        return render_template('/metabolite/view.html', meta_id=meta_id, metabolite=metabolite)

    def get_upload(self):
        return render_template('/metabolite/upload.html')

    def get_edit(self):
        return render_template('/metabolite/edit.html')

    def get_curate(self):
        return render_template('/metabolite/curate.html')
