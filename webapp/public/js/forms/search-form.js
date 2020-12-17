import {template} from "/js/forms/search-form.vue.js";
import {store} from '/js/store.js';


export let component = Vue.component('search-form', {
  template: template,

  props: {
    onTypingOverride: {
      type: Function,
      default: null
    },
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

    if (store.search_predecessor != null) {
      // take search form data over previous page
      _data.search_term = store.search_predecessor.search_term;
      _data.db_enabled = store.search_predecessor.db_enabled;
      _data.searchtype_selected = store.search_predecessor.searchtype_selected;

      store.search_predecessor = null;
    }

    return _data;
  },

  methods: {
    onTyping: function() {
      if (this.onTypingOverride != null) {
        // Parent overrides searching
        this.onTypingOverride(this.search_term);
        return;
      }

      // without an override, start searching the API
      if (this.search_term.length > 3) {
        // todo: call api

        this.$emit('results', this.search_term, [
          {
            search_value: "C-vitamin",
            search_key: "name",
            
            result_display: "Ascorbic Acid",
            result_value: "rndid12345",
            result_key: "meta_id",
          },
          {
            search_value: "ascorbate",
            search_key: "name",

            result_display: "Display 2",
            result_value: "ascorbic_acid",
            result_key: "meta_id",
          },
        ]);
      }
    },

    onSelectItem: function() {

      console.log("TODO navigate and shit");
      //nav.navigate_to();
    }
  }
});
