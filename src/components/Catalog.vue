<script setup lang="ts">
import Product from './Product.vue'
const products = [
  { id: 1, name: 'Apple', price: 1.2, category: 'Fruits' },
  { id: 2, name: 'Milk', price: 0.99, category: 'Dairy' },
  { id: 3, name: 'Bread', price: 2.5, category: 'Bakery' },
  { id: 4, name: 'Carrot', price: 1.0, category: 'Vegetables' },
  { id: 5, name: 'Eggs', price: 3.0, category: 'Dairy' },
  { id: 6, name: 'Banana', price: 0.8, category: 'Fruits' },
  { id: 7, name: 'Cheese', price: 4.5, category: 'Dairy' },
  { id: 8, name: 'Chicken Breast', price: 7.0, category: 'Meat' },
  { id: 9, name: 'Orange', price: 1.3, category: 'Fruits' },
  { id: 10, name: 'Yogurt', price: 0.89, category: 'Dairy' },
  { id: 11, name: 'Tomato', price: 0.99, category: 'Vegetables' },
  { id: 12, name: 'Cucumber', price: 1.2, category: 'Vegetables' },
  { id: 13, name: 'Pasta', price: 1.5, category: 'Pantry' },
  { id: 14, name: 'Rice', price: 2.0, category: 'Pantry' },
  { id: 15, name: 'Potato', price: 0.79, category: 'Vegetables' },
  { id: 16, name: 'Salmon', price: 10.5, category: 'Seafood' },
  { id: 17, name: 'Shrimp', price: 8.5, category: 'Seafood' },
  { id: 18, name: 'Lettuce', price: 1.0, category: 'Vegetables' },
  { id: 19, name: 'Butter', price: 2.8, category: 'Dairy' },
  { id: 20, name: 'Strawberries', price: 3.5, category: 'Fruits' },
  { id: 21, name: 'Blueberries', price: 4.0, category: 'Fruits' },
  { id: 22, name: 'Beef Steak', price: 12.0, category: 'Meat' },
  { id: 23, name: 'Pork Chops', price: 9.5, category: 'Meat' },
  { id: 24, name: 'Zucchini', price: 1.1, category: 'Vegetables' },
  { id: 25, name: 'Onion', price: 0.79, category: 'Vegetables' },
  { id: 26, name: 'Garlic', price: 1.5, category: 'Vegetables' },
  { id: 27, name: 'Peppers', price: 1.8, category: 'Vegetables' },
  { id: 28, name: 'Honey', price: 5.0, category: 'Pantry' },
  { id: 29, name: 'Jam', price: 3.0, category: 'Pantry' },
  { id: 30, name: 'Pineapple', price: 2.5, category: 'Fruits' },
  { id: 31, name: 'Mango', price: 1.7, category: 'Fruits' },
  { id: 32, name: 'Avocado', price: 2.0, category: 'Fruits' },
  { id: 33, name: 'Spinach', price: 1.5, category: 'Vegetables' },
  { id: 34, name: 'Kale', price: 1.8, category: 'Vegetables' },
  { id: 35, name: 'Grapes', price: 2.9, category: 'Fruits' },
  { id: 36, name: 'Cereal', price: 3.5, category: 'Pantry' },
  { id: 37, name: 'Chips', price: 2.2, category: 'Snacks' },
  { id: 38, name: 'Cookies', price: 3.0, category: 'Snacks' },
  { id: 39, name: 'Ice Cream', price: 4.5, category: 'Frozen' },
  { id: 40, name: 'Frozen Pizza', price: 5.0, category: 'Frozen' },
  { id: 41, name: 'Juice', price: 2.5, category: 'Beverages' },
  { id: 42, name: 'Coffee', price: 7.0, category: 'Beverages' },
  { id: 43, name: 'Tea', price: 3.0, category: 'Beverages' },
  { id: 44, name: 'Canned Beans', price: 1.2, category: 'Pantry' },
  { id: 45, name: 'Canned Tuna', price: 1.5, category: 'Pantry' },
  { id: 46, name: 'Apple Juice', price: 2.3, category: 'Beverages' },
  { id: 47, name: 'Chocolate', price: 2.8, category: 'Snacks' },
  { id: 48, name: 'Almonds', price: 6.0, category: 'Snacks' },
  { id: 49, name: 'Cashews', price: 7.0, category: 'Snacks' },
  { id: 50, name: 'Broccoli', price: 1.5, category: 'Vegetables' }
];

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
/* Grid container for evenly spaced layout */
.grid-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 5 columns */
  grid-template-rows: repeat(2, 1fr); /* 2 rows */
  gap: 20px; /* Spacing between items */
  justify-content: center; /* Center items horizontally */
  align-items: center; /* Center items vertically */
  width: 100%; /* Full width of the container */
  padding: 20px; /* Optional: padding around the grid */
  max-height: 400px; /* Limit the visible height to fit 8 items */
  overflow-y: auto;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
  border-radius: 10px;
}

/* Grid item styling */
.grid-item {
  display: flex;
  justify-content: center; /* Center content inside the grid item */
  align-items: center; /* Center content inside the grid item */
}
</style>
