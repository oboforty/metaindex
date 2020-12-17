//import {template} from "/js/pages/page-index.vue.js"
import {store} from '/js/store.js';


export let PageIndex = Vue.component('page-index', {
  //template: template,
  el: "#tpl-page-index",

  data: function() {
    return {
      show: true
    };
  },

  methods: {
    onTyping: function() {
      let search1 = this.$refs['search-form'];
      store.search_predecessor = search1;

      // navigate to page-search and pass required parameters
      this.open_page("search");
    }
  },

  watch: {
    show: function(val) {
      if (!val) {
        // hide static HTML as well when index gets hidden
        $("#static-page-description").style.display = 'none';
      }
    }
  }
});
