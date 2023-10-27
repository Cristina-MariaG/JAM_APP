<script setup lang="ts">
import useFilters from '@/composables/filters'
import { categoryRepository } from '@/helpers/api'
import type { Category } from '@/types/product.types';
import { ref, onMounted, watch } from 'vue'


const apiCategories = ref<Category[]>([])
const selectedCategories = ref([])
const storeFilters = useFilters()

watch(selectedCategories, (newVal) => {
  storeFilters.setCategoriesSearched(newVal)
})
onMounted(async () => {
  const { categories } = await categoryRepository.getCategories()
  apiCategories.value = categories
})
</script>

<template>
  <div>
    <p class="filtersText">{{ $t('filters.category') }}</p>
    <div class="category">
      <div v-for="category in apiCategories" :key="category.id" class="d-flex">
        <v-checkbox
          v-model="selectedCategories"
          :label="category.category"
          :value="category.id"
        ></v-checkbox>
      </div>
    </div>
  </div>
</template>
<style lang="scss" >

.separator {
  width: 90%;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
}
</style>
