<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { productRepository } from '@/helpers/api'
import type { Product } from '@/types/product.types'

const props = defineProps<{
  productId: string
}>()

const product = ref<Product>()

onMounted(async () => {
  product.value = await productRepository.getProductWithId(props.productId)
})

const cards = [
  { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
  { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6 },
  { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 }
]
</script>
<template>
  <div>
    <h1>Détails du produit</h1>
    <p>ID du produit : {{ props.productId }}</p>
    {{ product }}
    <!-- Affichez les détails du produit en fonction de l'ID -->
  </div>
  <!-- 
  <div v-if="product" class="product-detail">
    <h1>{{ product.name }}</h1>
    <img :src="product.image" alt="Product Image" />
    <p>Description: {{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
    <p>Flavor: {{ product.flavor }}</p>
    <p>Brand: {{ product.brand }}</p>
    <p>Stock Available: {{ product.stock_disponible }}</p>
   

  <v-card
    class="mx-auto"
    max-width="500"
  > -->
  <!-- <v-system-bar
      color="indigo darken-2"
      dark
    >
      <v-spacer></v-spacer>

      <v-icon icon="mdi-window-minimize"></v-icon>

      <v-icon icon="mdi-window-maximize"></v-icon>

      <v-icon icon="mdi-close"></v-icon>
    </v-system-bar>

    <v-toolbar
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Discover</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon="mdi-magnify"></v-btn>
    </v-toolbar> -->

  <v-container fluid>
    <v-row dense>
         <v-col> test </v-col>
      <v-col> test </v-col>
      <!-- <v-col v-for="card in cards" :key="card.title" :cols="card.flex">
        <v-card>
          <v-img
            :src="card.src"
            class="align-end"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            height="200px"
            cover
          >
            <v-card-title class="text-white" v-text="card.title"></v-card-title>
          </v-img>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn size="small" color="surface-variant" variant="text" icon="mdi-heart"></v-btn>

            <v-btn size="small" color="surface-variant" variant="text" icon="mdi-bookmark"></v-btn>

            <v-btn
              size="small"
              color="surface-variant"
              variant="text"
              icon="mdi-share-variant"
            ></v-btn>
          </v-card-actions>
        </v-card>
      </v-col> -->
    </v-row>
  </v-container>
  <!-- </v-card> -->
</template>

<style scoped>
.product-detail {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.product-detail h1 {
  font-size: 24px;
  margin-bottom: 10px;
}

.product-detail img {
  max-width: 100%;
  height: auto;
  margin-bottom: 10px;
}
</style>
