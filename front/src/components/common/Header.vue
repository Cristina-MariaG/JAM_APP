<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { ref, watch } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { computed } from 'vue'
import { useCartStore } from '@/stores/cart'
import router from '@/router'
import { useRoute } from 'vue-router'
import useFilters from '@/composables/filters'

const route = useRoute()
const drawerOpen = ref(false)
const searchedValue = ref<string>('')

watch(
  () => route.name,
  () => {
    if (route.name === 'search' && typeof route.params.searched === 'string') {
      searchedValue.value = route.params.searched
    }
  }
)

const authStore = useAuthStore()
const cartStore = useCartStore()

const userEmail = computed(() => authStore.getEmail)
const userAuthenticated = computed(() => authStore.isAuth)

const logoutUser = () => {
  authStore.logout()
  // cartStore.resetStore()
}

const searchJam = () => {
  if (route.name != 'home') {
    router.push(`/search/${searchedValue.value}`)
  } else {
    useFilters().setSearchedText(searchedValue.value)
  }
}

const languageOptions = ref<string[]>(['fr', 'en'])

const navigateToCart = () => {
  router.push({ name: 'cart' })
}
</script>

<template>
  <v-app-bar color="indigo-darken-3" prominent>
    <v-app-bar-nav-icon variant="text" @click.stop="drawerOpen = !drawerOpen"></v-app-bar-nav-icon>
    <v-toolbar-title> <RouterLink to="/">JAM Shop</RouterLink></v-toolbar-title>
    <v-spacer></v-spacer>
    <div class="searchBar">
      <div>
        <v-text-field
          v-model="searchedValue"
          append-inner-icon="mdi-magnify"
          rounded=""
          label="Search Jam"
          @click:append-inner="searchJam"
          @keyup.enter="searchJam"
        ></v-text-field>
      </div>
    </div>
    <v-spacer></v-spacer>

    <div class="mt-2 mr-5">
      <v-select v-model="$i18n.locale" :items="languageOptions" variant="underlined"></v-select>
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
      <v-btn @click="logoutUser">Disconnect</v-btn>
    </div>
    <div v-else>
      <v-btn color="indigo-darken-3" variant="flat" class="mx-5">
        <RouterLink to="/login">Connexion</RouterLink></v-btn
      >
      <v-btn color="indigo-darken-3" variant="flat"
        ><RouterLink to="/inscription">Inscription</RouterLink>
      </v-btn>
    </div>
  </v-app-bar>
  <v-navigation-drawer v-model="drawerOpen" location="left" temporary>
    <p>
      <RouterLink to="/">Home</RouterLink>
    </p>
    <p v-if="authStore.isAuth" @click="logoutUser">Deconexion</p>
    <div v-else>
      <p>
        <RouterLink to="/login">Connexion</RouterLink>
      </p>
      <p>
        <RouterLink to="/inscription">Inscription</RouterLink>
      </p>
    </div>
  </v-navigation-drawer>
</template>
<style lang="scss" scoped>
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
