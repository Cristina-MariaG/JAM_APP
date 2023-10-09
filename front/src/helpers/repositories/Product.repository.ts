import { Axios } from 'axios'
import { repositoryErrorHandler } from '../error-handler'
import type { Product, ProductsData } from '@/types/product.types'

export class ProductRepository {
  constructor(private axios: Axios) {}

  async getAllProducts() {
    try {
      // const { data } = await this.axios.get<any, AxiosResponse<any, any>, any>('/products/')
      const { data } = await this.axios.get<ProductsData>('/product/')
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      console.error('Recuperation failed:', errorMessage)
      throw errorMessage
    }
  }
  async getProductWithId(id: string) {
    try {
      // const { data } = await this.axios.get<any, AxiosResponse<any, any>, any>('/products/')
      const { data } = await this.axios.get<Product>(`/product/${id}`)
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      console.error('Recuperation failed:', errorMessage)
      throw errorMessage
    }
  }
}
