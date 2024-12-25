<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue';
import Product from './Product.vue';

const products = ref([]); // Loaded products
const nextPage = ref(1); // Current page number
const loading = ref(false); // Loading state
const hasMore = ref(true); // If there are more products to load

const fetchProducts = async () => {
  if (loading.value || !hasMore.value) return; // Prevent duplicate requests
  loading.value = true;

  try {
    const response = await fetch(`http://127.0.0.1:8000/api/products/?page=${nextPage.value}`);
    if (!response.ok) {
      throw new Error('Failed to fetch products');
    }

    const data = await response.json();

    products.value.push(...data.results); // Append new products
    nextPage.value += 1; // Increment page number
    hasMore.value = !!data.next; // Check if there's a next page
  } catch (error) {
    console.error('Error fetching products:', error);
  } finally {
    loading.value = false;
  }
};

const handleScroll = () => {
  const container = document.querySelector('.grid-container');
  if (
    container &&
    container.scrollTop + container.clientHeight >= container.scrollHeight - 10
  ) {
    fetchProducts();
  }
};

onMounted(() => {
  fetchProducts(); // Load the first batch of products

  const container = document.querySelector('.grid-container');
  if (container) {
    container.addEventListener('scroll', handleScroll);
  }
});

onBeforeUnmount(() => {
  const container = document.querySelector('.grid-container');
  if (container) {
    container.removeEventListener('scroll', handleScroll);
  }
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
    <!-- Loading indicator -->
    <div v-if="loading" class="loading-indicator">Loading more products...</div>
    <!-- End of products message -->
    <div v-if="!hasMore && !loading" class="end-message">No more products</div>
  </div>
</template>

<style scoped>
/* Grid container for evenly spaced layout */
.grid-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 4 columns */
  gap: 20px; /* Spacing between items */
  justify-content: center; /* Center items horizontally */
  align-items: start; /* Align items at the top */
  width: 100%; /* Full width of the container */
  padding: 20px; /* Optional: padding around the grid */
  max-height: 55vh; /* Limit the visible height for scrolling */
  overflow-y: auto; /* Enable scrolling */
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
  border-radius: 10px;
}

/* Grid item styling */
.grid-item {
  display: flex;
  justify-content: center; /* Center content inside the grid item */
  align-items: center; /* Center content inside the grid item */
}

.loading-indicator {
  text-align: center;
  font-size: 1.2rem;
  margin-top: 20px;
}

.end-message {
  text-align: center;
  font-size: 1.2rem;
  margin-top: 20px;
  color: gray;
}
</style>
