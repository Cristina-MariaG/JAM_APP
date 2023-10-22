import { Axios, type AxiosResponse } from 'axios'

import type { OrderData } from '@/types/order.types'

export class StripeRepository {
  constructor(private axios: Axios) {}

  async createCheckoutSession(orderData: OrderData) {
    return await this.axios.post<any, AxiosResponse<any, any>, any>(
      '/create-checkout-session/',
      orderData
    )
  }
  async checkoutSuccess(orderId: number) {
    return await this.axios.put<any, AxiosResponse<any, any>, any>('/edit-order/', {
      order_id: orderId
    })
  }
  async refreshToken(refreshToken: string) {
    console.log(refreshToken)
    return await this.axios.post<any, AxiosResponse<any, any>, any>('/refresh-token/', {
      refresh_token: refreshToken
    })
  }
  async checkoutCancel(orderId: number) {
    return await this.axios.delete<any, AxiosResponse<any, any>, any>(`/delete-order/${orderId}`)
  }
}
