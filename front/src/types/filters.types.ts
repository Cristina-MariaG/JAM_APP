export interface PriceRange {
  minPrice: number
  maxPrice: number
}

export interface FiltersStoreState {
  minPrice: number
  maxPrice: number
  minPriceUser: number
  maxPriceUser: number
  searchedText: string
  categories: number[]
  promotion: Boolean | null
  flavor: string
  stockDisponible: Boolean | null
  typeContenant: string
  brand: string[]
  ordonateByPrice: string | null
  chosenFilters: string[]
}
