import { flushPromises, mount } from '@vue/test-utils'
import { expect, describe, vi, it } from 'vitest'
import { categoryRepository } from '@/helpers/api'
import CategoryComponent from '@/components/filterComponents/CategoryComponent.vue'
import useFilters from '@/composables/filters'

const categoriesData = [
  { id: 1, category: 'Category' },
  { id: 2, category: 'Category2' },
  { id: 3, category: 'Category3' }
]

vi.mock('@/helpers/api', () => ({
  categoryRepository: {
    getCategories: vi.fn().mockResolvedValue({
      categories: [
        { id: 1, category: 'Category' },
        { id: 2, category: 'Category2' },
        { id: 3, category: 'Category3' }
      ]
    })
  }
}))

const setbrandListMock = vi.fn()
const useFiltersMock = vi.fn().mockReturnValue({
  setbrandList: setbrandListMock
})
vi.doMock('@/composables/filters', () => ({
  default: useFiltersMock,
  useFilters: vi.fn()
}))

const doMount = () => {
  return mount(CategoryComponent, {
    global: {}
  })
}

describe('CategoryComponent', () => {
  it('initializes data correctly', async () => {
    const wrapper = doMount()
    await flushPromises()
    await wrapper.vm.$nextTick()

    expect(categoryRepository.getCategories).toHaveBeenCalled()

    expect(wrapper.vm.apiCategories).toEqual(categoriesData)
    expect(wrapper.vm.selectedCategories).toEqual([])
  })

  it('calls setCategoriesSearched on selectedCategories change', async () => {
    const wrapper = doMount()
    await wrapper.vm.$nextTick()

    wrapper.vm.selectedCategories = [categoriesData[0]]

    await wrapper.vm.$nextTick()

    expect(wrapper.vm.selectedCategories).toStrictEqual([categoriesData[0]])
    await flushPromises()
    await wrapper.vm.$nextTick()
  })

  it('renders categories correctly', async () => {
    const wrapper = doMount()
    await flushPromises()
    await wrapper.vm.$nextTick()

    const renderedCategories = wrapper.findAll('.category .d-flex')
    expect(renderedCategories.length).toBe(categoriesData.length)
    expect(renderedCategories[0].text()).toContain(categoriesData[0].category)
    expect(renderedCategories[1].text()).toContain(categoriesData[1].category)
    expect(renderedCategories[2].text()).toContain(categoriesData[2].category)
  })
})
