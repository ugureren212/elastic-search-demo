<script setup lang="ts">
import { defineEmits, onMounted, ref, watch } from 'vue'
import Catalog from '@/components/Catalog.vue'
import InputText from 'primevue/inputtext'
import axios from 'axios'
import FilteringSideBar from '@/components/FilteringSideBar.vue'

const initialSearch = "Product";
const searchQuery = ref('')
const products = ref([])
const loading = ref(false)

const appliedFilters = ref({
  selectedCategory: null,
  selectedBrand: null,
  selectedColor: null,
  selectedRating: null,
  priceRange: [0, 500],
  inStock: false,
});

const emit = defineEmits(['handle-create-product', 'handle-edit-product']);

async function handleFiltersUpdate(filters: any) {
  appliedFilters.value = filters;

  // Build Elasticsearch query
  const mustQueries = [];

  if (filters.selectedCategory) {
    mustQueries.push({ match: { category: filters.selectedCategory } });
  }
  if (filters.selectedBrand) {
    mustQueries.push({ match: { brand: filters.selectedBrand } });
  }
  if (filters.selectedColor) {
    mustQueries.push({ match: { color: filters.selectedColor } });
  }
  if (filters.selectedRating) {
    mustQueries.push({ match: { rating: filters.selectedRating } });
  }
  if (filters.inStock) {
    mustQueries.push({ match: { is_available: true } });
  }
  // Price range filter
  if (filters.priceRange && filters.priceRange.length === 2) {
    mustQueries.push({
      range: {
        price: {
          gte: filters.priceRange[0],
          lte: filters.priceRange[1],
        },
      },
    });
  }

  // Elasticsearch query body
  const esQuery = {
    query: {
      bool: {
        must: mustQueries,
      },
    },
  };

  try {
    // Make a request to Elasticsearch
    const response = await axios.post(
      'http://127.0.0.1:9200/products/_search',
      esQuery
    );

    // Extract and update products
    const hits = response.data.hits.hits;
    products.value = hits.map((hit: any) => ({
      id: hit._id,
      ...hit._source,
    }));

    console.log('Filtered Products:', products.value);
  } catch (error) {
    console.error('Error fetching filtered products:', error);
  }
}

function handleCreateProduct(){
  emit('handle-create-product', true);
}
function handleEditProduct(product: any){
  emit('handle-edit-product', true, product);
}

async function handleDeleteProduct(id: number) {
  try {
    await axios.delete(`http://127.0.0.1:9200/products/_doc/${id}`)
    products.value = products.value.filter(product => product.id !== id)
    console.log(`Product with ID ${id} deleted successfully from Elasticsearch.`)
  } catch (error) {
    console.error(`Error deleting product with ID ${id}:`, error)
  }
}

const fetchProducts = async () => {
  if (!searchQuery.value) {
    products.value = []
    return
  }
  loading.value = true
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/products/search/', {
      params: { q: searchQuery.value }
    })
    // console.log('response.data: ', response)
    products.value = response.data
  } catch (error) {
    console.error('Error fetching products:', error)
    products.value = []
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  searchQuery.value = initialSearch
  fetchProducts()
})

watch(searchQuery, fetchProducts)
</script>

<template>
  <div class="flex-container">
    <FilteringSideBar @update-filters="handleFiltersUpdate"/>
    <!-- Search bar -->
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

    <!-- Loading indicator -->
    <!--    <div class="row" v-if="loading" style="margin-top: 20px; text-align: center;">-->
    <!--      <p>Searching...</p>-->
    <!--    </div>-->

    <!-- Products catalog -->
    <div class="row">
      <Catalog @handle-edit-product="handleEditProduct" @handle-delete-product="handleDeleteProduct" :products="products" />
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
</style>
