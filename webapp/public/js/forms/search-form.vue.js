export const template = `<div>
  <!-- Search bar -->
  <div class="input-group">
    <div class="input-group-prepend">
      <span class="input-group-text"><span class="ra ra-3x ra-magnifying-glass"></span></span>
    </div>

    <textarea ref="search-input" v-model="search_term" @keyup="onTyping" v-autofocus class="form-control" placeholder="Search for ID, Chemical name, Structure string, etc..."></textarea>
  </div>

  <!-- Advanced search -->
  <div class="search-wrapper">
    <span class="float-right">
      <a class="btn btn-link text-primary pointer" v-b-toggle.collapseAdvanced role="button" aria-expanded="false" aria-controls="collapseAdvanced">Search options</a>
    </span>

    <br class="clearfix"/>

    <b-collapse class="collapse mt-3 search-settings p-2 rounded shadow" id="collapseAdvanced">
      <div class="d-flex justify-content-end">
        <div class="p-2">
          Search field:
        </div>

        <div class="p-2">
          <b-form-checkbox-group
          v-model="selected"
          :options="attributes_db"
          name="flavour-2a"
          stacked
          ></b-form-checkbox-group>
        </div>

        <div class="ml-4 p-2">
          <b-form-checkbox-group
          v-model="selected"
          :options="attributes"
          name="flavour-2a"
          stacked
          ></b-form-checkbox-group>
        </div>
      </div>
      <div class="d-flex justify-content-end">
        <div class="p-2">
          <b-form-checkbox
            id="checkbox-1"
            v-model="do_discovery"
            name="checkbox-1"
          >
            Use discovery service
          </b-form-checkbox>
          
          <b-form-checkbox
            id="checkbox-terms"
            v-model="accept_terms"
            name="checkbox-terms"
          >
            I accept the terms and use
          </b-form-checkbox>

        </div>
      </div>
    </b-collapse>
  </div>
</div>

</div>`;