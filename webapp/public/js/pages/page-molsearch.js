import {component as anyad} from '/js/forms/molsearch-form.js';



export let PageMolSearch = Vue.component('page-molsearch', {

  props: {
    url: {
      default: "/molsearch"
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
