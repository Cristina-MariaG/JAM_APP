import { mount, flushPromises } from '@vue/test-utils'
import { expect, describe, vi, test, beforeEach, it } from 'vitest'
import useFilters from '@/composables/filters'
import type { VueWrapper } from '@vue/test-utils'
import AvailableStock from '@/components/filterComponents/AvailableStock.vue'

const mock = vi.hoisted(() => {
  return {
    useFilters: vi.fn().mockReturnValue({
      setAvailableStock: vi.fn()
    })
  }
})

vi.mock('../../composables/filters', () => ({
  useFilters: mock.useFilters
}))

let wrapper: VueWrapper
const doMount = async (params = {}) => {
  wrapper = mount(AvailableStock, {
    ...params
  })
}

test('should display product details correctly', async () => {
  doMount({})

  expect(wrapper.text()).toContain('filters.onlyAvailableStock')
  const switchElement = wrapper.find('input[type="checkbox"]')
  expect(switchElement.element.checked).toBe(false)

  await switchElement.trigger('click')

  expect(switchElement.element.checked).toBe(true)

})
