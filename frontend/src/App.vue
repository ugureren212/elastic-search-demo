<script setup lang="ts">
import ProductsViewLayout from './layout/ProductsViewLayout.vue'
import { ref } from 'vue'
import CreateProductCard from './components/CreateProductCard.vue'

const createProductOverlay = ref(false)
const fetchProducts = ref(false)

const editProduct = ref(<Record<string, any> | undefined | null>undefined)

function handleFetchProducts(fetchProductsBool: boolean) {
  console.log('app level: ', fetchProductsBool)
  fetchProducts.value = !fetchProductsBool
}

function handleCloseCreateProductOverlay(closeOverlay: boolean) {
  if (closeOverlay) {
    editProduct.value = undefined
  }
  createProductOverlay.value = !closeOverlay
}

function handleEditProduct(closeOverlay: boolean, product: any) {
  createProductOverlay.value = closeOverlay
  editProduct.value = product
}
</script>

<template>
  <div>
    <div id="create-product-overlay" v-if="createProductOverlay">
      <CreateProductCard
        :edit-product="editProduct"
        @handle-close-create-product-overlay="handleCloseCreateProductOverlay"
        @handle-fetch-products="handleFetchProducts"
      />
    </div>
    <div v-else>
      <ProductsViewLayout
        :fetchProducts="fetchProducts"
        @handle-edit-product="handleEditProduct"
        @handle-close-create-product-overlay="handleCloseCreateProductOverlay"
      />
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