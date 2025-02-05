<script setup lang="ts">
import { defineEmits, defineProps, ref, onMounted } from 'vue'
import Card from 'primevue/card'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'
import Dropdown from 'primevue/dropdown'
import axios from 'axios'

const cardID = ref<number | null>(null)
const cardName = ref('')
const cardPrice = ref<number | null>(null)
const cardStock = ref<number | null>(null)
const cardDescription = ref('')
const cardCategory = ref<string | null>(null)
const cardBrand = ref<string | null>(null)
const cardColor = ref<string | null>(null)
const cardRating = ref<number | null>(null)
const cardAvailability = ref<boolean | null>(null)

const categories = ['Electronics', 'Fashion', 'Home', 'Books', 'Sports', 'Toys']
const brands = ['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE']
const colors = ['Red', 'Blue', 'Green', 'Black', 'White', 'Yellow']
const ratings = [1, 2, 3, 4, 5]
const availabilityOptions = [true, false]

const emit = defineEmits([
  'handle-remove-product',
  'handle-create-product-overlay',
  'handle-edit-product',
])

const { editProduct } = defineProps<{
  editProduct?: {
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
}>()

function handleRandomValueGenerator() {
  cardID.value = Math.floor(Date.now() + Math.random() * 1000)
  cardName.value = `${Math.random().toString(36).substring(2, 7)}`
  cardPrice.value = parseFloat((Math.random() * 1000).toFixed(2))
  cardStock.value = Math.floor(Math.random() * 100)
  cardDescription.value = ` ${Math.random().toString(36).substring(2, 15)}`
  const categories = ['Electronics', 'Fashion', 'Home', 'Books', 'Sports']
  cardCategory.value = categories[Math.floor(Math.random() * categories.length)]
  const brands = ['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE']
  cardBrand.value = brands[Math.floor(Math.random() * brands.length)]
  const colors = ['Red', 'Blue', 'Green', 'Yellow']
  cardColor.value = colors[Math.floor(Math.random() * colors.length)]
  cardRating.value = Math.floor(Math.random() * 5) + 1
  cardAvailability.value = Math.random() > 0.5
}

function handleCloseCreateProductOverlay() {
  cardName.value = ''
  cardPrice.value = null
  cardStock.value = null
  cardDescription.value = ''
  cardCategory.value = null
  cardBrand.value = null
  cardColor.value = null
  cardRating.value = null
  cardAvailability.value = null
  emit('handle-create-product-overlay', false)
}

const handleSubmit = async () => {
  if (
    !cardName.value ||
    !cardPrice.value ||
    !cardStock.value ||
    !cardDescription.value ||
    !cardCategory.value ||
    !cardBrand.value ||
    !cardColor.value ||
    cardRating.value === null ||
    cardAvailability.value === null
  ) {
    alert('Please fill out all fields')
    return
  }

  emit('handle-create-product-overlay', false)

  const product = {
    id: cardID.value,
    name: cardName.value,
    price: cardPrice.value,
    stock: cardStock.value,
    description: cardDescription.value,
    category: cardCategory.value,
    brand: cardBrand.value,
    color: cardColor.value,
    rating: cardRating.value,
    is_available: cardAvailability.value,
  }

  try {
    await axios.post('http://127.0.0.1:9200/products/_doc?refresh=wait_for', product)
    console.log('newProduct: ', product)
    alert('Product successfully added!')
    handleCloseCreateProductOverlay()
  } catch (error) {
    console.error('Error adding product:', error)
    alert('Failed to add product. Please try again.')
  }
}

onMounted(() => {
  if (editProduct) {
    cardName.value = editProduct.name
    cardPrice.value = editProduct.price
    cardStock.value = editProduct.stock
    cardDescription.value = editProduct.description
    cardCategory.value = editProduct.category || null
    cardBrand.value = editProduct.brand
    cardColor.value = editProduct.color
    cardRating.value = editProduct.rating
    cardAvailability.value = editProduct.is_available
  }
})
</script>

<template>
  <Card class="product-card">
    <template #header>
      <div class="flex-container card-header">
        <div class="flex-row">
          <p class="label" style="color: white">Name</p>
          <InputText type="text" v-model="cardName" />
        </div>
      </div>
    </template>
    <template #content>
      <div class="flex-container">
        <div class="flex-row">
          <p class="label">Price</p>
          <InputText type="number" v-model="cardPrice" />
        </div>
        <div class="flex-row">
          <p class="label">Stock</p>
          <InputText type="number" v-model="cardStock" />
        </div>
        <div class="flex-row">
          <p class="label">Description</p>
          <InputText type="text" v-model="cardDescription" />
        </div>
        <div class="flex-row">
          <p class="label">Category</p>
          <Dropdown :options="categories" v-model="cardCategory" placeholder="Select a category" />
        </div>
        <div class="flex-row">
          <p class="label">Brand</p>
          <Dropdown :options="brands" v-model="cardBrand" placeholder="Select a brand" />
        </div>
        <div class="flex-row">
          <p class="label">Color</p>
          <Dropdown :options="colors" v-model="cardColor" placeholder="Select a color" />
        </div>
        <div class="flex-row">
          <p class="label">Rating</p>
          <Dropdown :options="ratings" v-model="cardRating" placeholder="Select a rating" />
        </div>
        <div class="flex-row">
          <p class="label">Availability</p>
          <Dropdown
            :options="availabilityOptions"
            v-model="cardAvailability"
            placeholder="Select availability"
          />
        </div>
      </div>
      <div style="display: flex; gap: 10px; justify-content: flex-end">
        <Button label="Random" @click="handleRandomValueGenerator" />
        <Button label="Submit" @click="handleSubmit" />
        <div class="close-create-product-overlay" @click="handleCloseCreateProductOverlay">x</div>
      </div>
    </template>
  </Card>
  <br />
</template>

<style scoped>
/* Updated styles for 100% width input fields */
.product-card {
  width: 30rem;
  height: auto;
  overflow: hidden;
  border: 1px solid #e0e0e0;
  background: #fff;
  margin: auto;
  border: 2px solid grey;
}

.card-header {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px;
  background: linear-gradient(90deg, #ff6b6b, #f94c4c);
  color: #fff;
  font-size: 1.25rem;
  font-weight: bold;
  text-align: center;
  border-radius: 10px 10px 0 0;
  text-transform: uppercase;
}

.flex-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  padding: 15px;
}

.flex-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.label {
  flex: 1;
  font-weight: bold;
  font-size: 1rem;
  text-align: left;
  color: #333;
}

input,
.p-dropdown,
.p-checkbox {
  flex: 2;
  width: 100%; /* Set input field width to 100% */
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
  transition: border-color 0.2s;
}

input:focus,
.p-dropdown:focus {
  border-color: #4caf50;
  outline: none;
}

.close-create-product-overlay {
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid black;
  border-radius: 5px;
  background: darkred;
  color: white;
  font-weight: bold;
  font-size: 14px; /* Adjust font size to fit the smaller button */
  width: 40px; /* Fixed square dimensions */
  height: 40px;
  line-height: 0; /* Remove line-height to prevent vertical misalignment */
  cursor: pointer;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  transition: transform 0.2s ease;
}

.close-create-product-overlay:hover {
  transform: scale(1.1);
}
</style>
