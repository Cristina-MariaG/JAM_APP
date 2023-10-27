<script setup lang="ts">
import JamCard from '@/components/JamCard.vue'
import NoDataFound from '@/components/NoDataFound.vue'
import FilterProductsComponent from '@/components/FilterProductsComponent.vue'

import { ref, onBeforeMount, watch } from 'vue'
import { filteringDataRepository } from '@/helpers/api'
import { productRepository } from '@/helpers/api'
import type { Product } from '@/types/product.types'
import useFilters from '@/composables/filters'

const products = ref<Product[]>([])
const filtersState = useFilters()
const searchVal = ref('')
const page = ref<number>(1)
const pagesNumber = ref<number>(1)

onBeforeMount(async () => {
  getData()
})

const getData = async () => {
  const { products: fetchedProducts, pages_number } = await productRepository.getAllProducts()

  products.value = fetchedProducts
  pagesNumber.value = pages_number
  console.log(pagesNumber)
}

watch(page, async (val) => {
  getDataFilered(val - 1)
})

watch(searchVal, (val) => {
  filtersState.setSearchedText(val)
})

watch(filtersState.state, async () => {
  getDataFilered(page.value - 1)
})

const getDataFilered = async (pageVal: number) => {
  const { products: fetchedProducts, pages_number } =
    await filteringDataRepository.getProductsFiltered(filtersState.state, pageVal)
  products.value = fetchedProducts
  pagesNumber.value = pages_number
}
</script>

<template>
  <div style="width: 90%" class="mx-auto">
    <div class="ma-5 pa-5">
      <v-row>
        <v-col cols="3"> <FilterProductsComponent /></v-col>
        <v-col cols="8">
          <div v-if="products.length != 0">
            <v-row>
              <v-col cols="4" v-for="product in products" :key="product.id">
                <JamCard :product="product" />
              </v-col>
            </v-row>
            <v-pagination v-model="page" :length="pagesNumber" rounded="circle"></v-pagination>
          </div>
          <NoDataFound v-else />
        </v-col>
      </v-row>
    </div>
  </div>
</template>
<style scoped></style>
