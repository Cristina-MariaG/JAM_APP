import { authRepository } from '@/helpers/api'
import type { AuthForm } from '@/types/auth.types'
import { defineStore } from 'pinia'

interface MapStoreState {
  accessToken: string
  failedCount: number
}

export const useAuthStore = defineStore('auth', {
  state: (): MapStoreState => ({
    accessToken: '',
    failedCount: 0
  }),

  getters: {
    isAuth(state) {
      return state.accessToken !== ''
    }
  },

  actions: {
    async login(payload: AuthForm) {
      try {
        const { accessToken } = await authRepository.login(payload)
        // this.accessToken = accessToken
        this.$patch({ accessToken })
        return true
      } catch (err) {
        this.failedCount++
        return false
      }
    },
    async signIn(payload: AuthForm) {
      try {
        const { accessToken } = await authRepository.signIn(payload)
        // this.accessToken = accessToken
        this.$patch({ accessToken })
        return true
      } catch (err) {
        this.failedCount++
        return false
      }
    }
  }
})
