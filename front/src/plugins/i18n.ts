import { createI18n } from 'vue-i18n'
import en from '@/locales/en.json'
import fr from '@/locales/fr.json'

type MessageSchema = typeof en
const i18n = createI18n<[MessageSchema], 'en' | 'fr'>({
  legacy: false,
  locale: import.meta.env.VITE_I18N_LOCALE || 'fr',
  fallbackLocale: import.meta.env.VITE_I18N_FALLBACK_LOCALE || 'en',
  messages: {
    en,
    fr
  }
})

export default i18n
