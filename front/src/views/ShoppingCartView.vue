<script setup lang="ts">
import { RouterLink } from 'vue-router'

import { toRaw } from 'vue'
import { useCartStore } from '@/stores/cart'
import { stripeRepository } from '@/helpers/api'

import { useAuthStore } from '@/stores/auth'
import HrComponent from '@/components/HrComponent.vue'

const authStore = useAuthStore()
const cartStore = useCartStore()
const getImageUrl = (imageName: string) => {
  return `../public/uploads/${imageName}`
}
const getTotalPrice = (price: number, selectedQuantity: number) => {
  return selectedQuantity * price
}

const redirectToStripe = async () => {
  const orderData = {
    cart: cartStore.getCart,
    token: authStore.getToken,
    total: cartStore.totalPrice
  }

  const { url, order_id: orderId } = await stripeRepository.createCheckoutSession(toRaw(orderData))
  cartStore.setWaitingPaymentOrderId(orderId)
  window.location.href = url
}
</script>

<template>
  <div>
    <div v-if="cartStore.productsNumber === 0">
      <h1 class="text-center">Le panier est vide</h1>
    </div>
    <div v-else style="width: 80%" class="mx-auto mt-5">
      <v-card>
        <v-container fluid>
          <v-row dense>
            <v-col cols="8">
              <div class="d-flex">
                <h1 class="ma-2 pa-2 me-auto">Panier</h1>

                <h5 class="ma-2 pa-2 d-flex align-self-center">
                  {{ cartStore.productsNumber }} produits
                </h5>
              </div>
              <div>
                <hr class="gray-line" />
                <v-container fluid>
                  <v-row dense>
                    <v-col cols="3" class="d-flex align-self-center">
                      <p>Image</p>
                    </v-col>
                    <v-col cols="2" class="d-flex align-self-center">
                      <p>Name</p>
                    </v-col>
                    <v-col cols="2" class="d-flex align-self-center">
                      <p>Price</p>
                    </v-col>
                    <v-col cols="2" class="d-flex align-self-center">
                      <p>Quantity</p>
                    </v-col>
                    <v-col cols="2" class="d-flex align-self-center">
                      <p>Total Price</p>
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
              </div>
            </v-col>

            <v-col col="4" class="ps-5">
              <div>
                <div class="d-flex">
                  <h1 class="ma-2 pa-2 me-auto">Synthèse</h1>
                </div>
                <div>
                  <hr class="gray-line" />
                </div>

                <div class="d-flex flex-column">
                  <div class="align-start">
                    <div class="align-self-start d-flex">
                      <h1 class="ma-2 pa-2 me-auto">Total</h1>
                      <h1 class="ma-2 pa-2 me-auto">{{ cartStore.totalPrice }} €</h1>
                    </div>
                  </div>

                  <div class="align-end mt-auto" v-if="!authStore.isAuth">
                    <p>Vous devez être connecté pour pouvoir commander</p>
                    <div class="mt-5">
                      <v-btn color="indigo-darken-3" variant="flat" class="mx-5">
                        <RouterLink to="/login">Connexion</RouterLink>
                      </v-btn>
                      <v-btn color="indigo-darken-3" variant="flat">
                        <RouterLink to="/inscription">Inscription</RouterLink>
                      </v-btn>
                    </div>
                  </div>

                  <div v-else class="align-end mt-auto">
                    <v-btn color="indigo-darken-3" variant="flat" @click="redirectToStripe">
                      Valider le panier</v-btn
                    >
                  </div>
                </div>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </div>
  </div>
</template>
<style></style>
