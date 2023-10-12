<script setup lang="ts">
import useFilters from '@/composables/filters';
import { filteringDataRepository } from '@/helpers/api'
import { ref, onMounted, watch, onBeforeMount } from 'vue'

interface Category {
  id: number
  category: string
}
const apiCategories = ref<Category[]>([])
const selectedCategories = ref([])
const storeFilters = useFilters()


watch(selectedCategories,(newVal)=>{
    storeFilters.setCategoriesSearched(newVal)

})
onMounted(async () => {
  const { categories } = await filteringDataRepository.getCategories()
  console.log(categories)
  apiCategories.value = categories
})
</script>

<template>
  <div>
    <p>Category</p>
    <div>
      <div v-for="category in apiCategories" :key="category.id" class="d-flex ">
        <v-checkbox
          v-model="selectedCategories"
          :label="category.category"
          :value="category.id"
        ></v-checkbox>
      </div>
    </div>
  </div>
</template>
