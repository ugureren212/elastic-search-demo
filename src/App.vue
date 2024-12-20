<script setup lang="ts">
import Catalog from '@/components/Catalog.vue'
import InputText from 'primevue/inputtext'
import { ref } from 'vue'

const value = ref(null)
</script>

<template>
  <div class="flex-container">
    <div class="row">
      <div style="overflow: hidden; max-width: 500px;">
        {{ value }}
      </div>
      <InputText v-model="value" class="large-input" type="text" size="large" placeholder="Large" />
    </div>
    <div class="row" style="margin-top: 20px">
      <Catalog />
    </div>
  </div>
</template>


<style scoped>
/* Full-page container */
.flex-container {
  display: flex;
  flex-direction: column; /* Arrange items in rows (vertical) */
  justify-content: center; /* Center vertically */
  align-items: center; /* Center horizontally */
  height: 100vh; /* Full viewport height */
}

.large-input {
  width: 100%; /* Full-width input */
  min-width: 500px; /* Optional: Set a max width */
  max-width: 500px; /* Optional: Set a max width */
  font-size: 1.5rem; /* Larger font size */
}

</style>
