import axios from 'axios'
// import { FeatureRepository } from './repositories/Feature.repository'
import { AuthRepository } from './repositories/Auth.repository'

const http = axios.create({
  baseURL: 'http://localhost:8213'
})

export function setAuthToken(token: string): void {
  http.defaults.headers.common.Authorization = `Bearer ${token}`
}

// export const featureRepository = new FeatureRepository(http)
export const authRepository = new AuthRepository(http)
