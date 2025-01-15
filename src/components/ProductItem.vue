<script setup lang="ts">
import Card from 'primevue/card'
import { defineProps, defineEmits } from 'vue'

interface ProductType {
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

const emit = defineEmits(['handle-delete-product', 'handle-edit-product'])

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const props = defineProps<{
  product: ProductType
}>()

const randomColor = `#${Array.from({ length: 3 })
  .map(() => {
    const value = Math.floor(Math.random() * 200)
    return value.toString(16).padStart(2, '0')
  })
  .join('')}`

function handleDeleteProduct(id: string) {
  emit('handle-delete-product', id)
}

function handleEditProduct(product: ProductType) {
  emit('handle-edit-product', product)
}
</script>

<template>
  <Card class="product-card">
    <template #header>
      <div class="header" :style="{ backgroundColor: randomColor }">
        <p class="product-name">{{ product.name }}</p>
        <div class="action-buttons">
          <div class="deleteProductButton" @click="handleDeleteProduct(product.id)">x</div>
          <div class="createProductButton" @click="handleEditProduct(product)">✏️</div>
        </div>
      </div>
    </template>
    <template #content>
      <div class="product-details">
        <p><strong>Price:</strong> ${{ product.price }}</p>
        <p><strong>Stock:</strong> {{ product.stock }}</p>
        <p><strong>Category:</strong> {{ product.category }}</p>
        <p><strong>Brand:</strong> {{ product.brand }}</p>
        <p><strong>Color:</strong> {{ product.color }}</p>
        <p><strong>Rating:</strong> {{ product.rating }} / 5</p>
        <p>
          <strong>Availability:</strong>
          <span :class="product.is_available ? 'available' : 'unavailable'">{{
            product.is_available ? 'In Stock' : 'Out of Stock'
          }}</span>
        </p>
        <p><strong>Description:</strong> {{ product.description }}</p>
      </div>
    </template>
  </Card>
</template>

<style scoped>
/* Card styling */
.product-card {
  width: 18rem;
  margin: auto;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  background: #fff;
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.15);
}

/* Header styling */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  color: #fff;
  font-size: 1.25rem;
  font-weight: bold;
  border-radius: 12px 12px 0 0;
}

.product-name {
  margin: 0;
}

/* Action buttons styling */
.action-buttons {
  display: flex;
  gap: 8px;
}

.deleteProductButton {
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  border-radius: 50%;
  background: #ff4d4d;
  color: white;
  font-size: 14px;
  width: 28px;
  height: 28px;
  cursor: pointer;
  transition:
    background 0.3s ease,
    transform 0.3s ease;
}

.deleteProductButton:hover {
  background: #ff1a1a;
  transform: scale(1.1);
}

.createProductButton {
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  border-radius: 50%;
  background: #4caf50;
  color: white;
  font-size: 14px;
  width: 28px;
  height: 28px;
  cursor: pointer;
  transition:
    background 0.3s ease,
    transform 0.3s ease;
}

.createProductButton:hover {
  background: #388e3c;
  transform: scale(1.1);
}

/* Content styling */
.product-details {
  padding: 16px;
  color: #333;
  font-size: 0.95rem;
  line-height: 1.5;
}

.product-details p {
  margin: 6px 0;
}

.product-details strong {
  color: #555;
}
</style>
