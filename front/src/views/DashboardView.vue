<script setup lang="ts">
import {
  categoryRepository,
  brandRepository,
  contenantTypeRepository,
  flavorRepository,
  ingredientRepository,
  productRepository,
  stripeRepository
} from '@/helpers/api'
import type { Brand, Category, Flavor, Ingredient, TypeContenant } from '@/types/product.types'
import Swal from 'sweetalert2'
import { ref, onMounted, watch, onBeforeMount, reactive } from 'vue'

const apiCategoriesList = ref<Category[]>([])
const apiBrandList = ref<Brand[]>([])
const apiContenantType = ref<TypeContenant[]>([])
const apiFlavorsList = ref<Flavor[]>([])
const apiIngredientList = ref<Ingredient[]>([])
const quantity = ref()
const ingredientsList = ref([])
const addQuantityValue = ref(false)
import { useAuthStore } from '@/stores/auth'
import router from '@/router'

const authStore = useAuthStore()
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const newProduct = reactive({
  categoryId: 'Select',
  brandId: 'Select',
  availableStock: true,
  contenantTypeId: 'Select',
  flavorId: 'Select',
  ingredients: [],
  name: '',
  description: '',
  image: '',
  price: '',
  quantity: null,
  promotion: null
})

onBeforeMount(async () => {
  const { categories } = await categoryRepository.getCategories()
  apiCategoriesList.value = categories

  const { brand_list: brandList } = await brandRepository.getBrands()
  apiBrandList.value = brandList

  const { contenant_types: contenantTypes } = await contenantTypeRepository.getContenantTypes()
  apiContenantType.value = contenantTypes

  const { flavours } = await flavorRepository.getFlavors()
  apiFlavorsList.value = flavours

  const { ingredients } = await ingredientRepository.getIngredients()
  apiIngredientList.value = ingredients
})

const addQuantity = (ingredientId: number) => {
  if (quantity.value && ingredientId) {
    newProduct.ingredients = [...newProduct.ingredients, { ingredientId, quantity: quantity.value }]
  }
}

const submitForm = async () => {
  if (
    newProduct.name &&
    newProduct.description &&
    newProduct.image &&
    newProduct.price &&
    newProduct.quantity !== null &&
    newProduct.promotion !== null &&
    newProduct.categoryId !== 'Select' &&
    newProduct.brandId !== 'Select' &&
    newProduct.contenantTypeId !== 'Select' &&
    newProduct.flavorId !== 'Select' &&
    newProduct.ingredients.length !== 0
  ) {
    const dataToSend= {...newProduct, accessToken : authStore.accessToken}
    try {
      await productRepository.createProduct(dataToSend)
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

          submitForm()
        } catch (refreshError) {
          authStore.logout()
          router.push({ name: 'login' })
        }
      }
    }
  } else {
    Swal.fire({
      icon: 'error',
      title: t('error.badCredentials ')
    })
  }
}
</script>
<template>
  <v-container>
    <h1 class="text-2xl uppercase pb-2">{{ $t('home.dashboard') }}</h1>
    <v-row>
      <v-col cols="2">
        <v-select
          v-if="apiCategoriesList.length"
          v-model="newProduct.categoryId"
          :items="apiCategoriesList"
          item-title="category"
          item-value="id"
          label="Select"
          single-line
        ></v-select>
      </v-col>
      <v-col cols="2">
        <p>Marque</p>
        <v-select
          v-if="apiBrandList.length"
          v-model="newProduct.brandId"
          :items="apiBrandList"
          item-title="brand"
          item-value="id"
          label="Marque"
          single-line
        ></v-select>
      </v-col>
      <v-col cols="2">
        <v-switch
          v-model="newProduct.availableStock"
          label="Only Available Stock"
          hide-details
          inset
        ></v-switch>
      </v-col>
      <v-col cols="2">
        <p>Type contenant</p>

        <v-select
          v-if="apiContenantType.length"
          v-model="newProduct.contenantTypeId"
          :items="apiContenantType"
          item-title="type_contenant"
          item-value="id"
          label="Select"
          single-line
        ></v-select>
      </v-col>
      <v-col cols="2">
        <p>Flavor</p>
        <v-select
          v-if="apiFlavorsList.length"
          v-model="newProduct.flavorId"
          :items="apiFlavorsList"
          item-title="flavor"
          item-value="id"
          label="Select"
          single-line
        ></v-select>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="6">
        <h3>Ingredients</h3>
        <v-text-field
          label="quantité de l'ingredient contenu"
          hide-details="auto"
          type="number"
          v-model="quantity"
        ></v-text-field>
        <v-row v-for="ingredient in apiIngredientList" :key="ingredient.id">
          <v-col cols="8">
            <p>{{ ingredient.ingredient }}</p>
          </v-col>
          <v-col cols="4">
            <v-btn @click="addQuantity(ingredient.id)">Add Quantity</v-btn>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="6">
        <v-form @submit.prevent="submitForm">
          <v-text-field v-model="newProduct.name" label="Name" required></v-text-field>
          <v-text-field v-model="newProduct.description" label="Description"></v-text-field>
          <v-text-field v-model="newProduct.image" label="Image URL"></v-text-field>
          <v-text-field v-model="newProduct.price" label="Price"></v-text-field>
          <v-text-field
            v-model.number="newProduct.quantity"
            label="Quantity"
            type="number"
          ></v-text-field>
          <v-text-field
            v-model.number="newProduct.promotion"
            label="Promotion"
            required
            type="number"
          ></v-text-field>
          <v-btn color="indigo-darken-3" variant="flat" type="submit">Save</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
