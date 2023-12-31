import { Axios, type AxiosResponse } from 'axios'
import { repositoryErrorHandler } from '../error-handler'
import type { FiltersStoreState } from '@/types/filters.types'

export class FilteringRepository {
  constructor(private axios: Axios) {}

  async getProductsFiltered(filters: FiltersStoreState, pageNumber = 0) {
    try {
      let paramsList: { [key: string]: any } = {}

      filters.chosenFilters.forEach((filter) => {
        paramsList[filter] = filters[filter]
      })
      paramsList.page = pageNumber
      const { data } = await this.axios.get<any, AxiosResponse<any, any>>('/filter/', {
        params: paramsList
      })
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      throw errorMessage
    }
  }
  async getAllLike(searched: string) {
    try {
      const { data } = await this.axios.get<any, AxiosResponse<any, any>>('/filter/', {
        params: { searchedText: searched }
      })
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      // console.error('Récupération échouée :', errorMessage)
      throw errorMessage
    }
  }
}
