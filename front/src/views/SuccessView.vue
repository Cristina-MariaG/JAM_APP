<script setup lang="ts">
import { stripeRepository } from '@/helpers/api'
import { useCartStore } from '@/stores/cart'
import { ref, onBeforeMount } from 'vue'

const cartStore = useCartStore()
// Get the cart data
onBeforeMount(async () => {
  console.log(cartStore.getOrderId)
  await stripeRepository
    .checkoutSuccess(cartStore.getOrderId)
    .then((response) => {
      cartStore.resetStore()
      console.log(response)
    })
    .catch((err) => {
      console.log(err)
    })

  //   const response = await updateOrderStatus()
})
</script>
<template>
  <h1 class="text-2xl uppercase pb-2">Votre commande a été enregistré avec success !</h1>

  <v-btn> </v-btn>
</template>
