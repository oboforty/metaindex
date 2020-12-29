import {template} from "/comments/js/components/comments.vue.js";
import {request} from '/js/api.mjs';


export let component = Vue.component('comments', {
  template: template,
  props: {
    meta_id: {
      default: null
    },
    user: {
      default: null
    }
  },
  data() {
    return {
      comments: [],

      input_text: "",
    };
  },

  methods: {
    init() {
      // Constructor:
      this.show = true;

      if (this.user != null)
        this.list_comments();
    },

    onSendComment() {
      if (this.input_text == "")
        return;
      
      this.create_comment({
        content: this.input_text,
        parent_id: null,
      });

      this.input_text = "";
    },

    list_comments() {
      request(`GET ${this.url}`, {}, comments=>this.comments = comments);
    },
    
    create_comment(comment) {
      request(`POST ${this.url}`, comment, resp=>this.comments.push(Object.assign(comment, resp, {author: this.user})));
    },

    delete_comment(comment_id) {
      request(`DELETE ${this.url}/${comment_id}`, {}, ()=>{
        this.comments.splice(this.comments.filter(w=>w.cid == comment.cid), 1);
      });
    },
  },
  computed: {
    url() {
      return `/api/metabolite/${this.meta_id}/comments`;
    }
  },
  watch: {
    meta_id: {
      immediate: true,
      handler: function() {
        this.$nextTick(() => {
          this.init();
        });
      }
    }
  }
});
