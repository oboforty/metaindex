import {template} from "/js/pages/page-search.vue.js"


export let PageSearch = Vue.component('page-search', {
  template: template,

  data: function() {
    return {
      show: false
    };
  },

  methods: {
    OnSearchResults(term, results) {
      let res = this.$refs['search-results'];

      res.results = results;
      res.search_term = term;
    }
  }
});
