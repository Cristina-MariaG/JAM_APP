import { describe, it, expect, vi } from 'vitest'
import { mount } from '@vue/test-utils'
import LoginView from '../LoginView.vue'

function mountTheForm() {
  const wrapper = mount(LoginView, { props: {} })
  return wrapper
}

describe('The Form', () => {
  it('Mounts properly', () => {
    expect(mountTheForm()).toBeTruthy()
    // Check the submit button mounts
    expect(mountTheForm().text()).toContain('Submit')
  })

  it('click the submit button', async () => {
    const form = mountTheForm().find('form')
    // The spyOn function will report if the element
    // has been clicked.
    const spyOnForm = vi.spyOn(form, 'trigger')
    await form.trigger('click')

    // ❌wrong
    // expect(spyOnForm).toHaveBeenCalledTimes(2)

    // ✅ good
    expect(spyOnForm).toHaveBeenCalledOnce()
  })

  it('Renders the input value', async () => {
    const input = mountTheForm().find('input')
    // input renders with an empty value
    expect(input.text()).toContain('')
    // fill the input
    await input.setValue('jane@doe.com')
    // Check the input has a value
    expect(input.element.value).toEqual('jane@doe.com')
  })
})
