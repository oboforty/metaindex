import {template} from "/js/components/meta/meta-description.vue.js";


export let component = Vue.component('meta-description', {
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