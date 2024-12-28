<script setup lang="ts">
import { defineProps} from 'vue';
import Product from './Product.vue';

defineProps({
  products: {
    type: Array,
    required: true,
  },
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
