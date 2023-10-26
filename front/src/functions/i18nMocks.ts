import type { BasicObject } from '@/types/generic.types'

const mockTranslateText = (key: string, param1?: number | BasicObject, param2?: number) => {
  let result

  if (typeof param1 === 'object' && typeof param2 === 'number') {
    result = JSON.stringify({ t: key, ...param1, c: param2 })
  } else if (typeof param1 === 'object' && typeof param2 === 'undefined') {
    result = JSON.stringify({ t: key, ...param1 })
  } else if (typeof param1 === 'number' && typeof param2 === 'undefined') {
    result = JSON.stringify({ t: key, c: param1 })
  } else {
    result = key
  }

  return result
}

const mockTranslateDate = (key: string) => key

export { mockTranslateText, mockTranslateDate }
