import {template} from "/js/pages/page-meta.vue.js"
import {store} from '/js/store.js';


export let PageMeta = Vue.component('page-meta', {
  template: template,

  data: function() {
    var db = store.settings.discovery.databases;

    return {
      show: false,
      meta: null,
      meta_id: null,

      databases: db,
    };
  },

  methods: {
    init: function(meta_id, metabolite) {
      // runs when jinja page is initialized with this vue.js page
      this.meta_id = meta_id;
      this.meta = metabolite;
    },
  },

  computed: {
    databases_filled() {
      return this.databases.filter(db=>Boolean(this.meta[db.lower()+"_id"]));
    }
  }
});
