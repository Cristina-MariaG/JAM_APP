<script setup lang="ts">
import useFilters from '@/composables/filters'
import { ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const orderedType = ref(['Ascending', 'Descending'])
const selectedOrder = ref(t('filters.select'))
const storeFilters = useFilters()

watch(selectedOrder, (val) => {
  storeFilters.setOrdonateByPrice(val)
})
</script>

<template>
  <div>
    <p id="title" class="filtersText">{{ $t('filters.orderByPrice') }}</p>
    <v-combobox
      v-model="selectedOrder"
      :items="orderedType"
      variant="solo-filled"
      label=""
    ></v-combobox>
  </div>
</template>
<style lang="scss" scoped>
.v-input--density-default {
  --v-input-control-height: 15px;
  --v-input-padding-top: 15px;
}
</style>
