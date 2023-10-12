<script setup lang="ts">
import SlidersComponent from '@/components/filterComponents/SlidersComponent.vue'
import CategoryComponent from './filterComponents/CategoryComponent.vue'
import OrderByPrice from './filterComponents/OrderByPriceComponent.vue'
</script>
<template>
  <div style="width: 80%">
    <SlidersComponent />
    <OrderByPrice />
    <CategoryComponent />
  </div>
</template>
