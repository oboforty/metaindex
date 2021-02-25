import {template} from "/js/components/search-results.vue.js";

function splice_string(value, offset, text, removeCount=0) {
  let calculatedOffset = offset < 0 ? value.length + offset : offset;
  return value.substring(0, calculatedOffset) +
    text + value.substring(calculatedOffset + removeCount);
};

export let component = Vue.component('search-results', {
  template: template,

  data() {
    return {
        search_tag1: '<b class="text-danger"><i>',
        search_tag2: '</i></b>',
      
        results: [],
        search_term: "",
    };
  },

  methods: {
    showText(r) {
      let value = r.search_value;
      let term = this.search_term.lower();
    
      // case insensitive replace
      value = value.lower().replace(term, "<QQ>"+term.lower()+"</Q>");
      let i = value.indexOf("<QQ>");
      let j = value.indexOf("</Q>", i+4)-4;
      
      value = r.search_value;

      if (i>0 && j>0 && i<=value.length && j<=value.length && i != j) {
        // highlight search term
        value = splice_string(value, i, this.search_tag1);
        value = splice_string(value, j+this.search_tag1.length, this.search_tag2);
      }

      return `<span>${value}</span><br/><span class="small">(${r.search_key})</span>`;
    },

    OnClick(result) {
      
      let page = this.open_page('meta');
      // todo: set url somewhere?
      page.init('TTTT', {});

      // todo: load meta page

      // todo: pass param to meta page
    }
  }
});
