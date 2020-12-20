export const template = `<div v-if="show">
    <h1 class="title text-success font-light">{{ meta.primary_name }}</h1>


    <div class="row">
        <div class="col-6">
            <a class="btn btn-link text-info pointer" v-b-toggle.collapseSynonyms role="button"><b>Synonyms</b></a>

            <div class="card">
                <div class="card-heading">
                </div>
                <div class="card-body">
                    <b-collapse visible class="collapse" id="collapseSynonyms">
                        <div class="rounded p-2 scroll meta-synonyms" style="background-color: #e9ecef;">
                            <div v-for="name in meta.names">
                                {{ name }}
                            </div>
                        </div>
                    </b-collapse>
                </div>
            </div>

            <a class="btn btn-link text-info pointer" v-b-toggle.collapseStructure role="button"><b>Structure</b></a>
            <div class="card">
                <div class="card-heading">
                </div>
                <div class="card-body">
                    <b-collapse visible class="collapse" id="collapseStructure">
                        
                        <b-tabs content-class="mt-3">
                            <b-tab title="ASCII" active>
                                <table class="table table-sm table-borderless table-hover">
                                    <tr>
                                        <th class="text-success">Formula</th>
                                        <td>{{ meta.formula }}</td>
                                    </tr>
                                    <tr>
                                        <th class="text-success">InChI</th>
                                        <td>{{ meta.inchi }}
                                            <br/>
                                            <span class="small">{{ meta.inchikey }}</span>
                                        </td>
                                    </tr>
                                    
                                    <tr>
                                        <th class="text-success">SMILES</th>
                                        <td>{{ meta.smiles }}</td>
                                    </tr>
                                    <tr>
                                        <th class="text-success">Mass<sup class="text-info sup-smol">average</sup></th>
                                        <td>{{ meta.mass }}</td>
                                    </tr>
                                    <tr>
                                        <th class="text-success">Mass<sup class="text-info sup-smol">monoisotopic</sup></th>
                                        <td>{{ meta.monoisotopic_mass }}</td>
                                    </tr>
                                </table>

                            </b-tab>
                            <b-tab title="2D" disabled>
                            </b-tab>
                            <b-tab title="3D" disabled>
                            </b-tab>
                        </b-tabs>

                    </b-collapse>
                </div>
            </div>

        </div>
        <div class="col-6">

            <a class="btn btn-link text-info pointer" v-b-toggle.collapseReferences role="button"><b>References</b></a>
            <div class="card">
                <div class="card-heading">
                </div>
                <div class="card-body">
                    <b-collapse visible class="collapse" id="collapseReferences">
                        <table class="table table-sm table-borderless table-hover">
                            <tr v-for="db in databases_filled">
                                <th class="text-success"><img class="meta-db-icon" :src="'/img/dbicons/'+db+'.png'"> {{ db }}</th>
                                <td>{{ meta[db.lower()+"_id"] }}</td>
                            </tr> 
                        </table>
                    </b-collapse>
                </div>
            </div>

            <a class="btn btn-link text-info pointer" v-b-toggle.collapseDescription role="button"><b>Description</b></a>
            <div class="card">
                <div class="card-heading">
                </div>
                <div class="card-body">
                    <b-collapse visible class="collapse" id="collapseDescription">
                        {{ meta.description }}
                    </b-collapse>
                </div>
            </div>

        </div>
    </div>

</div>`;