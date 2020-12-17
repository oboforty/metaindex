export const template = `<div v-if="show">
  <search-form ref="search-form" @results="OnSearchResults" class="m-4"></search-form>

  <search-results ref="search-results"></search-results>
</div>`;