<script setup lang="ts">
import { ref, watch } from 'vue'
import useFilters from '@/composables/filters'

const storeFilters = useFilters()

// const minPrice = ref(storeFilters.state.minPrice)
// const maxPrice = ref(storeFilters.state.maxPrice)

const minPrice = ref(0)
const maxPrice = ref(100)
const range = ref([storeFilters.state.minPrice, storeFilters.state.maxPrice])

const sliderMin = ref<number>(0)
const sliderMax = ref<number>(0)

watch(sliderMin, (newVal) => {
  storeFilters.setMinPriceUser(newVal)
})
watch(sliderMax, (newVal) => {
  storeFilters.setMaxPriceUser(newVal)
})
</script>

<template>
  <div>
    <v-range-slider
      v-model="range"
      :max="maxPrice"
      :min="minPrice"
      :step="1"
      hide-details
      class="align-center"
    >
      <template v-slot:prepend>
        <v-text-field
          v-model="range[0]"
          hide-details
          single-line
          type="number"
          variant="outlined"
          density="compact"
          style="width: 70px"
        ></v-text-field>
      </template>
      <template v-slot:append>
        <v-text-field
          v-model="range[1]"
          hide-details
          single-line
          type="number"
          variant="outlined"
          style="width: 70px"
          density="compact"
        ></v-text-field>
      </template>
    </v-range-slider>

    <!-- <v-slider
      v-model="sliderMin"
      class="align-center"
      :label="`min`"
      thumb-label
      step="1"
      :max="maxPrice"
      :min="minPrice"
      hide-details
    >
    </v-slider>
  </div>
  <div>
    <v-slider
      v-model="sliderMax"
      class="align-center"
      :label="`max `"
      thumb-label
      :max="maxPrice"
      :min="minPrice"
      hide-details
    >
    </v-slider> -->
  </div>
</template>
