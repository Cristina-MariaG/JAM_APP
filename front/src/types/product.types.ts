export interface Product {
  id: number
  name: string
  description: string | null
  image: string
  price: number
  flavor: number // Remplacez par le type approprié pour Flavor
  type_contenant: number // Remplacez par le type approprié pour TypeContenant
  brand: number // Remplacez par le type approprié pour Brand
  promotion: number
  stock_disponible: number // Remplacez par le type approprié pour StockDisponible
  category: number // Remplacez par le type approprié pour Category
  quantity: number
  ingredients: ProductIngredient[]
}

export interface ProductIngredient {
  id: number
  ingredient: Ingredient // Remplacez par le type approprié pour Ingredient
  quantity: number
}

export interface Ingredient {
  id: number
  ingredient: string
}
export interface ProductsData {
  products: Product[]
}
