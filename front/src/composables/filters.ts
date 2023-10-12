import type { FiltersStoreState, PriceRange } from '@/types/filters.types'
import type { Product } from '@/types/product.types'
import { reactive } from 'vue'

const state = reactive<FiltersStoreState>({
  minPrice: 0,
  maxPrice: 0,
  minPriceUser: 0,
  maxPriceUser: 0,
  searchedText: '',
  categories: [],
  promotion: null,
  flavor: '',
  stockDisponible: null,
  typeContenant: '',
  brand: [],
  ordonateByPrice: 'false',
  chosenFilters: []
})

function useFilters() {
  const setMinPrice = (value: number) => {
    state.minPrice = value
  }
  const setMaxPrice = (value: number) => {
    state.maxPrice = value
  }
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
  }
  const setCategoriesSearched = (value: number[]) => {
    state.categories = value
    if (!state.chosenFilters.includes('categories')) state.chosenFilters.push('categories')
  }
  const setPromotion = (value: Boolean) => {
    state.promotion = value
  }
  const setFlavour = (value: string) => {
    state.flavor = value
  }
  const setStockDisponible = (value: Boolean) => {
    state.stockDisponible = value
  }
  const setTypeContenant = (value: string) => {
    state.typeContenant = value
  }
  const setBrand = (value: string) => {
    state.brand.push(value)
  }
  const setOrdonateByPrice = (value: string) => {
    state.ordonateByPrice = value

    //   state.chosenFilters = state.chosenFilters.filter((item) => item !== 'ordonateByPrice')
    // } else {
    state.chosenFilters.push('ordonateByPrice')
    // }
  }

  const findMinMaxPrices = (products: Product[]) => {
    if (products.length === 0) {
      setMaxPrice(0)
      setMinPrice(0)
      return
    }

    const initialPrices: PriceRange = {
      minPrice: products[0].price,
      maxPrice: products[0].price
    }

    const { minPrice: min, maxPrice: max } = products.reduce(
      (prices: PriceRange, product: Product) => {
        return {
          minPrice: Math.min(prices.minPrice, product.price),
          maxPrice: Math.max(prices.maxPrice, product.price)
        }
      },
      initialPrices
    )

    setMinPrice(min)
    setMaxPrice(max)

    // setMinPriceUser(min)
    // setMaxPriceUser(max)
  }

  return {
    state,
    setMinPrice,
    setMaxPrice,
    findMinMaxPrices,
    setMaxPriceUser,
    setMinPriceUser,
    setSearchedText,
    setBrand,
    setCategoriesSearched,
    setFlavour,
    setOrdonateByPrice,
    setPromotion,
    setStockDisponible,
    setTypeContenant
    // ref, reactive, methods, computed
  }
}

export default useFilters
