<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { productRepository } from '@/helpers/api'
import type { Product } from '@/types/product.types'

const props = defineProps<{
  productId: string
}>()

const product = ref<Product>()
const getImage = (image: string) => {
  return `/uploads/${image}`
}
onMounted(async () => {
  const { product: product_fetched } = await productRepository.getProductWithId(props.productId)
  product.value = product_fetched
})

const capitalizeFirstLetter = (name: string): string => {
  return name.charAt(0).toUpperCase() + name.slice(1)
}
</script>
<template>
  <div class="mx-auto product-detail" style="width: 70%" v-if="product">
    <div class="text-center">
      <h1>{{ $t('product.detailsTitle') }}</h1>
    </div>
    <h2 class="text-center">{{ capitalizeFirstLetter(product.name) }}</h2>
    <div class="d-flex justify-center">
      <div style="width: 50%" class="d-flex justify-end align-center">
        <div style="width: 70%">
          <v-img :src="getImage(product.image)" aspect-ratio="1" cover></v-img>
        </div>
      </div>
      <div class="d-flex justify-start align-center product-description" style="width: 50%">
        <div>
          <p>{{ $t('product.category') }} {{ product.category.category }}</p>
          <p>{{ $t('product.brand') }} {{ product.brand.brand }}</p>
          <p>{{ $t('product.description') }} {{ product.description }}</p>
          <p>{{ $t('product.price') }} {{ product.price }} €</p>
          <p>{{ $t('product.flavor') }} {{ product.flavor.flavor }}</p>
          <p>{{ $t('product.containerType') }} {{ product.type_contenant.type_contenant }}</p>
          <p>
            {{ $t('product.stockAvailable') }}
            {{
              product.stock_disponible.stock_disponible === 'true'
                ? $t('product.yes')
                : $t('product.no')
            }}
          </p>
          <p>
            {{ $t('product.onPromotion')
            }}{{ product.promotion === 1 ? $t('product.yes') : $t('product.no') }}
          </p>
          <p>{{ $t('product.ingredients') }} :</p>
          <div v-for="ingredient in product.ingredients">
            <p class="ms-5 ps-5">
              * {{ ingredient.ingredient.ingredient }} {{ ingredient.quantity }} g
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.product-detail {
  max-width: 600px;
  margin: 0 auto;
  padding: 0.3em;
  h1 {
    font-size: 2.5em;
    margin-bottom: 0.5em;
  }
  .product-description {
    margin: 0.5em 0 0 2em;
    p {
      font-size: larger;
      font-family: 'Times New Roman', Times, serif;
      padding: 0.1em;
    }
  }
}
</style>
