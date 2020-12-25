export const template = `<div v-if="show" class="container-xl p-4">
    <h1 class="title text-success font-light">{{ meta.primary_name }}</h1>


    <div class="row">
        <div class="col-sm-12 col-md-6 col-lg-4 col-xl-3">
            <a class="btn btn-link w-100 text-info pointer" v-b-toggle.collapseSynonyms role="button"><b>Synonyms</b></a>
            <div class="border rounded p-3">
                <b-collapse visible class="collapse" id="collapseSynonyms">
                    <meta-synonyms :meta="meta"></meta-synonyms>
                </b-collapse>
            </div>
        </div>

        <div class="col-sm-12 col-md-6 col-lg-4 col-xl-3">
            <a class="btn btn-link w-100 text-info pointer" v-b-toggle.collapseStructure role="button"><b>Structure</b></a>
            <div class="border rounded p-3">
                <b-collapse visible class="collapse" id="collapseStructure">
                    <b-tabs content-class="mt-3">
                        <b-tab title="ASCII" active>
                            <meta-structure :meta="meta"></meta-structure>
                        </b-tab>
                    </b-tab>
                    <b-tab title="2D" disabled>

                    </b-tab>
                    <b-tab title="3D" disabled>

                    </b-tab>
                    </b-tabs>
                </b-collapse>
            </div>
        </div>

        <div class="col-sm-12 col-md-6 col-lg-4 col-xl-3">

            <a class="btn btn-link w-100 text-info pointer" v-b-toggle.collapseReferences role="button"><b>References</b></a>
            <div class="border rounded p-3">
                <b-collapse visible class="collapse" id="collapseReferences">
                    <meta-references :meta="meta"></meta-references>
                </b-collapse>
            </div>
        </div>

        <div class="col-sm-12 col-md-6 col-lg-4 col-xl-3">
            <a class="btn btn-link w-100 text-info pointer" v-b-toggle.collapseDescription role="button"><b>Description</b></a>
            <div class="border rounded p-3">
                <b-collapse visible class="collapse" id="collapseDescription">
                    <meta-description :meta="meta"></meta-description>
                </b-collapse>
            </div>
        </div>

        
        <div class="col-sm-12 col-md-6 col-lg-4 col-xl-3">
            <a class="btn btn-link w-100 text-info pointer" v-b-toggle.collapseDiscussion role="button"><b>Discussion</b></a>
            <div class="border rounded p-3">
                <b-collapse visible class="collapse" id="collapseDiscussion">
                    <meta-discussion :meta="meta" :user="user"></meta-discussion>
                </b-collapse>
            </div>
        </div>

    </div>

</div>`;