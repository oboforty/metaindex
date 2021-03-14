export const template = `<div class="d-flex mb-3 mt-3">

    <b-form-checkbox-group
      v-model="molsearch_option"
      :options="molsearch_options"
      name="flavour-2a"
      stacked
    ></b-form-checkbox-group>

    <div class="ml-2">
      <button class="btn btn-lg btn-block btn-secondary" @click="onSearch">Search</button>
    </div>

</div>`;