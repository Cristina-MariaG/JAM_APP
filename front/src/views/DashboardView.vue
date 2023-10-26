<script setup lang="ts">

</script>
<template>
  <h1 class="text-2xl uppercase pb-2">{{ $t('dashboard') }}</h1>

  <v-btn color="primary">
    <RouterLink to="/">{{ $t('home.home') }}</RouterLink>
  </v-btn>
</template>
