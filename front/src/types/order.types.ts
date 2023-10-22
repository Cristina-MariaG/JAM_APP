import type { ProductCart } from './cart.types'

export interface OrderData {
  accessToken: string
  cart: ProductCart[]
  total: number
}
