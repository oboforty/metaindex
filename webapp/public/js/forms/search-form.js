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
    },
  },

  mounted() {
    if (Cookies["accept_terms"] == 'true') {
      this.accept_terms = true;
    }

    if (Cookies["selected"]) {
      this.selected = Cookies["selected"].split("|");
    } else {
      this.selected = this.attributes_db.concat(this.attributes)
    }
  },

  data() {
    let _data = {
      attributes_db: store.settings.databases.map(db=>db.lower()),
      attributes: [
        'Name',
        'Formula',
        'SMILES',
        'InChI',
        // 'Mass',
        // 'Mmi',
      ],
      selected: [],

      do_discovery: true,
      accept_terms: false,

      // Search term:
      search_term: "",
    };

    // load from predecessor
    if (search_predecessor != null) {
      _data.search_term = search_predecessor.search_term;

      _data.attributes_db = search_predecessor.attributes_db;
      _data.attributes = search_predecessor.attributes;
      _data.selected = search_predecessor.selected;

      this.url = search_predecessor.url;

      search_predecessor = null;
    }

    return _data;
  },

  methods: {
    onTyping: function() {
      if (!this.accept_terms)
        // website does not search until legal requirements are met with service use
        return;
      else if (this.search_term.length < search_min_chars)
        // save network traffic before the first N characters
        return;
      else if (this.savePredecessorForm) {
        // save as predecessor (for upcoming search bar)
        // this is used for passing search-form data between different vue pages
        search_predecessor = this;
      }

      if (this.$listeners['search'])
        this.$emit('search', this.search_term);

      // only submit query if has result listeners
      if (this.$listeners['results']) {
        // create attr flags to save space
        //let attr_flags = this.selected.map(s=>s.substring(0,3)).join("|");
        let attr_flags = this.selected.join("|");
        
        if ((this.attributes.concat(this.attributes_db)).filter((elem) => {
          return this.selected.indexOf(elem) > -1;
        }).length == this.selected.length)
          // all selected
          attr_flags = 'all';

        // start searching the API
        request(`GET ${this.url}?attr=${attr_flags}&s=${this.search_term}`, {
        }, results=>{
          this.$emit('results', results);
        });
      }
    }
  },

  watch: {
    accept_terms(val) {
      if (val || val == 'true')
        Cookies["accept_terms"] = true;
      else
        Cookies["accept_terms"] = false;
    },

    selected(val) {
      Cookies["selected"] = val.join("|");
    }
  }
});
