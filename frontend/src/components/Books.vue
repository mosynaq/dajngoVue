<template>
  <sui-card-group :stackable="true"  class="centered doubling">
    <book :title="item.title" :price="item.price"
          :description="item.description"
          :rating="item.rating" :image="item.image"
          :key="item.id" :type="item.type" :author="item.author"
          class="disabled"
          v-for="item in items"/>
  </sui-card-group>
</template>

<script>
import book from "./Book.vue";

export default {
  name: "books",
  components: {
    book
  },
  props: ["items"]
}
</script>

<style scoped>

</style>