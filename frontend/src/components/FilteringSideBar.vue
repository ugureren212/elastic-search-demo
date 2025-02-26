<template>
  <div>
    <!-- Sidebar Toggle Button -->
    <Button icon="pi pi-filter" label="Filters" class="toggle-button" @click="visible = !visible" />

    <!-- Sidebar Component -->
    <Sidebar v-model:visible="visible" position="right">
      <h3>Filter Products</h3>
      <!-- Category Filter -->
      <div class="filter-section">
        <h4>Category</h4>
        <MultiSelect
          display="chip"
          :maxSelectedLabels="3"
          v-model="selectedCategory"
          :options="categories"
          optionLabel="label"
          placeholder="Select Categories"
        />
      </div>

      <!-- Brand Filter -->
      <div class="filter-section">
        <h4>Brand</h4>
        <MultiSelect
          display="chip"
          :maxSelectedLabels="3"
          v-model="selectedBrand"
          :options="brands"
          optionLabel="label"
          placeholder="Select Brands"
        />
      </div>

      <!-- Color Filter -->
      <div class="filter-section">
        <h4>Color</h4>
        <MultiSelect
          display="chip"
          :maxSelectedLabels="3"
          v-model="selectedColor"
          :options="colors"
          optionLabel="label"
          placeholder="Select Colors"
        />
      </div>

      <!-- Price Range Filter -->
      <div class="filter-section">
        <h4 style="margin-bottom: 10px">Price Range</h4>
        <Slider
          style="margin-bottom: 10px"
          v-model="priceRange"
          :min="0"
          :max="500"
          :step="10"
          range
        />
        <p>€{{ priceRange[0] }} - €{{ priceRange[1] }}</p>
      </div>

      <!-- Rating Filter -->
      <div class="filter-section">
        <h4>Rating</h4>
        <MultiSelect
          display="chip"
          :maxSelectedLabels="3"
          v-model="selectedRating"
          :options="ratings"
          optionLabel="label"
          placeholder="Select Ratings"
        />
      </div>

      <!-- Availability Filter -->
      <div class="filter-section">
        <Checkbox v-model="inStock" binary />
        <label> In stock</label>
        <Checkbox style="margin-left: 10px" v-model="notInStock" binary />
        <label> Out of stock </label>
      </div>

      <!-- Action Buttons -->
      <div class="filter-actions">
        <!--<Button label="Apply Filters" icon="pi pi-check" class="p-button-success" />-->
        <Button label="Reset" icon="pi pi-times" class="p-button-secondary" @click="resetFilters" />
      </div>
    </Sidebar>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import Sidebar from 'primevue/sidebar'
import MultiSelect from 'primevue/multiselect'
import Slider from 'primevue/slider'
import Checkbox from 'primevue/checkbox'
import Button from 'primevue/button'

const visible = ref(false)

const categories = ref([
  { label: 'Electronics', value: 'Electronics' },
  { label: 'Fashion', value: 'Fashion' },
  { label: 'Home', value: 'Home' },
  { label: 'Books', value: 'Books' },
  { label: 'Sports', value: 'Sports' },
  { label: 'Toys', value: 'Toys' },
])

const brands = ref([
  { label: 'BrandA', value: 'BrandA' },
  { label: 'BrandB', value: 'BrandB' },
  { label: 'BrandC', value: 'BrandC' },
  { label: 'BrandD', value: 'BrandD' },
  { label: 'BrandE', value: 'BrandE' },
])

const colors = ref([
  { label: 'Red', value: 'Red' },
  { label: 'Blue', value: 'Blue' },
  { label: 'Green', value: 'Green' },
  { label: 'Black', value: 'Black' },
  { label: 'White', value: 'White' },
  { label: 'Yellow', value: 'Yellow' },
])

const ratings = ref([
  { label: '1 Star', value: 1 },
  { label: '2 Stars', value: 2 },
  { label: '3 Stars', value: 3 },
  { label: '4 Stars', value: 4 },
  { label: '5 Stars', value: 5 },
])

const selectedCategory = ref([])
const selectedBrand = ref([])
const selectedColor = ref([])
const selectedRating = ref([])
const priceRange = ref([0, 500])
const inStock = ref(true)
const notInStock = ref(true)

const emit = defineEmits(['update-filters'])

function resetFilters() {
  selectedCategory.value = []
  selectedBrand.value = []
  selectedColor.value = []
  selectedRating.value = []
  priceRange.value = [0, 500]
  inStock.value = false
  notInStock.value = false
}

watch(
  [selectedCategory, selectedBrand, selectedColor, selectedRating, priceRange, inStock, notInStock],
  ([newCategory, newBrand, newColor, newRating, newPriceRange, newInStock, newNotInStock]) => {
    emit('update-filters', {
      selectedCategory: newCategory,
      selectedBrand: newBrand,
      selectedColor: newColor,
      selectedRating: newRating,
      priceRange: newPriceRange,
      inStock: newInStock,
      notInStock: newNotInStock,
    })
  },
  { deep: true },
)
</script>

<style scoped>
.toggle-button {
  position: fixed;
  top: 1rem;
  right: 1rem;
  z-index: 1000;
}

.toggle-button:hover {
  transform: scale(1.1);
  transition: transform 0.2s;
}

.filter-section {
  margin-bottom: 1.5rem;
}

.filter-actions {
  display: flex;
  justify-content: space-between;
  gap: 10px;
}

p-multiselect-header {
  display: none;
}
</style>