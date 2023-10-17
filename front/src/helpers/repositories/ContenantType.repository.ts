import { Axios, type AxiosResponse } from 'axios'
import { repositoryErrorHandler } from '../error-handler'

export class ContenantTypeRepository {
  constructor(private axios: Axios) {}

  async getContenantTypes() {
    try {
      const { data } = await this.axios.get<any, AxiosResponse<any, any>, any>('/contenant-type/')
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      console.error('Recuperation failed:', errorMessage)
      throw errorMessage
    }
  }
}
