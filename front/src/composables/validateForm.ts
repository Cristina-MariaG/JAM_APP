export function useValidationRules() {
  const emailRule = [
    (value: string | null) => {
      if (!value) {
        return 'Veuillez saisir une adresse e-mail.'
      }

      if (value.length < 10) {
        return "L'adresse e-mail doit contenir au moins 10 caractères."
      }

      const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
      if (!emailPattern.test(value)) {
        return 'Veuillez saisir une adresse e-mail valide.'
      }

      return true
    }
  ]

  const passwordRule = [
    (value: string | null) => {
      if (!value) {
        return 'Veuillez saisir un mot de passe.'
      }

      if (value.length < 10) {
        return 'Le mot de passe doit contenir au moins 10 caractères.'
      }

      return true
    }
  ]

  return {
    emailRule,
    passwordRule
  }
}
