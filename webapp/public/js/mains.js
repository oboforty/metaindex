import {PageIndex} from '/js/pages/page-index.js';
import {PageSearch} from '/js/pages/page-search.js';
import {PageMeta} from '/js/pages/page-meta.js';
import {PageMolSearch} from '/js/pages/page-molsearch.js';

import {store} from '/js/store.js';
import {colorize_moltext} from '/js/model/molutils.js';

let gui = null;

export function init_pages(page, settings, user, ...page_args) {
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
        let page = gui.page(name);

        history.pushState({}, "", page.url);
        return page;
      },

      molcol(text) {
        return colorize_moltext(text);
      }
    }
  });

  store.settings = settings;
  store.user = user;

  // gui:
  gui = new Vue({
    el: '#app-pages',

    // components: [
    //   PageIndex,
    //   PageSearch,
    //   PageMeta
    // ],

    data: {
      current: `page-${page}`,
    },
    mounted() {
      let _page = this.page(this.current);

      if (_page == null || !_page.init)
        throw "Page not found: "+this.current;
      
      _page.show = true;
      _page.init(...page_args);
    },
    methods: {
      page(name) {
        if (name.substring(0,5) != 'page-')
          name = 'page-'+name;

        return this.$refs[name];
      },

      show(name) {
        if (this.current != null)
          this.page(this.current).show = false;
        
        this.current = name;
        this.page(this.current).show = true;
      },

      hide(name) {
        if (name != null)
          this.page(name).show = false;
        else if (this.current != null) {
          this.page(this.current).show = false;
          this.current = null;
        }
      }
    },
  });

  window.gui = gui;
  return gui;
}
