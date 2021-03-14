export const template = `<div>
  <!-- Search bar -->
  <div class="input-group">
    <div class="input-group-prepend">
      <span class="input-group-text"><span class="ra ra-3x ra-magnifying-glass"></span></span>
    </div>

    <textarea ref="search-input" v-model="search_term" @keyup="onTyping" v-autofocus class="form-control" placeholder="Search for ID, Chemical name, Structure string, etc..."></textarea>
  </div>

  <!-- Advanced search -->
  <div>
    <span class="float-right">
      <a class="btn btn-link text-primary nounderline" href="/search-molecules">Molecule Search</a>

      <a class="btn btn-link text-primary pointer" v-b-toggle.collapseAdvanced role="button" aria-expanded="false" aria-controls="collapseAdvanced">Search options</a>
    </span>

    <br class="clearfix"/>

    <b-collapse class="collapse" id="collapseAdvanced">
      <div class="d-flex justify-content-end">
        <div class="p-2">
          <p class="text-small">Search areas:</p>

          <b-form-checkbox-group
            v-model="db_enabled"
            :options="db_available"
            name="flavour-2a"
            stacked
          ></b-form-checkbox-group>
        </div>

        <div class="ml-4 p-2">
          <p class="text-small">Search type:</p>

          <b-form-radio name="searchtype"
            v-for="searchtype in searchtypes_available" :key="searchtype"
            v-model="searchtype_selected" :value="searchtype.lower()">
            {{ searchtype }}
          </b-form-radio>
        </div>
        <div class="p-2">
          <!-- <p class="text-small">Extra search:</p> -->
        </div>
      </div>
    </b-collapse>
  </div>
</div>

</div>`;