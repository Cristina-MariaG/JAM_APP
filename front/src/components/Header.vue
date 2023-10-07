<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, reactive, toRaw } from 'vue'
import type { HeaderItem } from '@/types/headerItems.types'

const drawer = ref(false)
// const lang = ref('fr')
const group = ref(null)

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
    <!-- <v-system-bar color="deep-purple darken-3"></v-system-bar> -->

    <v-app-bar color="primary" prominent>
      <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>JAM</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn variant="text" icon="mdi-magnify">cxc</v-btn>
      <v-select v-model="$i18n.locale" :items="langItems" :label="$t('header.language')"></v-select>

      <v-btn variant="text" icon="mdi-dots-vertical"
        >fgfd
        <!-- <v-switch v-model="lang" hide-details inset :label="`Switch: ${lang.toString()}`"></v-switch -->
        ></v-btn
      >

      <v-btn variant="text" icon="mdi-filter"></v-btn>
    </v-app-bar>

    <v-navigation-drawer expand-on-hover rail>
      <!-- <v-navigation-drawer v-model="drawer" location="bottom" temporary> -->
      <v-list :items="list"></v-list>
    </v-navigation-drawer>
  </v-layout>
</template>
