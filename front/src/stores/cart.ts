import { defineStore } from 'pinia'
import type { ProductCart } from '@/types/cart.types'

interface CartStoreState {
  cart: ProductCart[]
  cartProductsNumber: number
  orderId: number
}

export const useCartStore = defineStore('cart', {
  state: (): CartStoreState => ({
    cart: [],
    cartProductsNumber: 0,
    orderId: -1
  }),

  getters: {
    getCart(state) {
      return state.cart
    },
    productsNumber(state) {
      return state.cart.length
    },
    totalPrice(state) {
      let total = 0
      state.cart.forEach((product) => {
        total += product.price * product.selectedQuantity
      })
      return total
    },
    getOrderId(state) {
      return state.orderId
    }
  },

  actions: {
    addToCart(product: ProductCart) {
      const productIndex = this.cart.findIndex((prod) => product.id === prod.id)

      if (productIndex !== -1) {
        this.cart.splice(productIndex, 1, product)
      } else {
        this.cart.push(product)
        this.cartProductsNumber = this.cart.length
      }
    },
    setWaitingPaymentOrderId(id: number) {
      if (id > 0) {
        this.orderId = id
      }
    },
    productIsAlreadyInTheCart(idRecherche: number) {
      let alreadyInCart = false
      if (this.cart.some((objet) => objet.id === idRecherche)) alreadyInCart = true
      return alreadyInCart
    },
    quantitySelected(idRecherche: number) {
      let quantity = 1
      const product = this.cart.find((produit) => produit.id === idRecherche)

      if (product && product.selectedQuantity) {
        quantity = product.selectedQuantity
      }

      return quantity
    },

    resetStore() {
      this.$reset()
    },
    resetOrderId() {
      this.orderId = -1
    }
  },
  persist: true
})
