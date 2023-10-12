import { Axios, type AxiosResponse } from 'axios'
import { repositoryErrorHandler } from '../error-handler'
import type { ProductCart } from '@/types/cart.types'
import Swal from 'sweetalert2'
import type { OrderData } from '@/types/order.types'

export class StripeRepository {
  constructor(private axios: Axios) {}

  async createCheckoutSession(orderData: OrderData) {
    try {
      const { data } = await this.axios.post<any, AxiosResponse<any, any>, any>(
        '/create-checkout-session/',
        orderData
      )
      console.log('order', data)
      return data
    } catch (error: any) {
      const errorMessage = repositoryErrorHandler(error)
      Swal.fire({
        icon: 'error',
        title: errorMessage.message
      })
    }
  }
  async checkoutSuccess(orderId: number) {
    return await this.axios.post<any, AxiosResponse<any, any>, any>('/checkout-success/', {
      order_id: orderId
    })
  }
}
