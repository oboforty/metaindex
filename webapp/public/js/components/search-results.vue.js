export const template = `<div class="list-group">
  <div v-for="result in results" class="list-group-item pointer" @click="OnClick(result)">
    <h4 :result_key="result.result_key">{{ result.result_display }}</h4>

    <p :search_key="result.search_key" v-html="showText(result)"></p>
  </div>
</div>`;