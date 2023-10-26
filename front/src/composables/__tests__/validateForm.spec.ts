import { useValidationRules } from '../validateForm'
import { expect, describe, it, beforeEach } from 'vitest'



describe('useValidationRules function', () => {
  const { emailRule, passwordRule } = useValidationRules()

  it('checks email validation rule with empty value', () => {
    expect(emailRule[0](null)).toBe('Veuillez saisir une adresse e-mail.')
  })

  it('checks email validation rule with insufficient length', () => {
    expect(emailRule[0]('test')).toBe("L'adresse e-mail doit contenir au moins 10 caractères.")
  })

  it('checks email validation rule with invalid format', () => {
    expect(emailRule[0]('invalidemail')).toBe('Veuillez saisir une adresse e-mail valide.')
  })

  it('checks email validation rule with valid email', () => {
    expect(emailRule[0]('test@example.com')).toBe(true)
  })

  it('checks password validation rule with empty value', () => {
    expect(passwordRule[0](null)).toBe('Veuillez saisir un mot de passe.')
  })

  it('checks password validation rule with insufficient length', () => {
    expect(passwordRule[0]('test')).toBe('Le mot de passe doit contenir au moins 10 caractères.')
  })

  it('checks password validation rule with valid password', () => {
    expect(passwordRule[0]('securepassword')).toBe(true)
  })
})
