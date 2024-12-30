<template>
  <div>
    <!-- Sidebar Toggle Button -->
    <Button
      icon="pi pi-filter"
      label="Filters"
      class="p-button-rounded p-button-outlined toggle-button"
      @click="visible = !visible"
    />

    <!-- Sidebar Component -->
    <Sidebar v-model:visible="visible" position="right">
      <h3>Filter Products</h3>
      <div class="filter-section">
        <h4>Category</h4>
        <Dropdown
          v-model="selectedCategory"
          :options="categories"
          placeholder="Select a Category"
        />
      </div>
      <div class="filter-section">
        <h4 style="margin-bottom: 10px">Price Range</h4>
        <Slider style="margin-bottom: 10px" v-model="priceRange" :min="0" :max="500" :step="10" />
        <p>€{{ priceRange[0] }} - €{{ priceRange[1] }}</p>
      </div>
      <div class="filter-section">
        <h4>In Stock</h4>
        <Checkbox v-model="inStock" /> <label>Only show products in stock</label>
      </div>
      <div class="filter-actions">
        <Button label="Apply Filters" icon="pi pi-check" class="p-button-success" />
        <Button label="Reset" icon="pi pi-times" class="p-button-secondary" @click="resetFilters" />
      </div>
    </Sidebar>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import Sidebar from 'primevue/sidebar';
import Dropdown from 'primevue/dropdown';
import Slider from 'primevue/slider';
import Checkbox from 'primevue/checkbox';
import Button from 'primevue/button';

const visible = ref(false);
const categories = ref([
  { label: 'Electronics', value: 'electronics' },
  { label: 'Books', value: 'books' },
  { label: 'Clothing', value: 'clothing' },
]);
const selectedCategory = ref(null);
const priceRange = ref([0, 500]);
const inStock = ref(false);

function resetFilters() {
  selectedCategory.value = null;
  priceRange.value = [0, 500];
  inStock.value = false;
}
</script>

<style scoped>
.toggle-button {
  position: fixed;
  top: 1rem;
  right: 1rem;
  z-index: 1000;
  background: linear-gradient(to right, #6a11cb, #2575fc);
  color: white;
  font-weight: bold;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
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
</style>
