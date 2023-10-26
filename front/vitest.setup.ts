import { config } from '@vue/test-utils'
import { vi } from 'vitest'
import { createVuetify } from 'vuetify'
import { mockTranslateText, mockTranslateDate } from './src/functions/i18nMocks'

// global plugin imports/mocks
const vuetify = createVuetify()

config.global.plugins = [vuetify]

config.global.mocks = {
  $t: mockTranslateText,
  $d: mockTranslateDate
}

// global mocks
global.ResizeObserver = vi.fn().mockImplementation(() => ({
  observe: vi.fn(),
  unobserve: vi.fn(),
  disconnect: vi.fn()
}))
global.requestAnimationFrame = vi.fn()

window.scrollTo = () => {}
window.URL.createObjectURL = () => ''
HTMLCanvasElement.prototype.getContext = () => null

// emulates svg support to avoid leaflet layers errors
const createElementNSOrig = global.document.createElementNS

// eslint-disable-next-line func-names
global.document.createElementNS = function (namespaceURI, qualifiedName) {
  if (namespaceURI === 'http://www.w3.org/2000/svg' && qualifiedName === 'svg') {
    // eslint-disable-next-line
    const element = createElementNSOrig.apply(this, arguments);

    element.createSVGRect = () => {};

    return element;
  }

  // eslint-disable-next-line
  return createElementNSOrig.apply(this, arguments);
};
