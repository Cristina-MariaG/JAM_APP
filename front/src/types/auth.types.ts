export enum AuthAccess {
  PUBLIC, // everyone can access
  NON_AUTH, //
  AUTH
}

export interface AuthForm {
  email: string
  password: string
}

export interface LoginData {
  token: string
  user: {
    email: string
  }
}
