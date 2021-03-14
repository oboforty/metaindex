import {template} from "/js/forms/molsearch-form.vue.js";
import {store} from '/js/store.js';
import {request} from '/js/api.mjs';


export let component = Vue.component('molsearch-form', {
  template: template,

  props: {
    savePredecessorForm: {
      type: Boolean,
      default: true
    },

    url: {
      default: '/metabolite/search'
    },

    molurl: {
      default: '/molsearch'
    }
  },

  data() {
    var db = store.settings.discovery.databases.map(db=>db.lower());

    return {
      db_enabled: db,
      db_available: db,

      jsme_mol2inchi: null,
      jsme: null,

      molsearch_option: 'inchi',
      molsearch_options: [
        'inchi',
        'MOL',
      ]
    };
  },

  methods: {

    onSearch() {
      if (this.jsme == null) {
        alert("Error: JSME Component not found!");
        return;
      }

      let mol = this.jsme.molFile();
      let search_val;
      let search_attr;

      if (this.molsearch_option == 'inchi') {
        let res = this.jsme_mol2inchi(mol);

        // search by inchi
        // res.auxinfo, res.inchi
        search_attr = 'inchikey';
        search_val = res.key;
      } else {
        // search by mol
        const mol_serialized = "??";

        console.log("TODO search mol");

        search_attr = 'mol';
        search_val = mol_serialized;
      }

      if (this.$listeners['results']) {
        request(`GET ${this.url}?attr=${search_attr}&s=${search_val}`, {
        }, results=>{
          this.$emit('results', results);
        });
      }
    }
  }
});
