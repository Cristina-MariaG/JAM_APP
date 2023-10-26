import useFilters from '@/composables/filters'
import { brandRepository } from '@/helpers/api'
import { mount, flushPromises } from '@vue/test-utils'
import { expect, describe, vi, test } from 'vitest'
import type { VueWrapper } from '@vue/test-utils'
import BrandVue from '@/components/filterComponents/Brand.vue'

const mock = vi.hoisted(() => {
  return {
    useFilters: vi.fn().mockReturnValue({
      setbrandList: vi.fn()
    })
  }
})

vi.mock('../../composables/filters', () => ({
  useFilters: mock.useFilters
}))

vi.mock('@/helpers/api', () => ({
  brandRepository: {
    getBrands: vi.fn().mockResolvedValue({
      brand_list: [
        { id: 1, brand: 'test brand 1' },
        { id: 2, brand: 'test brand 2' }
      ]
    })
  }
}))

let wrapper: VueWrapper
const doMount = async (params = {}) => {
  wrapper = mount(BrandVue, {
    ...params
  })
}

describe('Brand List', () => {
  test('should display Brand list correctly', async () => {
    doMount({})

    await flushPromises()
    await wrapper.vm.$nextTick()
    let labelsElements = wrapper.findAll('.v-label.v-label--clickable')

    expect(labelsElements.length).toBe(2)
    expect(labelsElements[0].text()).toBe('test brand 1')
    expect(labelsElements[1].text()).toBe('test brand 2')
  })

  test('should change checkbox values on click', async () => {
    doMount({})

    await flushPromises()
    await wrapper.vm.$nextTick()
    const checkboxElements = wrapper.findAll('input[type="checkbox"]')

    checkboxElements[1].trigger('click')

    expect(checkboxElements[1].element.checked).toBeTruthy()
    expect(checkboxElements[0].element.checked).toBeFalsy()
  })
})
