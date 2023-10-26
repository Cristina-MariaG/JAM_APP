import { mount } from '@vue/test-utils'
import HrComponent from '../HrComponent.vue'
import { expect, describe, it } from 'vitest'
import { hr } from 'vuetify/locale'

describe('HrComponent', () => {
    it('should render a gray line with the specified styles', () => {
        const wrapper = mount(HrComponent)
        
    const hrElement = wrapper.find('hr')
    // Vérifiez si la balise hr est rendue
    expect(hrElement.exists()).toBe(true)

    // Vérifiez si la classe gray-line est appliquée à la balise hr
    expect(wrapper.find('hr').classes()).toContain('gray-line')

  })
})
