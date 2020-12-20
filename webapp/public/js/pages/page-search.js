import {template} from "/js/pages/page-search.vue.js"


export let PageSearch = Vue.component('page-search', {
  template: template,

  data: function() {
    return {
      show: false
    };
  },

  methods: {
    init: function() {
      // runs when jinja page is initialized with this vue.js page

    },

    OnSearchResults(term, results) {
      let res = this.$refs['search-results'];

      res.results = results;
      res.search_term = term;
    }
  }
});
