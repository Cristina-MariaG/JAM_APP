import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import { i18n } from './plugins/i18n'

import createVuetify from './plugins/vuetify'
import App from './App.vue'
import router from './router'
import type { I18n } from 'vue-i18n'

const app = createApp(App)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

app.use(pinia)

// const vuetify = createVuetify({})

app.use(router)
app.use(i18n as I18n)
app.use(createVuetify)


app.mount('#app')
