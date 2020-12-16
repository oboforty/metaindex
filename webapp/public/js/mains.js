import {PageIndex} from '/js/pages/page-index.js';
import {PageSearch} from '/js/pages/page-search.js';
import {PageMeta} from '/js/pages/page-meta.js';

import {component as SearchForm} from '/js/forms/search-form.js';

import {store} from '/js/store.js';

let gui = null;

export function init_pages(settings, user) {
  Vue.directive('autofocus', {
    inserted: function (el) {
      el.focus();
    }
  });
  
  Vue.mixin({
    // mixin data isn't accessible in component data func
    methods: {
      open_page: function(name) {
        gui.show(name);
        
        return gui.page(name);
      },
    }
  });

  store.settings = settings;
  store.user = user;

  // gui:
  gui = new Vue({
    el: '#app-pages',

    components: [
      PageIndex,
      PageSearch,
      PageMeta
    ],

    data: {
      current: 'page-index',
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
