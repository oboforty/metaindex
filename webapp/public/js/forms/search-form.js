import {template} from "/js/forms/search-form.vue.js"

export let component = Vue.component('search-form', {
  template: template,

  data: function() {
    var db = this.settings.discovery.databases.map(db=>db.lower());

    var types = [
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

    return {
      searchtype_selected: types[0].lower(),
      searchtypes_available: types,

      db_enabled: db,
      db_available: db
    }
  },

  methods: {
  }
});
