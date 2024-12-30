<script setup lang="ts">
import ProductsViewLayout from '@/layout/ProductsViewLayout.vue'
import { ref } from 'vue'
import CreateProductCard from '@/components/CreateProductCard.vue'

const createProductOverlay = ref(false)

function handleCreateProduct(closeOverlay: boolean) {
  createProductOverlay.value = closeOverlay
}

</script>
<template>
  <div>
    <div id="create-product-overlay" v-if="createProductOverlay">
      <CreateProductCard @handle-create-product="handleCreateProduct"/>
    </div>
    <div v-else>
      <ProductsViewLayout @handle-create-product="handleCreateProduct" />
    </div>
  </div>
</template>

<style scoped>
#create-product-overlay {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1000;
}
</style>
