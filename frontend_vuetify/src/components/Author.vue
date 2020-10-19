<template>
  <v-card elevation="2"></v-card>
</template>

<script>
export default {
  name: "author",
  props: {
    id: {
      type: Number,
      default: null
    },
    first_name: {
      type: String,
      default: null
    },
    last_name: {
      type: String,
      default: null
    },
    date_of_birth: {
      type: String,
      default: null
    },
    bio: {
      type: String,
      default: null
    }
  }
};
</script>

<style scoped></style>
