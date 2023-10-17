<script setup lang="ts">
import { stripeRepository } from '@/helpers/api'
import { useCartStore } from '@/stores/cart'
import Swal from 'sweetalert2'
import { ref, onBeforeMount } from 'vue'
import { useRouter } from 'vue-router'
const router = useRouter()
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const cartStore = useCartStore()
onBeforeMount(async () => {
  await stripeRepository
    .checkoutCancel(cartStore.getOrderId)
    .then((response) => {
      cartStore.resetOrderId()
      setTimeout(() => {
        router.push({ name: 'home' })
      }, 3000)
    })
    .catch((err) => {
      Swal.fire({
        icon: 'error',
        title: t('error.genericError ')
      })
    })
})
</script>
<template>
  <h1 class="text-2xl uppercase pb-2">
    {{ $t('checkout.cancel') }}
  </h1>
</template>
