import { authRepository } from '@/helpers/api'
import type { AuthForm } from '@/types/auth.types'
import { defineStore } from 'pinia'

interface UserStoreState {
  token: string
  email: string
  token: string
}

export const useAuthStore = defineStore('auth', {
  state: (): UserStoreState => ({
    token: '',
    email: ''
  }),

  getters: {
    isAuth(state) {
      return state.token !== ''
    },
    getToken(state) {
      return state.token
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

        console.log(token)
        this.$patch({ email, token })
        return true
      } catch (err) {
        return false
      }
    },
    async signup(payload: AuthForm) {
      try {
        await authRepository.signup(payload)

        return true
      } catch (err) {
        return false
      }
    },
    async logout() {
      try {
        this.$reset()
        return true
      } catch (err) {
        return false
      }
    }
  },
  persist: true
})
