import { useAuthStore } from '../auth'
import { authRepository } from '@/helpers/api'
import { expect, describe, it, vi, beforeEach } from 'vitest'
import { setActivePinia, createPinia } from 'pinia'

vi.mock('@/helpers/api', () => ({
  authRepository: {
    login: vi.fn(),
    inscription: vi.fn()
  }
}))
let authStore;

describe('Auth Store', () => {
  beforeEach(() => {
    // creates a fresh pinia and makes it active
    // so it's automatically picked up by any useStore() call
    // without having to pass it to it: `useStore(pinia)`
    setActivePinia(createPinia())
    authStore = useAuthStore()
  })

  it('checks initial state values', () => {
    expect(authStore.accessToken).toBe('')
    expect(authStore.refreshToken).toBe('')
    expect(authStore.email).toBe('')
  })

  it('checks if user is authenticated', () => {
    expect(authStore.isAuth).toBe(false) // Initially, user should not be authenticated
    authStore.accessToken = 'test_token'
    expect(authStore.isAuth).toBe(true) // User should be authenticated after setting the token
  })

  it('checks login action', async () => {
    const mockPayload = { email: 'test@example.com', password: 'password' }
    const mockResponse = {
      token: { access_token: 'test_access_token', refresh_token: 'test_refresh_token' },
      user: { email: 'test@example.com' }
    }
    authRepository.login.mockResolvedValueOnce(mockResponse)

    const result = await authStore.login(mockPayload)
    expect(result).toBe(true)
    expect(authStore.accessToken).toBe('test_access_token')
    expect(authStore.refreshToken).toBe('test_refresh_token')
    expect(authStore.email).toBe('test@example.com')
  })

  it('checks setRefreshedTokens action', async () => {
    const mockToken = { access_token: 'new_access_token', refresh_token: 'new_refresh_token' }
    await authStore.setRefreshedTokens(mockToken)
    expect(authStore.accessToken).toBe('new_access_token')
    expect(authStore.refreshToken).toBe('new_refresh_token')
  })

  it('checks inscription action', async () => {
    const mockPayload = { email: 'test@example.com', password: 'password' }
    authRepository.inscription.mockResolvedValueOnce()

    const result = await authStore.inscription(mockPayload)
    expect(result).toBe(true)
  })

  it('checks logout action', () => {
    authStore.accessToken = 'test_token'
    authStore.refreshToken = 'test_refresh_token'
    authStore.email = 'test@example.com'
    authStore.logout()
    expect(authStore.accessToken).toBe('')
    expect(authStore.refreshToken).toBe('')
    expect(authStore.email).toBe('')
  })
})
