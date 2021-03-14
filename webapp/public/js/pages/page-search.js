import {template} from "/js/pages/page-search.vue.js"


export let PageSearch = Vue.component('page-search', {
  template: template,
  
  props: {
    url: {
      default: "/search"
    },
    hardLinks: {
      default: false,
    }
  },

  data() {
    return {
      show: false
    };
  },

  methods: {
    init() {
      // runs when jinja page is initialized with this vue.js page

    },

    addResults(results) {
      this.$refs['search-results'].results = results;
    }
  }
});
