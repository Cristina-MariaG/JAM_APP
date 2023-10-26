<script setup lang="ts">
import { useCartStore } from '@/stores/cart'
import HrComponent from '@/components/HrComponent.vue'
const cartStore = useCartStore()

const getImageUrl = (imageName: string) => {
  return `../public/uploads/${imageName}`
}
const getTotalPrice = (price: number, selectedQuantity: number) => {
  return selectedQuantity * price
}
</script>

<template>
  <v-container fluid>
    <v-row dense>
      <v-col cols="3" class="d-flex align-self-center">
        <p>{{ $t('cart.image') }}</p>
      </v-col>
      <v-col cols="2" class="d-flex align-self-center">
        <p>{{ $t('cart.name') }}</p>
      </v-col>
      <v-col cols="2" class="d-flex align-self-center">
        <p>{{ $t('cart.price') }}</p>
      </v-col>
      <v-col cols="2" class="d-flex align-self-center">
        <p>{{ $t('cart.quantity') }}</p>
      </v-col>
      <v-col cols="2" class="d-flex align-self-center">
        <p>{{ $t('cart.totalPrice') }}</p>
      </v-col>
    </v-row>
    <HrComponent />
    <div v-for="product in cartStore.getCart" :key="product.id">
      <v-row dense>
        <v-col cols="3">
          <v-img :src="getImageUrl(product.image)" aspect-ratio="1"></v-img>
        </v-col>
        <v-col cols="2" class="d-flex align-self-center">
          <p>{{ product.name }}</p>
        </v-col>
        <v-col cols="2" class="d-flex align-self-center">
          <p>{{ product.price }} €</p>
        </v-col>
        <v-col cols="2" class="d-flex align-self-center">
          <p>{{ product.selectedQuantity }}</p>
        </v-col>
        <v-col cols="2" class="d-flex align-self-center">
          <p>{{ getTotalPrice(product.price, product.selectedQuantity) }} €</p>
        </v-col>
      </v-row>
      <HrComponent />
    </div>
  </v-container>
</template>
