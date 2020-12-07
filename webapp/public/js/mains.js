import {component as SearchForm} from '/js/forms/search-form.js';

function init_mixins(settings, user) {
  // todo: setup doors acc?

  Vue.mixin({
    settings: settings,
  });
}


export function init_search(settings, user) {
  // mixins:
  init_mixins(settings, user);

  // gui:
  let gui = new Vue({
    el: '#app-search',

    data: {
    },
    methods: {
      child: function(name) {
        return this.$refs[name];
      },
    }
  });
}

export function init_view(settings, user, metabolite) {
  // mixins:
  init_mixins(settings, user);

  // gui:
  let gui = new Vue({
    el: '#app-view',

    data: {
    },
    methods: {
      child: function(name) {
        return this.$refs[name];
      },
    }
  });
}
