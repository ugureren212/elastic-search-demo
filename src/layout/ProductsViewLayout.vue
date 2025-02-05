<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import FilteringSideBar from '@/components/FilteringSideBar.vue'
import ProductCatalog from '../components/ProductCatalog.vue'
import InputText from 'primevue/inputtext'
import axios from 'axios'
import Button from 'primevue/button'

interface Product {
  id: string
  name: string
  price: number
  stock: number
  description: string
  category: string
  brand: string
  color: string
  rating: number
  is_available: boolean
}

interface ElasticsearchHit {
  _id: string
  _source: Omit<Product, 'id'>
}

interface FilterState {
  selectedCategory: { value: string }[] | null
  selectedBrand: { value: string }[] | null
  selectedColor: { value: string }[] | null
  selectedRating: { value: number }[] | null
  priceRange: [number, number]
  inStock: boolean
  notInStock: boolean
}

const fetchProducts = defineProps(['fetchProducts'])

const initialSearch = ''
const searchQuery = ref('')
const products = ref<Product[]>([])
const nextPage = ref(1)
const loading = ref(false)
const hasMore = ref(true)

const appliedFilters = ref<FilterState>({
  selectedCategory: null,
  selectedBrand: null,
  selectedColor: null,
  selectedRating: null,
  priceRange: [0, 500],
  inStock: true,
  notInStock: true,
})

const emit = defineEmits(['handle-create-product-overlay', 'handle-edit-product'])

const fetchProductsPagination = async (isNewSearch = false) => {
  if (loading.value || (!hasMore.value && !isNewSearch)) return
  loading.value = true

  if (isNewSearch) {
    nextPage.value = 1
    products.value = []
    hasMore.value = true
  }

  const mustQueries: Record<string, unknown>[] = []

  if (searchQuery.value) {
    mustQueries.push({ match: { name: searchQuery.value } })
  }

  if (appliedFilters.value.selectedCategory?.length) {
    const categories = appliedFilters.value.selectedCategory.map((c) => c.value)
    mustQueries.push({ terms: { 'category.keyword': categories } })
  }

  if (appliedFilters.value.selectedBrand?.length) {
    const brands = appliedFilters.value.selectedBrand.map((b) => b.value)
    mustQueries.push({ terms: { 'brand.keyword': brands } })
  }

  if (appliedFilters.value.selectedColor?.length) {
    const colors = appliedFilters.value.selectedColor.map((c) => c.value)
    mustQueries.push({ terms: { 'color.keyword': colors } })
  }

  if (appliedFilters.value.selectedRating?.length) {
    const ratings = appliedFilters.value.selectedRating.map((r) => r.value)
    mustQueries.push({ terms: { rating: ratings } })
  }

  if (appliedFilters.value.inStock !== null || appliedFilters.value.inStock !== undefined) {
    if (appliedFilters.value.inStock === true && appliedFilters.value.notInStock === true) {
    } else if (appliedFilters.value.inStock === true) {
      mustQueries.push({ match: { is_available: true } })
    } else if (appliedFilters.value.notInStock === true) {
      mustQueries.push({ match: { is_available: false } })
    }
  }

  if (appliedFilters.value.priceRange?.length === 2) {
    mustQueries.push({
      range: {
        price: {
          gte: appliedFilters.value.priceRange[0],
          lte: appliedFilters.value.priceRange[1],
        },
      },
    })
  }

  const esQuery = {
    query: {
      bool: { must: mustQueries },
    },
    from: (nextPage.value - 1) * 10,
    size: 16,
  }

  try {
    const response = await axios.post<{ hits: { hits: ElasticsearchHit[] } }>(
      'http://127.0.0.1:9200/products/_search',
      esQuery,
    )
    const hits = response.data.hits.hits
    products.value.push(
      ...hits.map((hit) => ({
        id: hit._id,
        ...hit._source,
      })),
    )
    nextPage.value += 1
    hasMore.value = hits.length > 0
  } catch (error) {
    if (error instanceof Error) {
      console.error('Error fetching paginated products:', error.message)
    }
  } finally {
    loading.value = false
  }
}

function handleFiltersUpdate(filters: FilterState) {
  appliedFilters.value = filters
  fetchProductsPagination(true)
}

function handleCreateProductOverlay() {
  emit('handle-create-product-overlay', true)
}

function handleEditProduct(product: Product) {
  emit('handle-edit-product', true, product)
}

const handleScroll = () => {
  const container = document.querySelector('.grid-container')
  if (container && container.scrollTop + container.clientHeight >= container.scrollHeight - 10) {
    fetchProductsPagination()
  }
}

async function handleDeleteProduct(id: string) {
  try {
    await axios.delete(`http://127.0.0.1:9200/products/_doc/${id}`)
    products.value = products.value.filter((product) => product._id !== id)
    console.log(`Product with ID ${id} deleted successfully from Elasticsearch.`)
  } catch (error) {
    if (error instanceof Error) {
      console.error(`Error deleting product with ID ${id}:`, error.message)
    }
  }
}

onMounted(() => {
  searchQuery.value = initialSearch
  fetchProductsPagination()

  const container = document.querySelector('.grid-container')
  if (container) {
    container.addEventListener('scroll', handleScroll)
  }
})

onBeforeUnmount(() => {
  const container = document.querySelector('.grid-container')
  if (container) {
    container.removeEventListener('scroll', handleScroll)
  }
})

watch([searchQuery, fetchProducts], () => {
  fetchProductsPagination(true)
})
</script>

<template>
  <div class="flex-container">
    <FilteringSideBar @update-filters="handleFiltersUpdate" />

    <div class="row" style="width: 500px; padding-bottom: 20px; justify-content: center">
      <div class="input-container">
        <InputText
          v-model="searchQuery"
          class="large-input"
          type="text"
          size="large"
          placeholder="Search for a product..."
        />
        <Button id="create-product-btn" @click="handleCreateProductOverlay">+</Button>
      </div>
    </div>

    <div class="row" style="margin-bottom: 10px">
      <div v-if="!hasMore && !loading" class="end-message">No more products</div>
      <div v-else>
        <ProductCatalog
          @handle-edit-product="handleEditProduct"
          @handle-delete-product="handleDeleteProduct"
          :products="products"
        />
      </div>
    </div>

    <div v-if="loading" class="loading-indicator">Loading more products...</div>

    <div class="row" v-if="!loading && products.length === 0 && searchQuery">
      <p>No products found for "{{ searchQuery }}"</p>
    </div>
  </div>
</template>

<style scoped>
.row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.large-input {
  width: 100%;
  max-width: 500px;
  font-size: 1.5rem;
}

#create-product-btn {
  font-size: 30px;
  font-weight: bold;
  padding: 5px 9px;
  cursor: pointer;
}

#create-product-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
}

.flex-container {
  background: whitesmoke;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.loading-indicator {
  text-align: center;
  font-size: 1.2rem;
  margin-top: 20px;
}

.input-container {
  display: flex;
  align-items: center;
  gap: 5px;
}
</style>
