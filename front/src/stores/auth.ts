import { authRepository } from '@/helpers/api'
import type { AuthForm } from '@/types/auth.types'
import { defineStore } from 'pinia'

interface UserStoreState {
  email: string
  accessToken: string
  refreshToken: string
}

export const useAuthStore = defineStore('auth', {
  state: (): UserStoreState => ({
    accessToken: '',
    refreshToken: '',
    email: ''
  }),

  getters: {
    isAuth(state) {
      return state.accessToken !== ''
    },
    getAccessToken(state) {
      return state.accessToken
    },
    getRefreshToken(state) {
      return state.refreshToken
    },
    getEmail(state) {
      console.log(state.email)
      return state.email
    }
  },

  actions: {
    async login(payload: AuthForm) {
      try {
        const {
          token,
          user: { email }
        } = await authRepository.login(payload)
        this.$patch({ email, accessToken: token.access_token, refreshToken: token.refresh_token })
        return true
      } catch (err) {
        return false
      }
    },
    async setRefreshedTokens(token: any) {
      try {
        console.log(token)
        this.$patch({ accessToken: token.access_token, refreshToken: token.refresh_token })
        return true
      } catch (err) {
        return false
      }
    },
    async inscription(payload: AuthForm) {
      try {
        await authRepository.inscription(payload)

        return true
      } catch (err) {
        return false
      }
    },
    logout() {
      this.$reset()
    }
  },
  persist: true
})
