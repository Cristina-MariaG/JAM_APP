<script setup lang="ts">
import PriceLimitsComponent from '@/components/filterComponents/PriceLimitsComponent.vue'
import CategoryComponent from './filterComponents/CategoryComponent.vue'
import OrderByPrice from './filterComponents/OrderByPriceComponent.vue'
import ContenantType from './filterComponents/ContenantType.vue'
import AvailableStock from './filterComponents/AvailableStock.vue'
import Brand from './filterComponents/Brand.vue'
</script>
<template>
  <div style="width: 80%">
    <PriceLimitsComponent />
    <OrderByPrice />
    <CategoryComponent />
    <ContenantType />
    <AvailableStock />
    <Brand />
  </div>
</template>
