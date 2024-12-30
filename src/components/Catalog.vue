<script setup lang="ts">
import { defineEmits, defineProps } from 'vue'
import Product from './Product.vue';

const emit = defineEmits(['handle-delete-product','handle-edit-product']);

defineProps({
  products: {
    type: Array,
    required: true,
  },
});

function handleDeleteProduct(id: number){
  emit('handle-delete-product', id);
}
function handleEditProduct(product: any){
  emit('handle-edit-product', product);
}
</script>

<template>
  <div class="grid-container">
    <div
      v-for="(product, index) in products"
      :key="index"
      class="grid-item"
    >
      <Product @handle-edit-product="handleEditProduct" @handle-delete-product="handleDeleteProduct" :product="product" />
    </div>
  </div>
</template>

<style scoped>
.grid-container {
  display: grid;
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

.end-message {
  text-align: center;
  font-size: 1.2rem;
  margin-top: 20px;
  color: gray;
}
</style>
