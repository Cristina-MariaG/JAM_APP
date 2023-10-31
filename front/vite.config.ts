import { fileURLToPath, URL } from 'node:url'
import { resolve, dirname } from 'node:path'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import VueI18nPlugin from '@intlify/unplugin-vue-i18n/vite'
import vuetify from 'vite-plugin-vuetify'
import { defineConfig, configDefaults } from 'vitest/config'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
    vuetify(),
    VueI18nPlugin({
      include: resolve(dirname(fileURLToPath(import.meta.url)), './src/locales/**') // provide a path to the folder where you'll store translation data (see below)
    })
  ],
  optimizeDeps: {
    exclude: ['vuetify'] // to avoid errors during cypress integration tests
  },

  server: {
    port: 8000,
    watch: {
      usePolling: true
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  define: {
    __VUE_I18N_FULL_INSTALL__: true,
    __VUE_I18N_LEGACY_API__: false,
    __INTLIFY_PROD_DEVTOOLS__: false
  },

  test: {
    root: fileURLToPath(new URL('./', import.meta.url)),
    environment: 'jsdom',
    exclude: [...configDefaults.exclude, 'e2e/*'],
    setupFiles: ['./vitest.setup.ts'],
    server: {
      deps: {
        inline: ['vuetify']
      }
    },
    globals: true,
    watch: false
  }
})
