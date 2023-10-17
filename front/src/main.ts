import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import i18n from './plugins/i18n'
// import VueI18n from 'vue-i18n'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import App from './App.vue'
import router from './router'

// const app = createApp(App, {
//   setup() {
//     const { t } = VueI18n.useI18n() // call `useI18n`, and spread `t` from  `useI18n` returning
//     return { t } // return render context that included `t`
//   }
// })

const app = createApp(App)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

app.use(pinia)

const vuetify = createVuetify({
  components,
  directives
})

app.use(router)
app.use(i18n)
app.use(vuetify)

// app.config.globalProperties.t = i18n.global.t

app.mount('#app')
