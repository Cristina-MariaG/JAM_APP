import { Axios, type AxiosResponse } from 'axios'
import { repositoryErrorHandler } from '../error-handler'
import type { FiltersStoreState, PriceRange } from '@/types/filters.types'

export class FilteringRepository {
  constructor(private axios: Axios) {}

  async getCategories() {
    try {
      // const { data } = await this.axios.get<any, AxiosResponse<any, any>, any>('/products/')
      const { data } = await this.axios.get<any, AxiosResponse<any, any>, any>('/category/')
      console.log(data)
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      console.error('Recuperation failed:', errorMessage)
      throw errorMessage
    }
  }
  async getProductsFiltered(filters: FiltersStoreState) {
    try {
      // const { data } = await this.axios.get<any, AxiosResponse<any, any>, any>('/products/')
      let paramsList = {}

      filters.chosenFilters.forEach((filter) => {
        console.log(filter)
        paramsList[filter] = filters[filter]
      })
      console.log(paramsList)

      const { data } = await this.axios.get<any, AxiosResponse<any, any>, any>('/filter/', {
        params: paramsList
      })
      console.log(data)
      return data
    } catch (error) {
      const errorMessage = repositoryErrorHandler(error)
      console.error('Recuperation failed:', errorMessage)
      throw errorMessage
    }
  }
}
