import { Axios, type AxiosResponse } from 'axios'
import { repositoryErrorHandler } from '../error-handler'

export class BrandRepository {
  constructor(private axios: Axios) {}

  async getBrands() {
    try {
      const { data } = await this.axios.get<any, AxiosResponse<any, any>, any>('/brand/')
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      throw errorMessage
    }
  }
}
