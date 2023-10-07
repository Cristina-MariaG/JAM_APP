import { AxiosError } from 'axios'

export function repositoryErrorHandler(err: unknown) {
  if (err instanceof AxiosError) {
    console.error(err)
    return {
      message: 'Api Error'
    }
  } else if (err instanceof Error) {
    console.error(err.message)
    return {
      message: 'Error'
    }
  }
  return {
    message: 'Unknown'
  }
}
