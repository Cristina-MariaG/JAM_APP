import { useCartStore } from '../cart'
import { expect, describe, it, beforeEach } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'

describe('useCartStore', () => {
  let cartStore: any

  beforeEach(() => {
    setActivePinia(createPinia())
    cartStore = useCartStore()
  })

  it('checks initial state values', () => {
    expect(cartStore.cart).toEqual([])
    expect(cartStore.cartProductsNumber).toBe(0)
    expect(cartStore.orderId).toBe(-1)
  })

  it('checks addToCart action', () => {
    const product1 = { id: 1, name: 'Product 1', price: 10, selectedQuantity: 2 }
    const product2 = { id: 2, name: 'Product 2', price: 15, selectedQuantity: 1 }

    cartStore.addToCart(product1)
    expect(cartStore.cart).toContainEqual(product1)
    expect(cartStore.cartProductsNumber).toBe(1)

    cartStore.addToCart(product2)
    expect(cartStore.cart).toContainEqual(product2)
    expect(cartStore.cartProductsNumber).toBe(2)

    product1.selectedQuantity = 3
    cartStore.addToCart(product1)
    expect(cartStore.cart).toContainEqual(product1)
    expect(cartStore.cartProductsNumber).toBe(2) // Should not increase the number of products
  })

  it('checks setWaitingPaymentOrderId action', () => {
    cartStore.setWaitingPaymentOrderId(5)
    expect(cartStore.orderId).toBe(5)

    cartStore.setWaitingPaymentOrderId(0) // Should not set orderId to 0
    expect(cartStore.orderId).toBe(5)
  })

  it('checks productIsAlreadyInTheCart action', () => {
    const product = { id: 1, name: 'Product 1', price: 10, selectedQuantity: 2 }
    cartStore.addToCart(product)

    expect(cartStore.productIsAlreadyInTheCart(1)).toBe(true)
    expect(cartStore.productIsAlreadyInTheCart(2)).toBe(false)
  })

  it('checks quantitySelected action', () => {
    const product = { id: 1, name: 'Product 1', price: 10, selectedQuantity: 2 }
    cartStore.addToCart(product)

    expect(cartStore.quantitySelected(1)).toBe(2)
    expect(cartStore.quantitySelected(2)).toBe(1)
  })

  it('checks resetOrderId action', () => {
    cartStore.setWaitingPaymentOrderId(5)
    expect(cartStore.orderId).toBe(5)

    cartStore.resetOrderId()
    expect(cartStore.orderId).toBe(-1)
  })

  it('checks resetStore action', () => {
    cartStore.addToCart({ id: 1, name: 'Product 1', price: 10, selectedQuantity: 2 })
    cartStore.setWaitingPaymentOrderId(5)

    cartStore.resetStore()
    expect(cartStore.cart).toEqual([])
    expect(cartStore.cartProductsNumber).toBe(0)
    expect(cartStore.orderId).toBe(-1)
  })

  it('checks totalPrice getter', () => {
    cartStore.addToCart({ id: 1, name: 'Product 1', price: 10, selectedQuantity: 2 })
    cartStore.addToCart({ id: 2, name: 'Product 2', price: 15, selectedQuantity: 1 })

    expect(cartStore.totalPrice).toBe(35) // 10*2 + 15*1
  })
})
