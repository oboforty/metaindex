export const template = `<div class="rounded p-2 scroll meta-synonyms" style="background-color: #e9ecef;">
  <div v-for="name in meta.names">
    {{ name }}
  </div>
</div>`;