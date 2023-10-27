import { authRepository } from '@/helpers/api'
import type { AuthForm } from '@/types/auth.types'
import { defineStore } from 'pinia'

interface UserStoreState {
  email: string
  accessToken: string
  refreshToken: string
  role: string
}

export const useAuthStore = defineStore('auth', {
  state: (): UserStoreState => ({
    accessToken: '',
    refreshToken: '',
    email: '',
    role: ''
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
      return state.email
    },
    isAdmin(state) {
      return state.role === 'admin'
    }
  },

  actions: {
    async login(payload: AuthForm) {
      try {
        const {
          token,
          user: { email, role }
        } = await authRepository.login(payload)
        this.$patch({
          role,
          email,
          accessToken: token.access_token,
          refreshToken: token.refresh_token
        })
        return true
      } catch (err) {
        return false
      }
    },
    async setRefreshedTokens(token: any) {
      try {
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
