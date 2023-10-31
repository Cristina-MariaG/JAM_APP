<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { onBeforeMount, onMounted, ref, watch } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { computed } from 'vue'
import { useCartStore } from '@/stores/cart'
import router from '@/router'
import { useRoute } from 'vue-router'
import useFilters from '@/composables/filters'
import HeaderActions from './HeaderActions.vue'
import { usei18nStore } from '@/stores/i18n'
import { useI18n } from 'vue-i18n'

const route = useRoute()
const searchedValue = ref<string>('')

watch(
  () => route.name,
  () => {
    if (route.name === 'search' && typeof route.params.searched === 'string') {
      searchedValue.value = route.params.searched
    } else {
      searchedValue.value = ''
    }
  }
)

onBeforeMount(() => {
  let locale = usei18nStore().getLang
  if (locale !== useI18n().locale.value) {
    useI18n().locale.value = locale
  }
})

const authStore = useAuthStore()
const cartStore = useCartStore()
const userEmail = computed(() => authStore.getEmail)
const userAuthenticated = computed(() => authStore.isAuth)

defineEmits(['toogleDrawer'])

const searchJam = () => {
  if (route.name != 'home') {
    router.push(`/search/${searchedValue.value}`)
  } else {
    useFilters().setSearchedText(searchedValue.value)
  }
}

const languageOptions = ref<string[]>(useI18n().availableLocales)
const onLanguageChange = (lang: string) => {
  usei18nStore().setLang(lang)
}
const navigateToCart = () => {
  router.push({ name: 'cart' })
}
</script>
<template>
  <v-app-bar-nav-icon variant="text" @click.stop="$emit('toogleDrawer')"></v-app-bar-nav-icon>
  <v-toolbar-title>
    <RouterLink to="/">{{ $t('header.appName') }}</RouterLink></v-toolbar-title
  >
  <v-spacer></v-spacer>
  <div class="searchBar">
    <div>
      <v-text-field
        v-model="searchedValue"
        append-inner-icon="mdi-magnify"
        rounded=""
        :label="$t('filters.searchJam')"
        @click:append-inner="searchJam"
        @keyup.enter="searchJam"
      ></v-text-field>
    </div>
  </div>
  <v-spacer></v-spacer>

  <div class="mt-2 mr-5">
    <v-select
      v-model="$i18n.locale"
      @update:modelValue="onLanguageChange"
      :items="languageOptions"
      variant="underlined"
    ></v-select>
  </div>
  <v-btn @click="navigateToCart">
    <v-icon size="large" color="white" icon="mdi-cart-outline"
      ><RouterLink to="/cart"></RouterLink
    ></v-icon>
    <div class="badge" v-if="cartStore.cartProductsNumber > 0">
      {{ cartStore.cartProductsNumber }}
    </div>
  </v-btn>
  <div v-if="userAuthenticated">
    <span>
      {{ userEmail }}
    </span>
  </div>
  <HeaderActions />
</template>
<style></style>
