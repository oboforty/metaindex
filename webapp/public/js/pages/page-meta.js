import {template} from "/js/pages/page-meta.vue.js"

import {component as metaSynonyms} from "/js/components/meta/meta-synonyms.js";
import {component as metaDescr} from "/js/components/meta/meta-description.js";
import {component as metaReferences} from "/js/components/meta/meta-references.js";
import {component as metaRefExtra} from "/js/components/meta/meta-refextra.js";

import {component as metaStructure} from "/js/components/meta/meta-structure.js";
import {component as meta3dStruct} from "/js/components/meta/meta-struct3d.js";
import {component as meta2dStruct} from "/js/components/meta/meta-struct2d.js";

import {component as metaOnthology} from "/js/components/meta/meta-onthology.js";
import {component as metaPathway} from "/js/components/meta/meta-pathway.js";
import {component as metaTaxonomy} from "/js/components/meta/meta-taxonomy.js";

import {component as metaCiting} from "/js/components/meta/meta-citing.js";

export let PageMeta = Vue.component('page-meta', {
  template: template,
  components: [
    metaSynonyms,
    metaDescr,
    metaReferences,
    metaRefExtra,
    metaStructure,
    meta3dStruct,
    metaOnthology,
    metaPathway,
    metaTaxonomy,
    metaCiting
  ],

  data: function() {
    return {
      show: false,
      meta: null,
      meta_id: null,
    };
  },

  methods: {
    init: function(meta_id, metabolite) {
      // runs when jinja page is initialized with this vue.js page
      this.meta_id = meta_id;
      this.meta = metabolite;
    },
  },

});
