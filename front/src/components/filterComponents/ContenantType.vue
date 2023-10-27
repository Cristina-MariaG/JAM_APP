<script setup lang="ts">
import useFilters from '@/composables/filters'
import { contenantTypeRepository } from '@/helpers/api'
import type { TypeContenant } from '@/types/product.types';
import { ref, onMounted, watch } from 'vue'


const apiContenantType = ref<TypeContenant[]>([])
const selectedContenantTypes = ref([])
const storeFilters = useFilters()

watch(selectedContenantTypes, (newVal) => {
  storeFilters.setTypeContenant(newVal)
})
onMounted(async () => {
  const { contenant_types: contenantTypes } = await contenantTypeRepository.getContenantTypes()
  apiContenantType.value = contenantTypes
})
</script>

<template>
  <div>
    <p class="filtersText">{{ $t('filters.contenantType') }}</p>
    <div class="contenantType">
      <div v-for="contenantType in apiContenantType" :key="contenantType.id" class="d-flex">
        <v-checkbox
          v-model="selectedContenantTypes"
          :label="contenantType.type_contenant"
          :value="contenantType.id"
        ></v-checkbox>
      </div>
    </div>
  </div>
</template>

