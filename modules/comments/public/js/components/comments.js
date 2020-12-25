import {template} from "/comments/js/components/comments.vue.js";


export let component = Vue.component('comment', {
  template: template,

  data() {
    return {
      show: false,
      comments: [],
      user: null,
    };
  },

  methods: {
    
  }
});
