import useFilters from '../filters'

import { expect, describe, it, beforeEach } from 'vitest'

describe('useFilters composable', () => {
  let {
    state,
    setMinPriceUser,
    setMaxPriceUser,
    setSearchedText,
    setCategoriesSearched,
    setPromotion,
    setFlavour,
    setAvailableStock,
    setTypeContenant,
    setbrandList,
    setOrdonateByPrice
  } = useFilters()

  beforeEach(() => {
    ;({
      state,
      setMinPriceUser,
      setMaxPriceUser,
      setSearchedText,
      setCategoriesSearched,
      setPromotion,
      setFlavour,
      setAvailableStock,
      setTypeContenant,
      setbrandList,
      setOrdonateByPrice
    } = useFilters())
  })
  it('sets min price user', () => {
    const { state, setMinPriceUser } = useFilters()
    setMinPriceUser(50)
    expect(state.minPriceUser).toBe(50)
    expect(state.chosenFilters).toContain('minPriceUser')
  })

  it('sets searched text', () => {
    const { state, setSearchedText } = useFilters()
    setSearchedText('sample text')
    expect(state.searchedText).toBe('sample text')
    expect(state.chosenFilters).toContain('searchedText')
  })

  it('clears categories and removes it from chosen filters', async () => {
    const { state, setCategoriesSearched } = useFilters()
    state.categories = [1, 2, 3]
    setCategoriesSearched([])
    expect(state.categories).toEqual([])
  })

  it('sets min price user', () => {
    setMinPriceUser(50)
    expect(state.minPriceUser).toBe(50)
    expect(state.chosenFilters).toContain('minPriceUser')
  })

  it('sets max price user', () => {
    setMaxPriceUser(100)
    expect(state.maxPriceUser).toBe(100)
    expect(state.chosenFilters).toContain('maxPriceUser')
  })

  it('sets searched text', () => {
    setSearchedText('sample text')
    expect(state.searchedText).toBe('sample text')
    expect(state.chosenFilters).toContain('searchedText')
  })

  it('sets categories searched', () => {
    setCategoriesSearched([1, 2, 3])
    expect(state.categories).toEqual([1, 2, 3])
    expect(state.chosenFilters).toContain('categories')

    setCategoriesSearched([])
    expect(state.categories).toEqual([])
    expect(state.chosenFilters).not.toContain('categories')
  })

  it('sets promotion', () => {
    setPromotion(true)
    expect(state.promotion).toBe(true)
  })

  it('sets flavour', () => {
    setFlavour('chocolate')
    expect(state.flavor).toBe('chocolate')
  })

  it('sets available stock', () => {
    setAvailableStock(true)
    expect(state.availableStock).toBe(true)
    expect(state.chosenFilters).toContain('availableStock')
  })

  it('sets type contenant', () => {
    setTypeContenant(['bottle', 'box'])
    expect(state.typeContenant).toEqual(['bottle', 'box'])
    expect(state.chosenFilters).toContain('typeContenant')

    setTypeContenant([])
    expect(state.typeContenant).toEqual([])
  })

  it('sets brand list', () => {
    setbrandList([100, 200, 300])
    expect(state.brandList).toEqual([100, 200, 300])
    expect(state.chosenFilters).toContain('brandList')

    setbrandList([])
    expect(state.brandList).toEqual([])
  })

  it('sets ordonate by price', () => {
    setOrdonateByPrice('true')
    expect(state.ordonateByPrice).toBe('true')
    expect(state.chosenFilters).toContain('ordonateByPrice')
  })
})
