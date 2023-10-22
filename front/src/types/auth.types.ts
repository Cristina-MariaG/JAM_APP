export interface AuthForm {
  email: string
  password: string
}

export interface LoginData {
  token: Token
  user: {
    email: string
  }
}

export interface Token {
  access_token: string
  refresh_token: string
}