input {
  background-color: #fafafa;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 8px 12px;
  transition: 0.3s border;
  width: 100%;
  margin-bottom: 12px;
}

.v-select {
  width: 100%;
  margin-bottom: 12px;
}
</style>

<!-- <template>
  <v-container>
    <h1 class="text-2xl uppercase pb-2">{{ $t('home.dashboard') }}</h1>

    <div class="d-flex">
      <v-row>
        <v-col cols="2">
          <div>
            <p>Category</p>
            <v-select
              v-if="apiCategoriesList.length"
              v-model="newProduct.categoryId"
              :items="apiCategoriesList"
              item-title="category"
              item-value="id"
              label="Select"
              single-line
            ></v-select>
          </div>
        </v-col>
        <v-col cols="2">
          <div>
            <p>Marque</p>
            <v-select
              v-if="apiBrandList.length"
              v-model="newProduct.brandId"
              :items="apiBrandList"
              item-title="brand"
              item-value="id"
              label="Select"
              single-line
            ></v-select>
          </div>
        </v-col>
        <v-col cols="2">
          <div>
            <p>Stock dispo</p>
            <v-switch
              v-model="newProduct.availableStock"
              hide-details
              inset
              :label="$t('filters.onlyAvailableStock')"
            ></v-switch>
          </div>
        </v-col>
        <v-col cols="2">
          <div>
            <p>Type Contenant</p>
            <v-select
              v-if="apiContenantType.length"
              v-model="newProduct.contenantTypeId"
              :items="apiContenantType"
              item-title="type_contenant"
              item-value="id"
              label="Select"
              single-line
            ></v-select>
          </div>
        </v-col>
        <v-col cols="2">
          <div>
            <p>Flavor</p>
            <v-select
              v-if="apiFlavorsList.length"
              v-model="newProduct.flavorId"
              :items="apiFlavorsList"
              item-title="flavor"
              item-value="id"
              label="Select"
              single-line
            ></v-select>
          </div>
        </v-col>
      </v-row>
    </div>
    <diV>
      <form @submit.prevent="submitForm">
        <v-row>
          <v-col cols="6">
            <p>Ingredients</p>
            <div v-if="addQuantityValue">
              <v-responsive class="mx-auto" max-width="344">
                <v-text-field
                  label="quantité contenu"
                  hide-details="auto"
                  type="number"
                  v-model="quantity"
                ></v-text-field>
              </v-responsive>
            </div>
            <div class="" v-for="ingredient in apiIngredientList" :key="ingredient.id">
              <p>{{ ingredient.ingredient }}</p>
              <div>
                <v-btn @click="addQuantity(ingredient.id)">Add quantity selected </v-btn>
                <v-btn @click="addQuantityValue = !addQuantityValue">show quantity </v-btn>
              </div>
            </div>
          </v-col>
          <v-col cols="4">
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="newProduct.name" required />
            <br /><br />

            <label for="description">Description:</label>
            <input type="text" id="description" v-model="newProduct.description" />
            <br /><br />

            <label for="image">Image URL:</label>
            <input type="text" id="image" v-model="newProduct.image" />
            <br /><br />

            <label for="price">Price:</label>
            <input type="text" id="price" v-model="newProduct.price" />
            <br /><br />

            <label for="quantity">Quantity:</label>
            <input type="number" id="quantity" v-model.number="newProduct.quantity" />
            <br /><br />

            <label for="promotion">Promotion:</label>
            <input type="number" id="promotion" v-model.number="newProduct.promotion" required />
            <br /><br />

            <v-btn type="submit">Save</v-btn>
          </v-col>
        </v-row>
      </form>
    </diV>
  </v-container>
</template>

<style>
input {
  background-color: #fafafa;
  border: 0;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.3);
  transition: 0.3s box-shadow;
}
</style> -->
