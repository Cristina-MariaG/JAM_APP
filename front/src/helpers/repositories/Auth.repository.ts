import type { AuthForm, LoginData } from '@/types/auth.types'
import { Axios, AxiosError, type AxiosResponse } from 'axios'
import { repositoryErrorHandler } from '../error-handler'

export class AuthRepository {
  constructor(private axios: Axios) {}

  async login(payload: AuthForm) {
    try {
      const { data } = await this.axios.post<LoginData>('/login/', payload)
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      throw errorMessage
    }
  }

  async inscription(payload: AuthForm) {
    try {
      await this.axios.post<any, AxiosResponse<any, any>, any>('/inscription/', payload)
      return true
    } catch (error) {
      // Handle errors using the repositoryErrorHandler or other error handling logic
      const errorMessage = repositoryErrorHandler(error)
      throw errorMessage // Optionally, re-throw the error to the caller
    }
  }
}
