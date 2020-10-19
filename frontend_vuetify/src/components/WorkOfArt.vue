<template>
  <v-card elevation="2">
    <v-card-title>{{ this.title }}</v-card-title>
    <v-card-subtitle>{{ this.price }}</v-card-subtitle>
    <v-card-text>{{ this.description }}</v-card-text>
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
