<script setup lang="ts">
import Header from './Header.vue'
</script>

<template>
  <div>
    <v-layout fill-height>
      <Header />

      <v-main>
        <slot></slot>
      </v-main>
    </v-layout>
  </div>
</template>
