<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, watch } from 'vue';
import FilteringSideBar from '@/components/FilteringSideBar.vue';
import Product from '../components/Product.vue';
import InputText from 'primevue/inputtext';
import axios from 'axios'

const initialSearch = 'Product';
const searchQuery = ref('');
const products = ref([]);
const nextPage = ref(1);
const loading = ref(false);
const hasMore = ref(true);

const appliedFilters = ref({
  selectedCategory: null,
  selectedBrand: null,
  selectedColor: null,
  selectedRating: null,
  priceRange: [0, 500],
  inStock: false
})

const emit = defineEmits(['handle-create-product', 'handle-edit-product']);

function handleCreateProduct() {
  emit('handle-create-product', true);
}

// Fetch Products
const fetchProductsPagination = async (isNewSearch = false) => {
  if (loading.value || (!hasMore.value && !isNewSearch)) return; // Prevent duplicate requests
  loading.value = true;

  if (isNewSearch) {
    nextPage.value = 1; // Reset pagination
    products.value = []; // Clear existing products
    hasMore.value = true; // Reset the hasMore flag
  }

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/products/?page=${nextPage.value}&q=${encodeURIComponent(searchQuery.value)}`
    );
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

async function handleFiltersUpdate(filters: any) {
  appliedFilters.value = filters;

  const mustQueries: any[] = [];

  // Include search query for product names
  if (searchQuery.value) {
    mustQueries.push({
      match: { name: searchQuery.value }, // Adjust the field name to match your Elasticsearch mapping
    });
  }

  if (filters.selectedCategory?.length) {
    const categories = filters.selectedCategory.map((c: any) => c.value || c);
    mustQueries.push({ terms: { 'category.keyword': categories } });
  }

  if (filters.selectedBrand?.length) {
    const brands = filters.selectedBrand.map((b: any) => b.value || b);
    mustQueries.push({ terms: { 'brand.keyword': brands } });
  }

  if (filters.selectedColor?.length) {
    const colors = filters.selectedColor.map((c: any) => c.value || c);
    mustQueries.push({ terms: { 'color.keyword': colors } });
  }

  // Fix for rating filter
  if (filters.selectedRating?.length) {
    const ratings = filters.selectedRating.map((r: any) => r.value || r);
    mustQueries.push({
      terms: { rating: ratings }, // Ensure 'rating' matches the field name in Elasticsearch
    });
  }

  if (filters.inStock !== null && filters.inStock !== undefined) {
    mustQueries.push({ match: { is_available: filters.inStock } });
  }

  if (filters.priceRange?.length === 2) {
    mustQueries.push({
      range: {
        price: {
          gte: filters.priceRange[0],
          lte: filters.priceRange[1],
        },
      },
    });
  }

  const esQuery = {
    query: {
      bool: { must: mustQueries },
    },
  };

  try {
    const response = await axios.post(
      'http://127.0.0.1:9200/products/_search',
      esQuery
    );

    const hits = response.data.hits.hits;
    products.value = hits.map((hit: any) => ({
      id: hit._id,
      ...hit._source,
    }));
  } catch (error) {
    console.error("Error fetching filtered products:", error.response?.data || error.message);
  }
}

// Watch Search Query
watch(searchQuery, () => {
  handleFiltersUpdate(appliedFilters.value); // Refetch products with updated search query
});

// Handle Scroll Event
const handleScroll = () => {
  const container = document.querySelector('.grid-container');
  if (
    container &&
    container.scrollTop + container.clientHeight >= container.scrollHeight - 10
  ) {
    fetchProductsPagination();
  }
};


// Initialize Scroll Listener
onMounted(() => {
  searchQuery.value = initialSearch;
  fetchProductsPagination(); // Load the first batch of products

  const container = document.querySelector('.grid-container');
  if (container) {
    container.addEventListener('scroll', handleScroll);
  }
});

// Cleanup Scroll Listener
onBeforeUnmount(() => {
  const container = document.querySelector('.grid-container');
  if (container) {
    container.removeEventListener('scroll', handleScroll);
  }
});
</script>


<template>
  <div class="flex-container">
    <FilteringSideBar @update-filters="handleFiltersUpdate" />

    <!-- Search and Create Product -->
    <div class="row">
      <div class="column">
        <InputText
          v-model="searchQuery"
          class="large-input"
          type="text"
          size="large"
          placeholder="Search for a product..."
        />
      </div>
      <div class="column">
        <button id="create-product-btn" @click="handleCreateProduct">+</button>
      </div>
    </div>

    <!-- Product Grid -->
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

    <!-- No results message -->
    <div class="row" v-if="!loading && products.length === 0 && searchQuery">
      <p>No products found for "{{ searchQuery }}"</p>
    </div>
  </div>
</template>

<style scoped>
.row {
  display: flex; /* Flex container to arrange children in a row */
  align-items: center; /* Vertically align items */
  justify-content: space-between; /* Add space between columns */
  gap: 10px; /* Space between columns */
}

.column {
  flex: 1; /* Each column takes equal width */
  max-width: 50%; /* Optional: Limit column width */
}

.large-input {
  width: 100%;
  max-width: 500px;
  font-size: 1.5rem;
}

#create-product-btn {
  background-color: #4CAF50; /* Green background */
  border: 2px solid #ccc; /* Grey border */
  color: white; /* White text */
  font-size: 30px; /* Font size */
  font-weight: bold; /* Bold text */
  padding: 5px; /* Padding for spacing */
  max-width: 100%; /* Button spans full width of its column */
  border-radius: 5px; /* Rounded corners */
  cursor: pointer; /* Pointer cursor on hover */
  transition: all 0.3s ease; /* Smooth hover effect */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow for a cool effect */
}

#create-product-btn:hover {
  background-color: #45a049; /* Slightly darker green on hover */
  border-color: #aaa; /* Darker grey border on hover */
  transform: scale(1.1); /* Slightly enlarge the button */
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2); /* Stronger shadow on hover */
}

.flex-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

/* Grid container styling */
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
