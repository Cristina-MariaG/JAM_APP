<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <p>Home Page</p>
  <RouterLink to="/login">{{$t('login')}}</RouterLink>
  test
</template>
<style>

</style>
