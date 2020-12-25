import {PageIndex} from '/js/pages/page-index.js';
import {PageSearch} from '/js/pages/page-search.js';
import {PageMeta} from '/js/pages/page-meta.js';

import {component as SearchForm} from '/js/forms/search-form.js';
import {component as SearchResults} from '/js/components/search-results.js';

import {store} from '/js/store.js';
import {colorize_moltext} from '/js/model/molutils.js';

let gui = null;

export function init_pages(page, settings, ...page_args) {
  Vue.directive('autofocus', {
    inserted: function (el) {
      el.focus();
    }
  });
  
  Vue.mixin({
    // mixin data isn't accessible in component data func
    methods: {
      open_page(name) {
        gui.show(name);
        
        return gui.page(name);
      },

      molcol(text) {
        return colorize_moltext(text);
      }
    }
  });

  store.settings = settings;

  // gui:
  gui = new Vue({
    el: '#app-pages',

    components: [
      PageIndex,
      PageSearch,
      PageMeta
    ],

    data: {
      current: `page-${page}`,
    },
    mounted() {
      let _page = this.page(this.current);
      
      _page.show = true;
      _page.init(...page_args);
    },
    methods: {
      page: function(name) {
        if (name.substring(0,5) != 'page-')
          name = 'page-'+name;

        return this.$refs[name];
      },

      show: function(name) {
        if (this.current != null)
          this.page(this.current).show = false;
        
        this.current = name;
        this.page(this.current).show = true;
      },

      hide: function(name) {
        if (name != null)
          this.page(name).show = false;
        else if (this.current != null) {
          this.page(this.current).show = false;
          this.current = null;
        }
      }
    },
  });
}
