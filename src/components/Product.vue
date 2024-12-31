<script setup lang="ts">
import Card from 'primevue/card';
import { defineProps, defineEmits } from 'vue';

const emit = defineEmits(['handle-delete-product', 'handle-edit-product']);

defineProps({
  product: Object,
});

const randomColor = `#${Array.from({ length: 3 })
  .map(() => {
    const value = Math.floor(Math.random() * 200);
    return value.toString(16).padStart(2, '0');
  })
  .join('')}`;

function handleDeleteProduct(id: number) {
  emit('handle-delete-product', id);
}

function handleEditProduct(product: any) {
  emit('handle-edit-product', product);
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
        <p><strong>ID:</strong> {{ product.id }}</p>
        <p><strong>Price:</strong> ${{ product.price }}</p>
        <p><strong>Stock:</strong> {{ product.stock }}</p>
        <p><strong>Description:</strong> {{ product.description }}</p>
      </div>
    </template>
  </Card>
</template>

<style scoped>
/* Card styling */
.product-card {
  width: 15rem;
  margin: auto;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  background: #fdfdfd;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.product-card:hover {
  transform: scale(1.02);
  box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
}

/* Header styling */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 15px;
  color: #fff;
  font-size: 1.25rem;
  font-weight: bold;
  border-radius: 10px 10px 0 0;
}

.product-name {
  margin: 0;
}

/* Action buttons styling */
.action-buttons {
  display: flex;
  gap: 5px;
}

.deleteProductButton {
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid black;
  border-radius: 5px;
  background: darkred;
  color: white;
  font-weight: bold;
  font-size: 12px;
  width: 24px;
  height: 24px;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.deleteProductButton:hover {
  transform: scale(1.2);
}

.createProductButton {
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid black;
  border-radius: 5px;
  background: darkblue;
  color: white;
  font-weight: bold;
  font-size: 12px;
  width: 24px;
  height: 24px;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.createProductButton:hover {
  transform: scale(1.2);
}

/* Content styling */
.product-details {
  padding: 10px 15px;
  color: #333;
  font-size: 0.95rem;
  line-height: 1.4;
}

.product-details p {
  margin: 5px 0;
}

.product-details strong {
  color: #555;
}
</style>
