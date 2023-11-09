import { flushPromises, mount } from '@vue/test-utils'
import { createTestingPinia } from '@pinia/testing'
import { describe, test, vi, beforeEach, afterEach, expect } from 'vitest'
import Header from '../common/Header.vue'
let mockCreated = vi.fn()
let wrapper

const doMount = (params = {}, createdIsMocked = true) => {
  //   if (createdIsMocked) {
  //     mockCreated = vi.spyOn(Header, 'created').mockImplementation(() => {})
  //   }

  wrapper = mount(Header, {
    ...params,
    global: {
      plugins: [
        createTestingPinia({
          initialState: { accessToken: '', email: '', refreshToken: '' }
        })
      ],
      stubs: ['router-link']
    }
  })
}

// afterEach(() => {
//   mockCreated.mockRestore()
//   vi.clearAllMocks()
// })

describe('Methods', () => {
  test('getProjects (success) - send get request & then update projects with response data & finally hide loader', async () => {
    wrapper =doMount()
   expect(wrapper.exists()).toBe(true)
    console.log(wrapper.html())
  })
})
