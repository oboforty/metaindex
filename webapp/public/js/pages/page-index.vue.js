export const template = `<div v-if="show" class="container">
  <!-- Search bar area -->
  <div class="jumbotron mt-4">
    <!-- this shit gotta stay here for SEO -->
    <h6 class="lead text-success">Welcome to MetaSeeker!</h6>
    <p class="font-light">This is a public search engine dedicated to rapidly identify and label metabolites.</p>
    <p class="font-light text-danger font-small"><i>The search bar recognizes various input formats that can identify metabolites. <a href="/home/formats">See the full list of searchable formats.</a></i></p>

    <search-form ref="search-form" :on-typing-override="onTyping"></search-form>
  </div>
</div>`;