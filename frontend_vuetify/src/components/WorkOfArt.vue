<template>
  <v-card elevation="2">
    <v-img :src="this.image" height="175" width="300"></v-img>
    <v-card-title>
      <span>
        <v-icon v-if="this.type == 'book'">mdi-book</v-icon>
        <v-icon v-else>mdi-file</v-icon>
        {{ this.title }}
      </span>
    </v-card-title>
    <v-card-subtitle>
      <span class="float-right">${{ this.price }}</span>
      <v-rating
        :value="this.rating"
        color="amber"
        dense
        half-increments
        readonly
        size="16"
      ></v-rating>
    </v-card-subtitle>
    <v-card-text>
      {{ this.description | truncate(200) }}
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "WorkOfArt",
  props: {
    id: {
      type: Number,
      default: null
    },
    title: {
      type: String,
      default: "some title"
    },
    price: {
      type: Number,
      default: 0
    },
    description: {
      type: String,
      default: "book description"
    },
    rating: {
      type: Number,
      default: 0
    },
    image: {
      type: String,
      default: null
    },
    type: {
      type: String,
      default: "book"
    },
    author: {
      type: Object,
      default: null
    }
  }
};
</script>

<style scoped>
.work-of-art-type-label {
  opacity: 0.5;
}
</style>
