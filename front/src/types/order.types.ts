import type { ProductCart } from './cart.types'

export interface OrderData {
  token: string
  cart: ProductCart[]
  total: number
}
