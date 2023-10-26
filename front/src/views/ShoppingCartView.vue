<script setup lang="ts">
import { useCartStore } from '@/stores/cart'
import CardJamCartComponent from '@/components/cart/CardJamCartComponent.vue'

const cartStore = useCartStore()
</script>

<template>
  <div>
    <div v-if="cartStore.productsNumber === 0">
      <h1 class="text-center">{{ $t('cart.empty') }}</h1>
    </div>
    <div v-else style="width: 80%" class="mx-auto mt-5">
      <CardJamCartComponent />
    </div>
  </div>
</template>
<style></style>
