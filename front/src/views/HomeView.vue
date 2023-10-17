<script setup lang="ts">
import JamCard from '@/components/JamCard.vue'
import { ref, onBeforeMount, watch } from 'vue'
import { productRepository } from '@/helpers/api'
import type { Product } from '@/types/product.types'
import FilterProductsComponent from '@/components/FilterProductsComponent.vue'
import useFilters from '@/composables/filters'
import { filteringDataRepository } from '@/helpers/api'
import NoDataDisponible from '@/components/NoDataDisponible.vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const products = ref<Product[]>([])
const filtersState = useFilters()
const searchVal = ref('')
const page = ref<number>(1)
const pagesNumber = ref<number>(1)

onBeforeMount(async () => {
  const { products: fetchedProducts, pages_number } = await productRepository.getAllProducts()

  products.value = fetchedProducts
  pagesNumber.value = pages_number
})

watch(searchVal, (val) => {
  filtersState.setSearchedText(val)
})

watch(filtersState.state, async (newVal) => {
  getDataFilered()
})

const getDataFilered = async () => {
  const { products: fetchedProducts, pages_number } =
    await filteringDataRepository.getProductsFiltered(filtersState.state)
  products.value = fetchedProducts
  pagesNumber.value = pages_number
}
const trad = ref(t('home.home'))
</script>

<template>
  <div style="width: 90%" class="mx-auto">
    <div class="ma-5 pa-5">
      <v-row>
        <v-col cols="3"> <FilterProductsComponent /></v-col>
        {{ trad }}
        <v-col cols="8">
          <div v-if="products.length != 0">
            <v-row>
              <v-col cols="4" v-for="product in products" :key="product.id">
                <JamCard :product="product" />
              </v-col>
            </v-row>
            <v-pagination v-model="page" :length="pagesNumber" rounded="circle"></v-pagination>
          </div>
          <NoDataDisponible v-else />
        </v-col>
      </v-row>
    </div>
  </div>
</template>
<style scoped></style>
