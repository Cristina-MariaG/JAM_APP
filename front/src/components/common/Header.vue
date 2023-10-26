<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
import AppBarContent from './headerComponents/AppBarContent.vue'
import HeaderActions from './headerComponents/HeaderActions.vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const drawerOpen = ref(false)
</script>

<template>
  <v-app-bar color="indigo-darken-3" prominent>
    <AppBarContent @toogleDrawer="drawerOpen = !drawerOpen" />
  </v-app-bar>
  <v-navigation-drawer v-model="drawerOpen" location="left" temporary>
    <v-btn color="indigo-darken-3" variant="flat" class="mt-5">
      <RouterLink to="/">{{ $t('home.home') }}</RouterLink>
    </v-btn>
    <v-btn v-if="authStore.isAdmin" color="indigo-darken-3" variant="flat">
      <RouterLink to="/dashboard">{{ $t('home.dashboard') }}</RouterLink>
    </v-btn>
    <HeaderActions />
  </v-navigation-drawer>
</template>
<style lang="scss">
.searchBar {
  flex: 2 1;
  margin-top: 1em;
}
.v-navigation-drawer__content {
  background: #283593;
}
.badge {
  content: attr(value);
  font-size: 12px;
  background: red;
  border-radius: 50%;
  padding: 3px;
  position: relative;
  left: -8px;
  top: -10px;
  opacity: 0.9;
}
</style>
