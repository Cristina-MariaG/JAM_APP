<script setup lang="ts">
import { ref, defineProps, reactive, toRaw } from 'vue'
import { useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'

const cartStore = useCartStore()
</script>

<template>
  <div>
    <div v-if="cartStore.productsNumber === 0">
      <p>Le panier est vide</p>
    </div>
    <div v-else style="width: 80%" class="mx-auto mt-5">
      <v-card>
        <v-container fluid>
          <v-row dense>
            <v-col cols="8" >
              <div class="d-flex">
                <h1 class="ma-2 pa-2 me-auto">Panier</h1>

                <h5 class="ma-2 pa-2">{{ cartStore.productsNumber }} produits</h5>
              </div>
               <div v-for="product in cartStore.getCart">

               </div>
            </v-col>
            <v-col> test </v-col>
          </v-row>
        </v-container>
        <!-- {{ cartStore.getCart }} -->
      </v-card>
    </div>
  </div>
</template>
