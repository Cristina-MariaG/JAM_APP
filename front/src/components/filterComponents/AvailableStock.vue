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
  <div class="mb-5">
    <p class="filtersText">{{ $t('filters.availableStock') }}</p>
    <v-switch
      v-model="availableStock"
      hide-details
      inset
      :label="$t('filters.onlyAvailableStock')"
    ></v-switch>
  </div>
</template>
