import type { AuthForm, LoginData } from '@/types/auth.types'
// import type { FeatureWithId } from '@/types/map.types'
import { Axios, AxiosError } from 'axios'
import { repositoryErrorHandler } from '../error-handler'

export class AuthRepository {
  constructor(private axios: Axios) {}

  async login(payload: AuthForm) {
    const { data } = await this.axios.post<LoginData>('/login/', payload)
    return data
  }
  async signup(payload: AuthForm) {
    const { data } = await this.axios.post<LoginData>('/signup/', payload)
    return data
  }
}
