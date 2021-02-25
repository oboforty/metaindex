import {template} from "/js/components/meta/meta-discussion.vue.js";
import {store} from "/js/store.js";

import {component as CommentsList} from "/comments/js/components/comments.js";


export let component = Vue.component('meta-discussion', {
    template: template,
    // components: [
    //     CommentsList
    // ],
    props: {
        meta: {
            default: null
        }
    },

    data() {
      return {
      };
    },
  
    computed: {
        user() {
            return store.user;
        }
    }
});