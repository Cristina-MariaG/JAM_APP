import { defineStore } from 'pinia'
import { type ProductCart } from '@/types/cart.types'

interface CartStoreState {
  cart: ProductCart[]
  cartProductsNumber: number
}

export const useCartStore = defineStore('cart', {
  state: (): CartStoreState => ({
    cart: [],
    cartProductsNumber: 0
  }),

  getters: {
    getCart(state) {
      return state.cart
    },
    productsNumber(state) {
      return state.cart.length
    }
  },

  actions: {
    addToCart(product: ProductCart) {
      // Ajoutez le produit au panier
      const productIndex = this.cart.findIndex((prod) => product.id === prod.id)

      if (productIndex !== -1) {
        // Si le produit existe, remplacez-le par les nouvelles valeurs
        this.cart.splice(productIndex, 1, product)
      } else {
        this.cart.push(product)
        this.cartProductsNumber = this.cart.length
      }

      // Mettez à jour le nombre de produits dans le panier
    }
  },
  persist: true
})
