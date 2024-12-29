<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import Catalog from '@/components/Catalog.vue'
import InputText from 'primevue/inputtext'
import axios from 'axios'

const initialSearch = "Product";
const searchQuery = ref('')
const products = ref([])
const loading = ref(false)

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
  searchQuery.value = initialSearch;
  fetchProducts();
});

watch(searchQuery, fetchProducts)
</script>

<template>
  <div class="flex-container">
    <!-- Search bar -->
    <div class="row">
      <InputText
        v-model="searchQuery"
        class="large-input"
        type="text"
        size="large"
        placeholder="Search for a product..."
      />
    </div>

    <!-- Loading indicator -->
    <!--    <div class="row" v-if="loading" style="margin-top: 20px; text-align: center;">-->
    <!--      <p>Searching...</p>-->
    <!--    </div>-->

    <!-- Products catalog -->
    <div
      class="row"
      style="margin-top: 20px; border: 1px solid lightgrey; border-radius: 10px"
    >
      <Catalog :products="products" />
    </div>

    <!-- No results message -->
    <div class="row" v-if="!loading && products.length === 0 && searchQuery">
      <p>No products found for "{{ searchQuery }}"</p>
    </div>
  </div>
</template>

<style scoped>
.flex-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.large-input {
  width: 100%;
  min-width: 500px;
  max-width: 500px;
  font-size: 1.5rem;
}
</style>
