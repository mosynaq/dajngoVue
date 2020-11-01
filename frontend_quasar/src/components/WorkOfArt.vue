<template>
  <q-card class="my-card Lato">
    <q-img :src="this.image" :alt="this.title" :ratio="4/3" style="height: 170px; max-width: 300px"/>
    <q-card-section>
      <div class="text-h6 LatoBold">{{ this.title }}</div>
      <!--        <div class="text-subtitle2">{{ this.description }}</div>-->
    </q-card-section>
    <q-card-section class="q-pt-none">
      {{ this.description }}
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: 'WorkOfArt',
  props: {
    title: {
      type: String,
      default: null
    },
    description: {
      type: String,
      default: null
    },
    image: {
      type: String,
      default: null
    }
  }
}
</script>
<style lang="scss" scoped>
.my-card {
  //width: 100%;
  max-width: 250px
}

</style>
