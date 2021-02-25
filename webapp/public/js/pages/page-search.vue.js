export const template = `<div v-if="show" class="container">
  <search-form ref="search-form" @results="addResults" class="m-4"></search-form>

  <search-results ref="search-results"></search-results>
</div>`;