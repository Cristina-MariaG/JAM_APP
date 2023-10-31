import { flushPromises, mount } from '@vue/test-utils'
import { createTestingPinia } from '@pinia/testing'
import { describe, test, vi, beforeEach, afterEach } from 'vitest'
import Header from '../Header.vue'
import { createLocalVue } from '@vue/test-utils'

let mockCreated = vi.fn()
let wrapper

const doMount = (params = {}, createdIsMocked = true) => {
  //   if (createdIsMocked) {
  //     mockCreated = vi.spyOn(Header, 'created').mockImplementation(() => {})
  //   }

  wrapper = mount(Header, {
    ...params,
    localVue,
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
    doMount()

    console.log(wrapper.html())
  })
})
