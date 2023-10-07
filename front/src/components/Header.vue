<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, reactive, toRaw } from 'vue'
import type { HeaderItem } from '@/types/headerItems.types'
import { useAuthStore } from '@/stores/auth'
import { computed } from 'vue'

const drawer = ref(false)

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
  <v-layout>
    <v-app-bar color="primary" prominent>
      <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title> <RouterLink to="/">JAM Shop</RouterLink></v-toolbar-title>

      <v-spacer></v-spacer>

      <div class="langueSelector mt-2">
        <v-select
          center-affix
          v-model="$i18n.locale"
          :items="langItems"
          variant="underlined"
          :label="$t('header.language')"
        ></v-select>
      </div>
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
          ><RouterLink to="/signIn">Inscription</RouterLink>
        </v-btn>
      </div>

      <v-btn variant="text" icon="mdi-filter"></v-btn>
    </v-app-bar>

    <v-navigation-drawer expand-on-hover rail>
      <v-list :items="list"></v-list>
    </v-navigation-drawer>
  </v-layout>
</template>
<style>
.langueSelector {
  padding-top: 0.2em;
}
</style>
