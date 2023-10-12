import axios from 'axios'
import { ProductRepository } from './repositories/Product.repository'
import { AuthRepository } from './repositories/Auth.repository'
import { FilteringRepository } from './repositories/Filtering.repository'
import { StripeRepository } from './repositories/Stripe.repository'

const http = axios.create({
  baseURL: 'http://localhost:8213'
})

export const productRepository = new ProductRepository(http)
export const filteringDataRepository = new FilteringRepository(http)
export const authRepository = new AuthRepository(http)
export const stripeRepository = new StripeRepository(http)
