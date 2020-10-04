<template>
  <div>
    <sui-card-group
      :stackable="true"
      class="centered doubling"
      v-if="worksOfArt"
    >
      <WorkOfArt
        v-for="workOfArt in worksOfArt"
        :key="workOfArt.id"
        :id="workOfArt.id"
        :title="workOfArt.title"
        :price="workOfArt.price"
        :description="workOfArt.description"
        :rating="workOfArt.rating"
        :image="workOfArt.image"
        :type="workOfArt.type"
        :author="workOfArt.author"
        class="animate animate__bounceInLeft"
      />
    </sui-card-group>

    <div v-else>
      <sui-card-group :stackable="true" class="centered doubling">
        <WorkOfArtPlaceholder v-for="i in 6" :key="i" />
      </sui-card-group>
    </div>
  </div>
</template>

<script>
import config from "../../config.json";
import WorkOfArt from "../components/WorkOfArt.vue";
import WorkOfArtPlaceholder from "@/components/WorkOfArtPlaceholder.vue";
import axios from "axios";

export default {
  name: "WorksOfArt",
  components: {
    WorkOfArt,
    WorkOfArtPlaceholder
  },
  data() {
    return {
      worksOfArt: null,
      worksOfArtPrevPage: null,
      worksOfArtNextPage: null
    };
  },
  mounted() {
    axios.get(config.api_worksOfArt_url).then(response => {
      this.worksOfArt = response.data.results;
      this.worksOfArtPrevPage = response.data.previous;
      this.worksOfArtNextPage = response.data.next;
    });
  },
  props: {
    booksLoaded: {
      type: Boolean,
      default: false
    }
  }
};
</script>

<style scoped></style>
