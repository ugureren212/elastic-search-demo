<script setup lang="ts">
import Card from 'primevue/card';
import { defineProps, defineEmits } from 'vue';

const emit = defineEmits(['delete-item']);

defineProps({
  product: Object,
});

// Generate a random color that avoids white or very light shades
const randomColor = `#${Array.from({ length: 3 })
  .map(() => {
    const value = Math.floor(Math.random() * 200);
    return value.toString(16).padStart(2, '0');
  })
  .join('')}`;

function handleDelete(id: number){
  emit('handle-delete', id);
}
</script>

<template>
  <Card style="width: 15rem; overflow: hidden">
    <template #header>
      <div class="header" :style="{ backgroundColor: randomColor }">
        <p>{{ product.name }}</p>
        <div class="deleteProductButton" @click="handleDelete(product.id)">x</div>
      </div>
    </template>
    <template #content>
      <p>Price: ${{ product.price }}</p>
      <p>Stock: {{ product.stock }}</p>
      <p>{{ product.description }}</p>
    </template>
  </Card>
</template>

<style scoped>
/* Header styles */
.header {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px; /* Space between icon and name */
  padding: 15px;
  font-size: 1.5rem; /* Larger font size */
  color: #fff; /* White text for better contrast */
  font-weight: bold;
  text-align: center;
  border-radius: 5px 5px 0 0; /* Rounded corners on the top */
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
  font-size: 14px; /* Adjust font size to fit the smaller button */
  width: 20px; /* Fixed square dimensions */
  height: 20px;
  line-height: 0; /* Remove line-height to prevent vertical misalignment */
  cursor: pointer;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  transition: transform 0.2s ease;
}

.deleteProductButton:hover {
  transform: scale(1.1);
}

</style>
