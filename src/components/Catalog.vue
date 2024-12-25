<script setup lang="ts">
import { ref, onMounted } from 'vue';
import Product from './Product.vue';

const products = ref([]);

const fetchProducts = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/products/');
    if (!response.ok) {
      throw new Error('Failed to fetch products');
    }
    const data = await response.json();

    products.value = data;
  } catch (error) {
    console.error('Error fetching products:', error);
  }
};

onMounted(() => {
  fetchProducts();
});
</script>

<template>
  <div class="grid-container">
    <div
      v-for="(product, index) in products"
      :key="index"
      class="grid-item"
    >
      <Product :product="product" />
    </div>
  </div>
</template>

<style scoped>
/* Grid container for evenly spaced layout */
.grid-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 4 columns */
  gap: 20px; /* Spacing between items */
  justify-content: center; /* Center items horizontally */
  align-items: center; /* Center items vertically */
  width: 100%; /* Full width of the container */
  padding: 20px; /* Optional: padding around the grid */
  max-height: 400px; /* Limit the visible height to fit 8 items */
  overflow-y: auto;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
  border-radius: 10px;
}

/* Grid item styling */
.grid-item {
  display: flex;
  justify-content: center; /* Center content inside the grid item */
  align-items: center; /* Center content inside the grid item */
}
</style>
