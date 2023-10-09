<script setup lang="ts">
import type { Product } from '@/types/product.types'
import { ref, defineProps, reactive, toRaw } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'

const cartStore = useCartStore()
const router = useRouter()
const selectedQuantity = ref(1)
const quantityOptions = ref([1, 2, 3, 4, 5])
const getImage = (image: string) => {
  return `public/uploads/${image}`
}
const { product } = defineProps<{
  product: Product
}>()

const addToCart = () => {
  // Mettez ici la logique pour ajouter le produit au panier
  const productToAdd = {
    ...product,
    selectedQuantity: selectedQuantity.value
  }
  cartStore.addToCart(productToAdd)
}
const redirectToProductDetails = () => {
  const productId = product.id // Assurez-vous d'adapter cela à votre modèle de données

  // Utilisez Vue Router pour rediriger vers la page de détails du produit
  router.push(`/product-details/${productId}`)
}
</script>

<template>
  <v-card class="pa-3 mx-auto">
    <v-img :src="getImage(product.image)" aspect-ratio="1" cover></v-img>

    <v-card-title class="ms-5"> {{ product.name }} </v-card-title>

    <v-card-title class="ms-5"> {{ product.price }} €</v-card-title>
    <v-btn @click="redirectToProductDetails"> See details...</v-btn>
    <v-card-actions>
      <v-btn @click="addToCart" color="primary"> Ajouter au panier </v-btn>
      <v-select v-model="selectedQuantity" :items="quantityOptions" label="Quantité"></v-select>
    </v-card-actions>

    <!--  <v-card-actions>
      <v-btn color="orange-lighten-2" variant="text"> Details </v-btn>

      <v-spacer></v-spacer>

      <v-btn :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'" @click="show = !show"></v-btn>
    </v-card-actions>

  <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          <div>
            <h3>Quantité</h3>
            <p>{{ product.quantity }} g</p>
          </div>
          <div>
            <h3>Description</h3>
            <p>
              {{ product.description }}
            </p>
          </div>
          <div>
            <h3>Ingrédients :</h3>
            <ul>
              <li v-for="ingredient in product.ingredients" :key="ingredient.id">
                {{ ingredient.ingredient.ingredient }} ({{ ingredient.quantity }})
              </li>
            </ul>
          </div>
        </v-card-text>
      </div>
    </v-expand-transition> -->
  </v-card>
</template>
