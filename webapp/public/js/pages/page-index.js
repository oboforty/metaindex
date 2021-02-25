//import {template} from "/js/pages/page-index.vue.js"

import {component as SearchForm} from '/js/forms/search-form.js';
import {component as SearchResults} from '/js/components/search-results.js';

export let PageIndex = Vue.component('page-index', {
  //el: "#tpl-page-index",
  //template: template,
  
  props: {
    url: {
      default: "/"
    }
  },

  data() {
    return {
      show: true
    };
  },

  methods: {
    init() {
      // runs when jinja page is initialized with this vue.js page
    },
  },

  watch: {
    show(val) {
      if (!val) {
        // hide static HTML as well when index gets hidden
        $("#static-page-description").style.display = 'none';
      }
    }
  }
});
