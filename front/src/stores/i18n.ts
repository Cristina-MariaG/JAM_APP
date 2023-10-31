import { defineStore } from 'pinia'

interface i18n {
  lang: string
}

export const usei18nStore = defineStore('i18n', {
  state: (): i18n => ({
    lang: 'fr'
  }),
  getters: {
    getLang(state) {
      return state.lang
    }
  },
  actions: {
    setLang(lang: string) {
        this.lang = lang
    }
  },
  persist: true
})
