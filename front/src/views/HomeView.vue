<script setup lang="ts">
import JamCard from '@/components/JamCard.vue'
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import { productRepository } from '@/helpers/api'
import type { Product, ProductsData } from '@/types/product.types'

const products = ref<ProductsData>()

onMounted(async () => {
  products.value = await productRepository.getAllProducts()
})
</script>

<template>
  <div class="ma-5 pa-5">
    <v-row>
      <v-col v-for="product in products?.products" :key="product.id" cols="12" sm="6" md="4" lg="3">
        <JamCard :product="product" />
      </v-col>
    </v-row>
  </div>
  <p>Home Page</p>
  <RouterLink to="/login">{{ $t('login') }}</RouterLink>
  test
</template>
<style scoped>
.product-ingredients {
  margin-top: 10px;
}
</style>
