import {template} from "/js/forms/search-form.vue.js";
import {store} from '/js/store.js';
import {request} from '/js/api.mjs';

const search_min_chars = 3;
let search_predecessor = null;

export let component = Vue.component('search-form', {
  template: template,

  props: {
    savePredecessorForm: {
      type: Boolean,
      default: true
    },

    url: {
      default: '/metabolite/search'
    }
  },

  data() {
    var db = store.settings.discovery.databases.map(db=>db.lower());

    var types = [
      'Any',
      'Identifier',
      'Name',
      'SMILES',
      'InChI',
      'Formula',
      'Mass',
      'Pathway',
      'Structure',
      'Onthology',
    ];

    const _data = {
      // Advanced search:
      searchtype_selected: types[0].lower(),
      searchtypes_available: types,
      db_enabled: db,
      db_available: db,

      // Search term:
      search_term: "",
    };

    // load from predecessor
    if (search_predecessor != null) {
      _data.search_term = search_predecessor.search_term;
      _data.db_enabled = search_predecessor.db_enabled;
      _data.searchtype_selected = search_predecessor.searchtype_selected;
      this.url = search_predecessor.url;

      search_predecessor = null;
    }

    return _data;
  },

  methods: {
    onTyping: function() {
      if (this.search_term.length < search_min_chars)
        return;

      if (this.savePredecessorForm) {
        // save as predecessor (for upcoming search bar)
        search_predecessor = this;
      }

      //if (this.$listeners['search'])
        this.$emit('search', this.search_term);

      // only submit query if has result listeners
      if (this.$listeners['results']) {

        // start searching the API
        request(`GET ${this.url}?attr=${this.searchtype_selected}&s=${this.search_term}`, {
        }, results=>{
          this.$emit('results', results);
        });
      }
    },

    onSelectItem: function() {

      console.log("TODO navigate and shit");
      //nav.navigate_to();
    }
  }
});
