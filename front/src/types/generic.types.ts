export interface BasicObject {
  [key: string | symbol]: string | number
}

export type Timer = ReturnType<typeof setInterval>
