import { authRepository } from '@/helpers/api'
import type { AuthForm } from '@/types/auth.types'
import { defineStore } from 'pinia'

interface UserStoreState {
  accessToken: string
  email: string
  failedCount: number
}

export const useAuthStore = defineStore('auth', {
  state: (): UserStoreState => ({
    accessToken: '',
    email: '',
    failedCount: 0
  }),

  getters: {
    isAuth(state) {
      return state.accessToken !== ''
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
          accessToken,
          user: { email }
        } = await authRepository.login(payload)
        // this.accessToken = accessToken
        console.log('email', email)
        this.$patch({ accessToken })
        console.log(email, 'user')
        this.$patch({ email })
        return true
      } catch (err) {
        this.failedCount++
        return false
      }
    },
    async signup(payload: AuthForm) {
      try {
        const { accessToken } = await authRepository.signup(payload)
        // this.accessToken = accessToken
        this.$patch({ accessToken })
        return true
      } catch (err) {
        this.failedCount++
        return false
      }
    },
    async logout() {
      try {
        this.$reset()
        return true
      } catch (err) {
        this.failedCount++
        return false
      }
    }
  }
})
