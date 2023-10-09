import axios from 'axios'
import { ProductRepository } from './repositories/Product.repository'
import { AuthRepository } from './repositories/Auth.repository'

const http = axios.create({
  baseURL: 'http://localhost:8213'
})

// export function setAuthToken(token: string): void {
//   http.defaults.headers.common.Authorization = `Bearer ${token}`
// }

export const productRepository = new ProductRepository(http)
export const authRepository = new AuthRepository(http)
