<template>
  <sui-card>
    <sui-card-content>
<!--      <sui-image :src="this.image" height="150"/>-->
      <a class="header">
        {{ this.last_name }}, {{ this.first_name }}
      </a>

      <sui-card-meta>
        Born {{ Date(this.date_of_birth) }}
      </sui-card-meta>

      <sui-card-description>
        {{ this.bio }}
      </sui-card-description>
    </sui-card-content>
  </sui-card>
</template>

<script>



export default {
  name: "author",
  props: {
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
  },
  filters:{

  }
}
</script>

<style scoped>

</style>