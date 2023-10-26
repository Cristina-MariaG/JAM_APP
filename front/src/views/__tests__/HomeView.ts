// import JamCard from '@/components/JamCard.vue'
// import NoDataFound from '@/components/NoDataFound.vue'
// import HomeViewVue from '../HomeView.vue'
// import { flushPromises, mount, shallowMount } from '@vue/test-utils'
// import { describe, test, vi, beforeEach, expect } from 'vitest'

// import { productRepository, filteringDataRepository } from '@/helpers/api'
// // import {  } from '@/helpers/api'
// import useFilters from '@/composables/filters'



// vi.mock('@/helpers/api', () => ({
//     productRepository: {
//       getAllProducts: vi.fn().mockResolvedValue({
//         products: [],
//         pages_number: 0
//       })
//     },
//   filteringDataRepository: {
//     getProductsFiltered: vi.fn().mockResolvedValue({
//       products: [],
//       pages_number: 0
//     })
//   },
// }))

// const doMount = () => {
//   return mount(HomeViewVue, {
//     global: {}
//   })
// }

// describe('ContenantTypeComponenet', () => {
//   test('initializes data correctly', async () => {
//     const wrapper = doMount()
//     await flushPromises()
//     await wrapper.vm.$nextTick()
//     console.log(wrapper.html())
//   })
// })
