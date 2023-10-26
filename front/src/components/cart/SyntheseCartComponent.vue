<script setup lang="ts">
import { stripeRepository } from '@/helpers/api'
import { useCartStore } from '@/stores/cart'
import { useAuthStore } from '@/stores/auth'
import router from '@/router'

const authStore = useAuthStore()
const cartStore = useCartStore()

const redirectToStripe = async () => {
  const orderData = {
    cart: cartStore.getCart,
    accessToken: authStore.getAccessToken,
    total: cartStore.totalPrice
  }
  try {
    const { data } = await stripeRepository.createCheckoutSession(orderData)
    cartStore.setWaitingPaymentOrderId(data.order_id)
    window.location.href = data.url
  } catch (error: any) {
    if (error.response.status === 401) {
      try {
        const refreshResponse = await stripeRepository.refreshToken(authStore.getRefreshToken)

        const newAccessToken = refreshResponse.data

        authStore.setRefreshedTokens(newAccessToken.token)

        redirectToStripe()
      } catch (refreshError) {
        authStore.logout()
        router.push({ name: 'login' })
      }
    }
  }
}
</script>

<template>
  <div>
    <div class="d-flex">
      <h1 class="ma-2 pa-2 me-auto">{{ $t('cart.synthese') }}</h1>
    </div>
    <div>
      <hr class="gray-line" />
    </div>

    <div class="d-flex flex-column">
      <div class="align-start">
        <div class="align-self-start d-flex">
          <h1 class="ma-2 pa-2 me-auto">{{ $t('cart.total') }}</h1>
          <h1 class="ma-2 pa-2 me-auto">{{ cartStore.totalPrice }} €</h1>
        </div>
      </div>

      <div class="align-end mt-auto" v-if="!authStore.isAuth">
        <p>{{ $t('cart.notConnected') }}</p>
        <div class="d-flex mt-5">
          <v-btn color="indigo-darken-3" variant="flat" class="mx-3">
            <RouterLink to="/login">{{ $t('login.login') }}</RouterLink>
          </v-btn>
          <v-btn color="indigo-darken-3" variant="flat">
            <RouterLink to="/inscription">{{ $t('login.inscription') }}</RouterLink>
          </v-btn>
        </div>
      </div>

      <div v-else class="align-end mt-auto">
        <v-btn color="indigo-darken-3" variant="flat" @click="redirectToStripe">
          {{ $t('cart.validateCart') }}</v-btn
        >
      </div>
    </div>
  </div>
</template>
