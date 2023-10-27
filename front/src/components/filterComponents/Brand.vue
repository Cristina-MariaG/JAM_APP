<script setup lang="ts">
import useFilters from '@/composables/filters'
import { brandRepository } from '@/helpers/api'
import type { Brand } from '@/types/product.types';
import { ref, onMounted, watch } from 'vue'

const apiBrandList = ref<Brand[]>([])
const selectedBrands = ref([])
const storeFilters = useFilters()

watch(selectedBrands, (newVal) => {
  storeFilters.setbrandList(newVal)
})

onMounted(() => {
  getBrand()
})

const getBrand = async () => {
  const { brand_list: brandList } = await brandRepository.getBrands()
  apiBrandList.value = brandList
}
</script>

<template>
  <div>
    <p class="filtersText">{{ $t('filters.brand') }}</p>
    <div>
      <div v-for="brand in apiBrandList" :key="brand.id" class="d-flex">
        <v-checkbox v-model="selectedBrands" :label="brand.brand" :value="brand.id"></v-checkbox>
      </div>
    </div>
  </div>
</template>
<style lang="scss">
.v-input--density-default {
  --v-input-control-height: 0px;
  --v-input-padding-top: 0px;
}
.v-selection-control.v-selection-control--density-default {
  --v-selection-control-size: 25px;
}
.v-input__details {
  min-height: auto;
  padding: 0;
}

.separator {
  width: 90%;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
}
.filtersText {
  margin-bottom: 1em;
}
</style>
