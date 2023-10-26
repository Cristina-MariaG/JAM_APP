import { flushPromises, mount } from '@vue/test-utils'
import { expect, describe, vi, it } from 'vitest'
import OrderByPrice from '@/components/filterComponents/OrderByPriceComponent.vue'
import useFilters from '@/composables/filters'
import { useI18n } from 'vue-i18n'

vi.mock('vue-i18n', () => ({
  useI18n: () => ({
    t: (key: string) => key
  })
}))

const doMount = () => {
  return mount(OrderByPrice)
}

describe('OrderByPrice', () => {
  it('initializes data correctly', async () => {
    const wrapper = doMount()
    await flushPromises()
    await wrapper.vm.$nextTick()

    const labelElem = wrapper.findAll('.v-label.v-field-label')
    expect(labelElem[0].text()).toBe('')

    let inputText = wrapper.find('#input-0')
    let title = wrapper.find('#title')

    expect(title.text()).toBe('filters.orderByPrice')
    expect(inputText.element.value).toBe('filters.select')
  })

  it('change select value', async () => {
    const wrapper = doMount()

    await flushPromises()
    await wrapper.vm.$nextTick()
    let inputText = wrapper.find('#input-0')
    expect(inputText.element.value).toBe('filters.select')

    await inputText.setValue('Ascending')
    await wrapper.vm.$nextTick()

    expect(inputText.element.value).toBe('Ascending')
  })
})
