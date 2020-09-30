<template>
  <div>

    <sui-card-group :stackable="true" class="centered doubling" v-if="booksLoaded">
      <book v-for="workOfArt in worksOfArt" :key="workOfArt.id"
            :title="workOfArt.title" :price="workOfArt.price"
            :description="workOfArt.description"
            :rating="workOfArt.rating" :image="workOfArt.image"
            :type="workOfArt.type" :author="workOfArt.author"
            class="animate animate__bounceInLeft"
      />
    </sui-card-group>

    <div v-else>
      <sui-card-group :stackable="true" class="centered doubling">
        <book_placeholder v-for="i in 6" :key="i"/>
      </sui-card-group>
    </div>
  </div>
</template>

<script>
import config from "../../config.json"
import book from "./Book.vue";
import book_placeholder from "@/components/BookPlaceholder.vue";
import axios from "axios";

export default {
  name: "books",
  components: {
    book,
    book_placeholder
  },
  data() {
    return {
      worksOfArt: null,
      worksOfArtPrevPage: null,
      worksOfArtNextPage: null,
    }
  },
  mounted() {
    axios.get(config.api_worksOfArt_url)
        .then(response => {
              this.worksOfArt = response.data.results;
              this.worksOfArtPrevPage = response.data.previous;
              this.worksOfArtNextPage = response.data.next;
            }
        )
  },
  props: {
    booksLoaded: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style scoped>

</style>