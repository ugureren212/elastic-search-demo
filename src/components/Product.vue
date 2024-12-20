<script setup lang="ts">
import Card from 'primevue/card';

defineProps({
  product: Object, // Single product object
});

// Generate a random color that avoids white or very light shades
const randomColor = `#${Array.from({ length: 3 })
  .map(() => {
    const value = Math.floor(Math.random() * 200); // Limit value to 200 to avoid light colors
    return value.toString(16).padStart(2, '0'); // Convert to hex with padding
  })
  .join('')}`;

</script>

<template>
  <Card style="width: 15rem; overflow: hidden">
    <template #header>
      <div class="header" :style="{ backgroundColor: randomColor }">
        <p>{{ product.name }}</p>
      </div>
    </template>
    <template #title>{{ product.name }}</template>
    <template #content>
      <p>Category: {{ product.category }}</p>
      <p>Price: ${{ product.price }}</p>
    </template>
  </Card>
</template>

<style scoped>
/* Header styles */
.header {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px; /* Space between icon and name */
  padding: 15px;
  font-size: 1.5rem; /* Larger font size */
  color: #fff; /* White text for better contrast */
  font-weight: bold;
  text-align: center;
  border-radius: 5px 5px 0 0; /* Rounded corners on the top */
}
</style>
