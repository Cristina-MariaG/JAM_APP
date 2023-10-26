<script setup lang="ts">
import { useCartStore } from '@/stores/cart'
const cartStore = useCartStore()
</script>

<template>
  <div class="d-flex">
    <h1 class="ma-2 pa-2 me-auto">{{ $t('cart.cart') }}</h1>

    <h5 class="ma-2 pa-2 d-flex align-self-center">
      {{ cartStore.productsNumber }} {{ $t('cart.products') }}
    </h5>
  </div>
</template>
