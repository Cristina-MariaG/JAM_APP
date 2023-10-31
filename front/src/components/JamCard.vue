<script setup lang="ts">
import type { Product } from '@/types/product.types'
import { ref, defineProps, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'
import { productRepository, stripeRepository } from '@/helpers/api'
import { useAuthStore } from '@/stores/auth'
import Swal from 'sweetalert2'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const authStore = useAuthStore()
const cartStore = useCartStore()
const router = useRouter()

const getImage = (image: string) => {
  return `/uploads/${image}`
}
const { product } = defineProps<{
  product: Product
}>()

// const alreadyInCart = ref(cartStore.productIsAlreadyInTheCart(product.id))

const alreadyInCart = computed(() => {
  return cartStore.productIsAlreadyInTheCart(product.id);
});

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

const deleteProduct = async (id: number) => {
  try {
    await productRepository.deleteProduct({ id, token: authStore.accessToken })
    Swal.fire({
      icon: 'success',
      title: 'Reussi'
    })
  } catch (error: any) {
    if (error.response.status === 401) {
      try {
        const refreshResponse = await stripeRepository.refreshToken(authStore.getRefreshToken)

        const newAccessToken = refreshResponse.data

        authStore.setRefreshedTokens(newAccessToken.token)

        deleteProduct(id)
      } catch (refreshError) {
        authStore.logout()
        router.push({ name: 'login' })
      }
    } else {
      Swal.fire({
        icon: 'error',
        title: t('error.badCredentials ')
      })
    }
  }
}
const redirectToProductDetails = () => {
  router.push(`/product-details/${product.id}`)
}
</script>

<template>
  <v-card class="pa-3 mx-auto">
    <v-img :src="getImage(product.image)" aspect-ratio="1" cover></v-img>

    <v-card-title class="ms-5"> {{ product.name }} </v-card-title>

    <v-card-title class="ms-5">Price: {{ product.price }} €</v-card-title>
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
        <v-btn
          v-if="authStore.isAdmin"
          style="width: 80%"
          class="mt-3"
          color="indigo-darken-3"
          variant="flat"
          @click="deleteProduct(product.id)"
          id="product-detail"
        >
          {{ $t('home.delete') }}</v-btn
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
