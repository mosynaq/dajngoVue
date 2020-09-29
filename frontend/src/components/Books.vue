<template>
  <div>

    <sui-card-group :stackable="true" class="centered doubling" v-if="booksLoaded">
      <book :title="item.title" :price="item.price"
            :description="item.description"
            :rating="item.rating" :image="item.image"
            :key="item.id" :type="item.type" :author="item.author"
            class="animate animate__bounceInLeft"
            v-for="item in items"/>
    </sui-card-group>

    <div v-else>
      <sui-card-group :stackable="true" class="centered doubling">
        <book_placeholder v-for="i in 6" :key="i"/>
      </sui-card-group>
    </div>
  </div>
</template>

<script>
import book from "./Book.vue";
import book_placeholder from "@/components/BookPlaceholder.vue";

export default {
  name: "books",
  components: {
    book,
    book_placeholder
  },
  props: {
    items: {
      type: Array,
      default: null
    },
    booksLoaded: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style scoped>

</style>