<template>
  <v-container fluid>
    <v-row :align="align">
      <v-col
        class="col-sm-6 col-md-4 col-12"
        v-for="workOfArt in worksOfArt"
        :key="workOfArt.id"
      >
        <WorkOfArt
          :id="workOfArt.id"
          :title="workOfArt.title"
          :price="workOfArt.price"
          :description="workOfArt.description"
          :rating="workOfArt.rating"
          :image="workOfArt.image"
          :type="workOfArt.type"
          :author="workOfArt.author"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import config from "../../config.json";
import WorkOfArt from "../components/WorkOfArt.vue";
import axios from "axios";

export default {
  name: "WorksOfArt",
  components: {
    WorkOfArt
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
