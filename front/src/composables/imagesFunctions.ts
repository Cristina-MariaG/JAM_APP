export function useImagesFunctions() {
  const getImage = (image: string) => {
    return `public/uploads/${image}`
  }

  return { getImage }
}
