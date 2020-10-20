<template>
  <v-card>
    <v-card-title>{{ this.last_name }}, {{ this.first_name }}</v-card-title>
    <v-card-subtitle>
      {{ this.date_of_birth | moment("YYYY, Qo MMMM") }}</v-card-subtitle
    >
    <v-card-text>{{ this.bio | truncate(250) }}</v-card-text>
    <v-card-actions>
      <v-btn
        color="deep-purple lighten-2"
        text
        @click="
          $router.push({
            name: 'authorSingle',
            params: { id: this.id.toString() }
          })
        "
      >
        Read on...
      </v-btn>
    </v-card-actions>
  </v-card>
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
