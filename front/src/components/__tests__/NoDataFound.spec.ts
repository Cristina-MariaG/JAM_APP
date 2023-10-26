import { describe, it, expect, test } from 'vitest'
import { mount } from '@vue/test-utils'

import NoDataFound from '../NoDataFound.vue'

describe('NoDataFound', () => {
  test('renders properly', () => {
    const wrapper = mount(NoDataFound)
    expect(wrapper.text()).toContain('noDataFound')
  })
})
