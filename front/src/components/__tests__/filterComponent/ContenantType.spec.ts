import { flushPromises, mount } from '@vue/test-utils'
import { expect, describe, vi, it } from 'vitest'
import ContenantType from '@/components/filterComponents/ContenantType.vue'
import { contenantTypeRepository } from '@/helpers/api'
import useFilters from '@/composables/filters'

const mockContenantTypes = [
  { id: 1, type_contenant: 'Type 1' },
  { id: 2, type_contenant: 'Type 2' }
]
vi.mock('@/helpers/api', () => ({
  contenantTypeRepository: {
    getContenantTypes: vi.fn().mockResolvedValue({
      contenant_types: [
        { id: 1, type_contenant: 'Type 1' },
        { id: 2, type_contenant: 'Type 2' }
      ]
    })
  }
}))
const doMount = () => {
  return mount(ContenantType, {
    global: {}
  })
}

describe('ContenantTypeComponenet', () => {
  it('initializes data correctly', async () => {
    const wrapper = doMount()
    await flushPromises()
    await wrapper.vm.$nextTick()
    let labelsElements = wrapper.findAll('.v-label.v-label--clickable')

    expect(labelsElements.length).toBe(2)
    expect(labelsElements[0].text()).toBe(mockContenantTypes[0].type_contenant)
    expect(labelsElements[1].text()).toBe(mockContenantTypes[1].type_contenant)
    expect(contenantTypeRepository.getContenantTypes).toHaveBeenCalled()
  })

  it('call contenantTypeRepository', async () => {
    const wrapper = doMount()
    await flushPromises()
    await wrapper.vm.$nextTick()
    expect(contenantTypeRepository.getContenantTypes).toHaveBeenCalled()
  })

  it('click checkbox correctly', async () => {
    const wrapper = doMount()
    await flushPromises()
    await wrapper.vm.$nextTick()

    const checkboxElements = wrapper.findAll('input[type="checkbox"]')

    checkboxElements[1].trigger('click')

    expect(checkboxElements[1].element.checked).toBeTruthy()
    expect(checkboxElements[0].element.checked).toBeFalsy()
  })

  it('set value of selectedContenantTypes', async () => {
    const setTypeContenantMock = vi.fn()
    const useFilters= vi.fn().mockReturnValue({
      setTypeContenant: setTypeContenantMock
    })

    const wrapper = doMount()
    await flushPromises()
    await wrapper.vm.$nextTick()

    wrapper.vm.selectedContenantTypes = [mockContenantTypes[0]]

    await flushPromises()
    await wrapper.vm.$nextTick()

    expect(wrapper.vm.selectedContenantTypes).toStrictEqual([mockContenantTypes[0]])

    // expect(setTypeContenantMock).toHaveBeenCalled()
  })
})
