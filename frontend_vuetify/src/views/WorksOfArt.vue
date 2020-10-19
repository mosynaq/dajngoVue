<template>
  <v-item-group>
    <v-container fluid>
      <v-row dense>
        <v-col v-for="workOfArt in worksOfArt" :key="workOfArt.id">
          <v-item>
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
          </v-item>
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>
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
