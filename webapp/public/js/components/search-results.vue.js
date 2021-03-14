export const template = `<div class="list-group">
  <div v-for="result in results" class="list-group-item pointer" @click="OnClick(result)">
    <h4 :meta_id="result.entity_id">{{ result.display }}</h4>

    <p :search_attr="result.search_attr" v-html="showText(result)"></p>
  </div>
</div>`;