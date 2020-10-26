<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <WorkOfArt v-for="workOfArt in worksOfArt" :key="workOfArt.id"
                :title="workOfArt.title"
                :description="workOfArt.description"
                :image="workOfArt.image"
    />

  </div>
</template>

<script>

import WorkOfArt from '../components/WorkOfArt.vue'
import config from '../../config.json'

export default {
  name: 'WorksOfArt',
  components: {
    WorkOfArt
  },
  data () {
    return {
      worksOfArt: null
    }
  },
  methods: {
    getWorksOfArt () {
      this.$axios.get(config.api.worksOfArt_url)
        .then((response) => {
          this.worksOfArt = response.data.results
          // console.log(response.data.results)
        })
    }
  },
  mounted () {
    this.getWorksOfArt()
  }
}
</script>

<style scoped>

</style>
