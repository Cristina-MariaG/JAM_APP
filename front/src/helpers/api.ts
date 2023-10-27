import axios from 'axios'
import { ProductRepository } from './repositories/Product.repository'
import { AuthRepository } from './repositories/Auth.repository'
import { FilteringRepository } from './repositories/Filtering.repository'
import { StripeRepository } from './repositories/Stripe.repository'
import { ContenantTypeRepository } from './repositories/ContenantType.repository'
import { BrandRepository } from './repositories/Brand.repository'
import { CategoryRepository } from './repositories/Category.repository'
import { FlavorRepository } from './repositories/Flavor.repository'
import { IngredientRepository } from './repositories/Ingredient.repository'

const http = axios.create({
  baseURL: 'http://localhost:8213'
})

export const productRepository = new ProductRepository(http)
export const contenantTypeRepository = new ContenantTypeRepository(http)
export const categoryRepository = new CategoryRepository(http)
export const brandRepository = new BrandRepository(http)
export const flavorRepository = new FlavorRepository(http)
export const ingredientRepository = new IngredientRepository(http)
export const filteringDataRepository = new FilteringRepository(http)
export const authRepository = new AuthRepository(http)
export const stripeRepository = new StripeRepository(http)
