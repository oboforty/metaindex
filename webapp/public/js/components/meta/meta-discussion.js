import {template} from "/js/components/meta/meta-discussion.vue.js";

import {component as CommentsList} from "/comments/js/components/comments.js";
import {component as CommentsInput} from "/comments/js/components/comment-box.js";


export let component = Vue.component('meta-discussion', {
    template: template,
    components: [
        CommentsInput,
        CommentsList
    ],
    props: {
        meta: {
            default: null
        },
        user: {
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