<script setup lang="ts">
import { stripeRepository } from '@/helpers/api'
import { useCartStore } from '@/stores/cart'
import Swal from 'sweetalert2'
import { ref, onBeforeMount } from 'vue'

import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const cartStore = useCartStore()
onBeforeMount(async () => {
  await stripeRepository
    .checkoutSuccess(cartStore.getOrderId)
    .then((response) => {
      cartStore.resetStore()
    })
    .catch((err) => {
      console.log(err)
      Swal.fire({
        icon: 'error',
        title: t('error.genericError ')
      })
    })
})
</script>
<template>
  <h1 class="text-2xl uppercase pb-2">{{ $t('checkout.success') }}</h1>

  <v-btn color="primary">
    <RouterLink to="/">{{ $t('home.home') }}</RouterLink>
  </v-btn>
</template>
