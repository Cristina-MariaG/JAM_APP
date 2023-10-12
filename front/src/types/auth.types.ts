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
