import { AxiosError } from 'axios'

export function repositoryErrorHandler(err: any) {
  if (err.response.status == 401) {
    return {
      message: 'Une re/connexion est necessaire !'
    }
  }
  if (err instanceof AxiosError) {
    console.error(err)
    return {
      message: 'Api Error'
    }
  } else if (err instanceof Error) {
    return {
      message: 'Error'
    }
  }
  return {
    message: 'Unknown'
  }
}
