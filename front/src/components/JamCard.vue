<script setup lang="ts">
import type { Product } from '@/types/product.types'
import { ref, defineProps } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'

const cartStore = useCartStore()
const router = useRouter()

const getImage = (image: string) => {
  return `/uploads/${image}`
}
const { product } = defineProps<{
  product: Product
}>()

const alreadyInCart = ref(cartStore.productIsAlreadyInTheCart(product.id))

const selectedQuantity = ref(cartStore.quantitySelected(product.id))

const addToCart = () => {
  const productToAdd = {
    id: product.id,
    name: product.name,
    description: product.description,
    image: product.image,
    price: product.price,
    selectedQuantity: selectedQuantity.value
  }
  cartStore.addToCart(productToAdd)
}

const redirectToProductDetails = () => {
  router.push(`/product-details/${product.id}`)
}
</script>

<template>
  <v-card class="pa-3 mx-auto">
    <v-img :src="getImage(product.image)" aspect-ratio="1" cover></v-img>

    <v-card-title class="ms-5"> {{ product.name }} </v-card-title>

    <v-card-title class="ms-5">Price:  {{ product.price }} €</v-card-title>
    <v-card-actions>
      <div class="d-flex flex-wrap">
        <v-btn style="width: 50%" v-if="alreadyInCart" @click="addToCart">{{
          $t('home.modify')
        }}</v-btn>
        <v-btn style="width: 50%" v-else @click="addToCart">{{ $t('home.add') }}</v-btn>
        <div style="width: 50%">
          <v-text-field
            style="width: 70px"
            v-model="selectedQuantity"
            type="number"
            density="compact"
            hide-details
            variant="outlined"
          ></v-text-field>
        </div>
        <v-btn
          style="width: 80%"
          class="mt-3"
          color="indigo-darken-3"
          variant="flat"
          @click="redirectToProductDetails"
          id="product-detail"
        >
          {{ $t('home.details') }}</v-btn
        >
      </div>
    </v-card-actions>
  </v-card>
</template>

<style scoped>
.v-input {
  display: block;
}
</style>
