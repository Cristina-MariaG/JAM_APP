import en from '@/locales/en.json'
import fr from '@/locales/fr.json'

import { createI18n, useI18n } from 'vue-i18n'
import { mockTranslateText, mockTranslateDate } from '@/functions/i18nMocks'

const locale = import.meta.env.VITE_I18N_LOCALE || 'fr'

const messages = {
  fr,
  en
}

const plugin =  process.env.NODE_ENV === 'test'
    ? { global: { t: mockTranslateText, d: mockTranslateDate } }
    : createI18n({
      legacy: false,
      allowComposition: true,
      locale,
      messages,
    })

const composable =
  process.env.NODE_ENV === 'test' ? () => ({ t: mockTranslateText, d: mockTranslateDate }) : useI18n

export { plugin as i18n, composable as useI18n }

