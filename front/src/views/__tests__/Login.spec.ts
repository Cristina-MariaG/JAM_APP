import { flushPromises, mount, shallowMount } from '@vue/test-utils'
import { describe, test, vi, beforeEach, expect } from 'vitest'
import LoginViewVue from '../LoginView.vue'
import { useAuthStore } from '@/stores/auth'
import { createTestingPinia } from '@pinia/testing'
import { setActivePinia, createPinia } from 'pinia'
import Swal from 'sweetalert2'
import { useI18n } from 'vue-i18n'
import { useValidationRules } from '@/composables/validateForm'
import { RouterLinkStub } from '@vue/test-utils'
import { RouterLink } from 'vue-router'

vi.mock('vue-i18n', () => ({
  useI18n: () => ({
    t: (key: string) => key
  })
}))

vi.mock('vue-router')

const doMount = () => {
  return mount(LoginViewVue, {
    global: {
      plugins: [
        createTestingPinia({
          initialState: {
            stubActions: false,
            auth: { accessToken: '', refreshToken: '', email: '', role: '' }
          }
        })
      ]
    },
    stubs: {
      RouterLink: RouterLinkStub
    }
  })
}

describe('test login', () => {
  let store
  beforeEach(() => {
    setActivePinia(createPinia())
    store = useAuthStore()
  })
  test('mount Page login', async () => {
    const wrapper = doMount()

    await flushPromises()
    await wrapper.vm.$nextTick()

    console.log(wrapper.html())
  })
  test('show elements', async () => {
    const wrapper = doMount()

    await flushPromises()
    await wrapper.vm.$nextTick()

    let title = wrapper.find('h1')

    expect(title.text()).toBe('login.login')

    let inputElements = wrapper.findAll('input')
    expect(inputElements.length).toBe(2)

    let buttonSubmit = wrapper.find('#submit')

    expect(buttonSubmit.element.disabled).toBe(true)
  })
  test('set inputs elements', async () => {
    const wrapper = doMount()

    await flushPromises()
    await wrapper.vm.$nextTick()

    let inputElements = wrapper.findAll('input')
    expect(inputElements.length).toBe(2)
    let email = 'arcusi_cristina@yahoo.com'
    await inputElements[0].setValue(email)

    expect(inputElements[0].element.value).toBe(email)

    let password = 'testForPassword'
    await inputElements[1].setValue(password)

    expect(inputElements[1].element.value).toBe(password)

    let buttonSubmit = wrapper.find('#submit')

    expect(buttonSubmit.element.disabled).toBe(false)
  })

  test('test router link', async () => {
    const wrapper = shallowMount(LoginViewVue, {
      global: {
        plugins: [
          createTestingPinia({
            initialState: {
              stubActions: false,
              auth: { accessToken: '', refreshToken: '', email: '', role: '' }
            }
          })
        ]
      },
      stubs: {
        RouterLink: RouterLinkStub
      }
    })
    let routerLink = wrapper.find('.routerLink')

    expect(routerLink.text()).toBe('login.inscription')
    routerLink.trigger('click')
    
  })

  test('set inputs elements', async () => {
    const wrapper = doMount()
    const handleSubmitSpy = vi.spyOn(wrapper.vm, 'handleSubmit')

    await flushPromises()
    await wrapper.vm.$nextTick()

    let inputElements = wrapper.findAll('input')
    expect(inputElements.length).toBe(2)
    let email = 'arcusi_cristina@yahoo.com'
    await inputElements[0].setValue(email)

    expect(inputElements[0].element.value).toBe(email)

    let password = 'testForPassword'
    await inputElements[1].setValue(password)

    expect(inputElements[1].element.value).toBe(password)
    let buttonSubmit = wrapper.find('#submit')

    expect(buttonSubmit.element.disabled).toBe(false)

    await buttonSubmit.trigger('click')

    expect(handleSubmitSpy).toHaveBeenCalledTimes(1)
  })
})
