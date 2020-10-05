<template>
  <sui-card>
    <sui-card-content>
      <!--      <sui-image :src="this.image" height="150"/>-->
      <!--      <a class="header"> {{ this.last_name }}, {{ this.first_name }} </a>-->
      <router-link
        class="header"
        :to="{ name: 'author_single', params: { id: this.id } }"
      >
        {{ this.last_name }}, {{ this.first_name }}
      </router-link>
      <sui-card-meta>
        Born {{ this.date_of_birth | moment("YYYY, Qo MMMM") }}
      </sui-card-meta>
      <sui-card-description>
        {{ this.bio | truncate(250) }}
      </sui-card-description>
    </sui-card-content>
  </sui-card>
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
