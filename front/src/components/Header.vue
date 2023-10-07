<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, reactive, toRaw } from 'vue'
import type { HeaderItem } from '@/types/headerItems.types'
import { useAuthStore } from '@/stores/auth'
import { computed } from 'vue'

const drawer = ref(false)
// const cartItemCount = ref(5)

const authStore = useAuthStore()

const userEmail = computed(() => authStore.getEmail)

const userAuthenticated = computed(() => authStore.isAuth)

const logOutUser = () => {
  authStore.logout()
}

const langItems = ref<string[]>(['fr', 'en'])
const list = ref<HeaderItem[]>([
  {
    title: 'Foo',
    value: 'foo'
  },
  {
    title: 'Bar',
    value: 'bar'
  },
  {
    title: 'Fizz',
    value: 'fizz'
  },
  {
    title: 'Buzz',
    value: 'buzz'
  }
])
</script>

<template>
  <v-app-bar color="indigo-darken-3" prominent>
    <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

    <v-toolbar-title> <RouterLink to="/">JAM Shop</RouterLink></v-toolbar-title>

    <v-spacer></v-spacer>

    <div class="mt-2 mr-5">
      <v-select v-model="$i18n.locale" :items="langItems" variant="underlined"></v-select>
      <!-- :label="$t('header.language')" -->
    </div>
    <v-btn>
      <v-icon size="large" color="white" icon="mdi-cart-outline"></v-icon>
      <!-- <div class="badge" v-if="cartItemCount > 0">{{ cartItemCount }}</div> -->
    </v-btn>
    <div v-if="userAuthenticated">
      <span>
        {{ userEmail }}
      </span>
      <v-btn @click="logOutUser">Disconnect</v-btn>
    </div>
    <div v-else>
      <v-btn color="indigo-darken-3" variant="flat" class="mx-5">
        <RouterLink to="/login">Connexion</RouterLink></v-btn
      >
      <v-btn color="indigo-darken-3" variant="flat"
        ><RouterLink to="/signup">Inscription</RouterLink>
      </v-btn>
    </div>
  </v-app-bar>
  <v-navigation-drawer v-model="drawer" location="left" temporary>
    <v-list :items="list"></v-list>
  </v-navigation-drawer>
</template>
<style>
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
