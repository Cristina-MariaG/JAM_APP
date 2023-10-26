<script setup lang="ts">
import type { Product } from '@/types/product.types'
import { ref, defineProps } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'

const cartStore = useCartStore()
const router = useRouter()

const quantityOptions = ref([1, 2, 3, 4, 5])
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

    <v-card-title class="ms-5"> {{ product.price }} €</v-card-title>
    <v-card-actions>
      <v-btn v-if="alreadyInCart" @click="addToCart">Modifier</v-btn>
      <v-btn v-else @click="addToCart">Ajouter</v-btn>
      <v-select v-model="selectedQuantity" :items="quantityOptions" label="Qty"></v-select>
    </v-card-actions>
    <v-btn @click="redirectToProductDetails" id="product-detail">
      See details...</v-btn
    >
  </v-card>
</template>
