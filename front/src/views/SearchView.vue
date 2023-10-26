<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import type { Product } from '@/types/product.types'
import { filteringDataRepository } from '@/helpers/api'
import JamCard from '@/components/JamCard.vue'
import NoDataFound from '@/components/NoDataFound.vue'

const props = defineProps<{
  searched: string
}>()

const products = ref<Product[]>([])
const page = ref<number>(1)
const pagesNumber = ref<number>(1)

onMounted(async () => {
  const { products: fetchedProducts, pages_number } = await filteringDataRepository.getAllLike(
    props.searched
  )
  products.value = fetchedProducts
  pagesNumber.value = pages_number
})

watch(
  () => props.searched,
  async () => {
    const { products: fetchedProducts, pages_number } = await filteringDataRepository.getAllLike(
      props.searched
    )
    products.value = fetchedProducts
    pagesNumber.value = pages_number
  }
)
</script>

<template>
  <div style="width: 90%" class="mx-auto">
    <div class="ma-5 pa-5" v-if="products.length != 0">
      <v-row>
        <v-col cols="4" v-for="product in products" :key="product.id">
          <JamCard :product="product" />
        </v-col>
      </v-row>
      <v-pagination v-model="page" :length="pagesNumber" rounded="circle"></v-pagination>
    </div>

    <NoDataFound v-else />
  </div>
</template>
<style>
.filtersText {
  color: gray;
}
</style>
