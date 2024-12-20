<script setup lang="ts">
const colors = [
  'red', 'blue', 'green', 'yellow', 'orange',
  'purple', 'pink', 'teal', 'brown', 'gray'
];
</script>

<template>
  <div class="grid-container">
    <div
      v-for="(color, index) in colors"
      :key="index"
      :style="{ backgroundColor: color }"
      class="grid-item"
    ></div>
  </div>
</template>

<style scoped>
/* Grid container for 5x2 layout */
.grid-container {
  display: grid;
  grid-template-columns: repeat(5, 1fr); /* 5 columns */
  grid-template-rows: repeat(2, 1fr); /* 2 rows */
  gap: 10px; /* Spacing between squares */
  width: 100%; /* Optional: adjust as needed */
}

/* Grid item styling */
.grid-item {
  width: 100px;
  padding-top: 100%; /* Maintains a square aspect ratio */
}
</style>
