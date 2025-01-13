<script setup lang="ts">
import { defineEmits, defineProps, ref } from 'vue';
import Product from './Product.vue';

const emit = defineEmits(['handle-delete-product', 'handle-edit-product', 'handle-loading-product']);

defineProps({
  products: {
    type: Array,
    required: true,
  },
});

const isLoading = ref(false);

function handleDeleteProduct(id: number) {
  emit('handle-delete-product', id);
}
function handleEditProduct(product: any) {
  emit('handle-edit-product', product);
}

function handleScroll(event: Event) {
  const container = event.target as HTMLElement;
  const scrollTop = container.scrollTop;
  const scrollHeight = container.scrollHeight;
  const clientHeight = container.clientHeight;

  if (scrollTop + clientHeight >= scrollHeight - 100 && !isLoading.value) {
    isLoading.value = true;
    emit('handle-loading-product', true);

    setTimeout(() => {
      isLoading.value = false;
      emit('handle-loading-product', false);
    }, 2000);
  }
}
</script>

<template>
  <div class="grid-container" @scroll="handleScroll">
    <div
      v-for="(product, index) in products"
      :key="index"
      class="grid-item"
    >
      <Product
        @handle-edit-product="handleEditProduct"
        @handle-delete-product="handleDeleteProduct"
        :product="product"
      />
    </div>
    <div v-if="isLoading" class="loading-message">Loading more products...</div>
  </div>
</template>

<style scoped>
.grid-container {
  display: grid;
  background: white;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  justify-content: center;
  align-items: start;
  width: 100%;
  padding: 20px;
  max-height: 55vh;
  overflow-y: auto;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}

.grid-item {
  display: flex;
  justify-content: center;
  align-items: center;
}

.loading-message {
  text-align: center;
  font-size: 1.2rem;
  color: gray;
  grid-column: span 4;
}
</style>
