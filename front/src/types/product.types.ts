export interface Product {
  id: number
  name: string
  description: string
  image: string
  price: number
  flavor: number
  type_contenant: number
  brand: number
  promotion: number
  stock_disponible: number
  category: number
  quantity: number
  ingredients: ProductIngredient[]
}

export interface ProductIngredient {
  id: number
  ingredient: Ingredient
  quantity: number
}

export interface Ingredient {
  id: number
  ingredient: string
}

export interface ProductsData {
  products: Product[]
}
