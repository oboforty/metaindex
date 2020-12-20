import {template} from "/js/components/meta/meta-structure.vue.js";


export let component = Vue.component('meta-structure', {
    template: template,
    
    props: {
        meta: {
            default: null
        }
    },

    data() {
      return {
      };
    },
  
    methods: {
    }
});