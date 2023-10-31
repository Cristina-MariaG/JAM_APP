import { mount } from '@vue/test-utils'
import { describe, test, vi, beforeEach } from 'vitest'
import LoginViewVue from '../LoginView.vue'
import { useAuthStore } from '@/stores/auth'
import { setActivePinia, createPinia } from 'pinia'

const $router = {
  push: vi.fn()
}

const doMount = (params: any) => {
  return mount(LoginViewVue, {
    global: {
      mocks: {
        $route: {
          params
        },
        $router
      }
    }
  })
}


beforeEach(() => {
  setActivePinia(createPinia())
})


describe('test CreateEditStudy.vue', () => {
  test('mount Page Create', async () => {
    const wrapper = doMount({name:"login"})
    const store = useAuthStore()

    // expect(wrapper.exists()).toBe(true)
  })
})
