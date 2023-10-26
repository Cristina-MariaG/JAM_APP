<script setup lang="ts">
import { onBeforeMount, ref, watch } from 'vue'
import useFilters from '@/composables/filters'
import { productRepository } from '@/helpers/api'

const storeFilters = useFilters()

onBeforeMount(async () => {
  const { price__min: min, price__max: max } = await productRepository.getMinMAx()
  sliderMin.value = min
  sliderMax.value = max
})

const sliderMin = ref<number>(0)
const sliderMax = ref<number>(0)

const range = ref([sliderMin.value, sliderMax.value])

watch([sliderMin, sliderMax], ([newSliderMin, newSliderMax]) => {
  range.value = [newSliderMin, newSliderMax]
})
watch(range, (newVal, oldVal) => {
  if (oldVal[0] == 0 && oldVal[0] == 0) {
    return
  }
  storeFilters.setMinPriceUser(newVal[0])
  storeFilters.setMaxPriceUser(newVal[1])
})
</script>

<template>
  <div>
    <p class="filtersText text-center">{{ $t('filters.priceBetween') }}</p>
    <v-range-slider
      v-model="range"
      step="1"
      thumb-label="always"
      :min="sliderMin"
      :max="sliderMax"
    ></v-range-slider>
  </div>
</template>
