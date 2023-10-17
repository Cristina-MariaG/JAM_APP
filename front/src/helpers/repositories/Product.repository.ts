import { Axios } from 'axios'
import { repositoryErrorHandler } from '../error-handler'
import type { Product } from '@/types/product.types'

export class ProductRepository {
  constructor(private axios: Axios) {}

  async getAllProducts() {
    try {
      const { data } = await this.axios.get<{ products: Product[]; pages_number: number }>(
        '/product/'
      )
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      console.error('Recuperation failed:', errorMessage)
      throw errorMessage
    }
  }

  async getProductWithId(id: string) {
    try {
      const { data } = await this.axios.get<{ product: Product }>(`/product/${id}`)
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      console.error('Recuperation failed:', errorMessage)
      throw errorMessage
    }
  }

  async getMinMAx() {
    try {
      const { data } = await this.axios.get(`/prices-min-max/`)
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      console.error('Recuperation failed:', errorMessage)
      throw errorMessage
    }
  }
}
