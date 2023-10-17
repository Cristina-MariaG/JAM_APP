<script setup lang="ts">
import useFilters from '@/composables/filters'
import { categoryRepository } from '@/helpers/api'
import { ref, onMounted, watch, onBeforeMount } from 'vue'

interface Category {
  id: number
  category: string
}
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
<style lang="scss">
.v-input--density-default {
  --v-input-control-height: 0px;
  --v-input-padding-top: 0px;
}
.v-selection-control.v-selection-control--density-default {
  --v-selection-control-size: 25px;
}
.v-input__details {
  min-height: auto;
  padding: 0;
}

.separator {
  width: 90%;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
}
</style>
