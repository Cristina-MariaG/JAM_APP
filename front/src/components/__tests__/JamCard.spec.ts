import { mount, flushPromises } from '@vue/test-utils'
import { expect, describe, vi, test, beforeEach, it } from 'vitest'
import JamCardVue from '../JamCard.vue'
import { setActivePinia, createPinia } from 'pinia'
import { useCartStore } from '@/stores/cart'
import { createTestingPinia } from '@pinia/testing'
import type { VueWrapper } from '@vue/test-utils'
import { useRouter } from 'vue-router'

const product = {
  id: 1,
  name: 'Product Name',
  description: 'Product Description',
  image: 'product_image.jpg',
  price: 10.99,
  flavor: {
    id: 1,
    flavor: 'Product Flavor'
  },
  type_contenant: {
    id: 1,
    type_contenant: 'Product Type'
  },
  brand: {
    id: 1,
    brand: 'Product Brand'
  },
  promotion: 5,
  stock_disponible: {
    id: 1,
    stock_disponible: 'In Stock'
  },
  category: {
    id: 1,
    category: 'Product Category'
  },
  quantity: 100,
  ingredients: [
    {
      id: 1,
      ingredient: {
        id: 1,
        ingredient: 'Ingredient 1'
      },
      quantity: 2,
      product: 1
    },
    {
      id: 2,
      ingredient: {
        id: 2,
        ingredient: 'Ingredient 2'
      },
      quantity: 3,
      product: 1
    }
  ]
}

vi.mock('vue-router')

useRouter.mockReturnValue({
  push: vi.fn()
})

let wrapper: VueWrapper
const doMount = async (params = {}) => {
  wrapper = mount(JamCardVue, {
    ...params,
    global: {
      plugins: [
        createTestingPinia({
          initialState: {
            stubActions: false,
            cart: { cart: [], cartProductsNumber: 0, orderId: -1 } 
          }
        })
      ]
    },
    stubs: ['router-link', 'router-view']
  })
}

describe('YourComponent', () => {
  useRouter.mockReturnValue({
    push: vi.fn()
  })

  beforeEach(() => {
    // creates a fresh pinia and makes it active
    // so it's automatically picked up by any useStore() call
    // without having to pass it to it: `useStore(pinia)`
    setActivePinia(createPinia())
    const cartStore = useCartStore()
    useRouter().push.mockReset()
  })
  
  test('should display product details correctly', async () => {
    doMount({
      props: {
        product: product
      }
    })

    // Test if the product name and price are rendered correctly
    const titles = wrapper.findAll('.ms-5')

    expect(titles[0].text()).toContain(product.name)

    expect(titles[1].text()).toContain(`${product.price} €`)

    // Test if the image source is set correctly
    expect(wrapper.find('img').attributes('src')).toContain(`/uploads/${product.image}`)

    // Test if the quantity options are displayed in the select component
    const quantityOptions = wrapper.vm.quantityOptions
    const selectComponent = wrapper.findComponent({ name: 'v-select' })
    expect(selectComponent.props().items).toEqual(quantityOptions)

    // Simulate button click and test if the addToCart method is called
    await wrapper.find('button').trigger('click')
    expect(wrapper.vm.cartStore.addToCart).toHaveBeenCalled()

    let details = await wrapper.find('#product-detail')

    details.trigger('click')
    await flushPromises()
    expect(useRouter().push).toHaveBeenCalledTimes(1)
  })
})
