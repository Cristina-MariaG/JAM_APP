<script setup lang="ts">
import useFilters from '@/composables/filters'
import { ref, onMounted, watch } from 'vue'

const orderedType = ref(['Ascending', 'Descending'])
const selectedOrder = ref('Select')
const storeFilters = useFilters()

watch(selectedOrder, (val) => {
  storeFilters.setOrdonateByPrice(val)
})
</script>

<template>
  <div>
    <v-combobox
      v-model="selectedOrder"
      :items="orderedType"
      label="Order by price"
      variant="solo-filled"
    ></v-combobox>
  </div>
</template>
