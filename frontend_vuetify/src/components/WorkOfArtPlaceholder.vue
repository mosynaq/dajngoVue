<template>
  <div class="ui card">
    <div class="image">
      <div class="ui placeholder">
        <div class="image"></div>
      </div>
    </div>
    <div class="content">
      <div class="ui placeholder">
        <div class="header">
          <div class="long line"></div>
          <div class="medium line"></div>
        </div>
        <sui-label
          attached="top right"
          color="black"
          class="work-of-art-type-label"
        >
          <sui-icon
            name="question mark"
            :fitted="true"
            size="small"
            class="work-of-art-type-label"
          />
        </sui-label>
        <div class="paragraph">
          <div class="very long line"></div>
          <div class="very long line"></div>
          <div class="very long line"></div>
          <div class="very long line"></div>
          <div class="short line"></div>
        </div>
      </div>
    </div>
    <div class="extra content">
      <sui-rating :max-rating="5" :disabled="true" />
      <div class="right floated">
        <sui-icon name="dollar" />
        <div class="short line"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "WorkOfArtPlaceholder"
};
</script>

<style scoped>
.work-of-art-type-label {
  opacity: 0.5;
}
</style>
