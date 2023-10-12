<script setup lang="ts">
import JamCard from '@/components/JamCard.vue'
import { ref, onMounted, watch } from 'vue'
import { productRepository } from '@/helpers/api'
import type { Product } from '@/types/product.types'
import HrComponent from '@/components/HrComponent.vue'
import FilterProductsComponent from '@/components/FilterProductsComponent.vue'
import useFilters from '@/composables/filters'
import { filteringDataRepository } from '@/helpers/api'

const products = ref<Product[]>([])
const productsFiltered = ref<Product[]>([])
const searchedName = ref<string>('')
const namesOfPoductsArray = ref<string[]>([])
const filtersState = useFilters()

onMounted(async () => {
  const { products: fetchedProducts } = await productRepository.getAllProducts()
  products.value = fetchedProducts
  useFilters().findMinMaxPrices(products.value)
  namesOfPoductsArray.value = products.value.map((val) => {
    return val.name
  })
})

// watch(products, (newValue) => {
//   productsFiltered.value = newValue
// })

watch(searchedName, (newValue) => {
  // console.log(searchedName)
  filtersState.setSearchedText(searchedName.value)
  // productsFiltered.value = filterByName(newValue)
  console.log(filtersState.state)
})

watch(filtersState.state, async (newVal) => {
  console.log('state changed', filtersState.state)
  // const { productsFiltered } = await filteringDataRepository.getProductsFiltered(filtersState.state)

  console.log(productsFiltered)
})
// const filterByName = (nameToSearch: string) => {
//   if (!nameToSearch) {
//     return products.value
//   } else {
//     return products.value.filter((product) => product.name.toLowerCase().includes(nameToSearch))
//   }
// }
const getDataFilered = async () => {
  await filteringDataRepository.getProductsFiltered(filtersState.state)
}
</script>

<template>
  <div style="width: 90%" class="mx-auto">
    <div class="ma-5 pa-5">
      <div class="d-flex justify-center">
        <div style="width: 80%">
          <v-text-field type="text" v-model="searchedName" label="Search jam"></v-text-field>
        </div>
      </div>
      <HrComponent />
      <v-row>
        <v-col cols="3">
          <FilterProductsComponent /> <v-btn @click="getDataFilered"> Filter </v-btn></v-col
        >
        <v-col cols="8">
          <v-row>
            <v-col cols="4" v-for="product in products" :key="product.id">
              <JamCard :product="product" />
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </div>
  </div>
  <!-- <p>Home Page</p>
  <RouterLink to="/login">{{ $t('login') }}</RouterLink>
  test -->
</template>
<style scoped></style>
