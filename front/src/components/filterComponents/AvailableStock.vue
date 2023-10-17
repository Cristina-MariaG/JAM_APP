<script setup lang="ts">
import useFilters from '@/composables/filters'
import { ref, watch } from 'vue'

const availableStock = ref(false)
const storeFilters = useFilters()

watch(availableStock, (newVal) => {
  storeFilters.setAvailableStock(newVal)
})
</script>

<template>
  <div>
    <p class="filtersText">{{ $t('filters.stockDisponible') }}</p>
    <v-switch
      v-model="availableStock"
      hide-details
      inset
      :label="`Only available stock`"
    ></v-switch>
  </div>
</template>
<style lang="scss" scoped></style>
