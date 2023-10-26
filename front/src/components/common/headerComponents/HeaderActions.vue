<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { computed } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

const userAuthenticated = computed(() => authStore.isAuth)

const logoutUser = () => {
  authStore.logout()
  // cartStore.resetStore()
}
</script>
<template>
  <div v-if="userAuthenticated">
    <v-btn @click="logoutUser">{{ $t('home.logoutUser') }}</v-btn>
  </div>
  <div v-if="!userAuthenticated">
    <v-btn color="indigo-darken-3" variant="flat">
      <RouterLink to="/login">{{ $t('login.login') }}</RouterLink></v-btn
    >
  </div>
  <div v-if="!userAuthenticated">
    <v-btn color="indigo-darken-3" variant="flat">
      <RouterLink to="/inscription">{{ $t('login.inscription') }}</RouterLink>
    </v-btn>
  </div>
</template>
