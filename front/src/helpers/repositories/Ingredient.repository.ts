import { Axios, type AxiosResponse } from 'axios'
import { repositoryErrorHandler } from '../error-handler'

export class IngredientRepository {
  constructor(private axios: Axios) {}

  async getIngredients() {
    try {
      const { data } = await this.axios.get<any, AxiosResponse<any, any>, any>('/ingredient/')
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      throw errorMessage
    }
  }
}
