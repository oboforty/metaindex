import {template} from "/js/components/meta/meta-references.vue.js";
import {store} from '/js/store.js';


export let component = Vue.component('meta-references', {
    template: template,
    
    props: {
        meta: {
            default: null
        },

        target: {
            default: "_blank"
        }
    },

    data: function() {
        const db = store.settings.databases;
    
        return {
          databases: db,
        };
    },
  
    methods: {
    },
    
    computed: {
        databases_filled() {
            return this.databases.filter(db=>Boolean(len(this.meta[db.lower()+"_id"])));
        }
    }
});