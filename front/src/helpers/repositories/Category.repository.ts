import { Axios, type AxiosResponse } from 'axios'
import { repositoryErrorHandler } from '../error-handler'

export class CategoryRepository {
  constructor(private axios: Axios) {}

  async getCategories() {
    try {
      // const { data } = await this.axios.get<any, AxiosResponse<any, any>, any>('/products/')
      const { data } = await this.axios.get<any, AxiosResponse<any, any>, any>('/category/')
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      console.error('Recuperation failed:', errorMessage)
      throw errorMessage
    }
  }
}
