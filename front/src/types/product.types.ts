export interface Product {
  id: number
  name: string
  description: string
  image: string
  price: number
  flavor: Flavor
  type_contenant: TypeContenant
  brand: Brand
  promotion: number
  stock_disponible: StockDisponible
  category: Category
  quantity: number
  ingredients: IngredientOfIngredients[]
}

export interface TypeContenant {
  id: number
  type_contenant: string
}
export interface Flavor {
  id: number
  flavor: string
}
export interface Category {
  id: number
  category: string
}
export interface Ingredient {
  id: number
  ingredient: string
}
export interface IngredientOfIngredients {
  id: number
  ingredient: Ingredient
  quantity: number
  product: number
}
export interface Brand {
  id: number
  brand: string
}
export interface StockDisponible {
  id: number
  stock_disponible: string
}


