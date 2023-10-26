import type { FiltersStoreState } from '@/types/filters.types'
import { reactive } from 'vue'

const state = reactive<FiltersStoreState>({
  minPriceUser: 0,
  maxPriceUser: 0,
  searchedText: '',
  categories: [],
  promotion: null,
  flavor: '',
  stockDisponible: null,
  typeContenant: [],
  brandList: [],
  ordonateByPrice: 'false',
  chosenFilters: []
})

function useFilters() {
  const setMinPriceUser = (value: number) => {
    state.minPriceUser = value
    state.chosenFilters.push('minPriceUser')
  }
  const setMaxPriceUser = (value: number) => {
    state.maxPriceUser = value
    state.chosenFilters.push('maxPriceUser')
  }
  const setSearchedText = (value: string) => {
    state.searchedText = value
    state.chosenFilters.push('searchedText')
  }
  const setCategoriesSearched = (value: number[]) => {
    state.categories = value
    if (value.length === 0 && state.chosenFilters.includes('categories')) {
      const index = state.chosenFilters.indexOf('categories')
      if (index > -1) {
        state.chosenFilters.splice(index, 1)
      }
    } else if (!state.chosenFilters.includes('categories')) {
      state.chosenFilters.push('categories')
    }
  }
  const setPromotion = (value: Boolean) => {
    state.promotion = value
  }
  const setFlavour = (value: string) => {
    state.flavor = value
  }
  const setAvailableStock = (value: Boolean) => {
    state.availableStock = value
    state.chosenFilters.push('availableStock')
  }
  const setTypeContenant = (value: string[]) => {
    state.typeContenant = value
    if (value.length === 0 && state.typeContenant.includes('typeContenant')) {
      const index = state.chosenFilters.indexOf('typeContenant')
      if (index > -1) {
        state.chosenFilters.splice(index, 1)
      }
    } else if (!state.chosenFilters.includes('typeContenant')) {
      state.chosenFilters.push('typeContenant')
    }
  }
  const setbrandList = (value: number[]) => {
    state.brandList = value

    if (value.length === 0 && state.typeContenant.includes('brandList')) {
      const index = state.chosenFilters.indexOf('brandList')
      if (index > -1) {
        state.chosenFilters.splice(index, 1)
      }
    } else if (!state.chosenFilters.includes('brandList')) {
      state.chosenFilters.push('brandList')
    }
  }
  const setOrdonateByPrice = (value: string) => {
    state.ordonateByPrice = value

    state.chosenFilters.push('ordonateByPrice')
  }

  return {
    state,
    setMaxPriceUser,
    setMinPriceUser,
    setSearchedText,
    setbrandList,
    setCategoriesSearched,
    setFlavour,
    setOrdonateByPrice,
    setPromotion,
    setAvailableStock,
    setTypeContenant
    // ref, reactive, methods, computed
  }
}

export default useFilters
