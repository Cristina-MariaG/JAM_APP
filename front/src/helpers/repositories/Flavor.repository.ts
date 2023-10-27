import { Axios, type AxiosResponse } from 'axios'
import { repositoryErrorHandler } from '../error-handler'

export class FlavorRepository {
  constructor(private axios: Axios) {}

  async getFlavors() {
    try {
      const { data } = await this.axios.get<any, AxiosResponse<any, any>, any>('/flavor/')
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      console.error('Recuperation failed:', errorMessage)
      throw errorMessage
    }
  }
}
