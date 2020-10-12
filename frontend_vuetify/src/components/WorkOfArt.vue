<template>
  <sui-card>
    <sui-image :src="this.image" height="150" />
    <sui-card-content>
      <router-link
        class="header"
        :to="{ name: 'WorksOfArtSingle', params: { id: this.id } }"
      >
        {{ this.title }}
      </router-link>
      <sui-card-meta>
        By {{ this.author.last_name + ", " + this.author.first_name }}
      </sui-card-meta>

      <sui-label
        attached="top right"
        color="black"
        class="work-of-art-type-label"
      >
        <sui-icon name="book" v-if="this.type === 'book'" />
        <sui-icon name="file" v-if="this.type === 'article'" />
        {{ this.type | titleCase }}
      </sui-label>

      <sui-card-description>{{ this.description }}</sui-card-description>
    </sui-card-content>
    <sui-card-content extra>
      <sui-rating
        :rating="this.rating"
        :max-rating="5"
        :disabled="true"
        icon="yellow star"
      />
      <span class="right floated">
        <sui-icon name="dollar" />
        {{ this.price }}
      </span>
    </sui-card-content>
  </sui-card>
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
