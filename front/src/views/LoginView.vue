<script setup lang="ts">
import { reactive, toRaw } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'

const authStore = useAuthStore()
const router = useRouter()

const form = reactive({
  email: '',
  password: ''
})

const handleSubmit = async () => {
  const success = await authStore.login(toRaw(form))
  if (success) {
    console.log(success)
    router.push({ name: 'home' })
  } else {
    Swal.fire({
      icon: 'error',
      title: 'Bad credentials'
    })
  }
}
</script>

<template>
  <form @submit.prevent="handleSubmit">
    <div>
      <label for="email">Email</label>
      <input type="text" v-model="form.email" id="email" />
    </div>
    <div>
      <label for="password">Password</label>
      <input type="password" v-model="form.password" id="password" />
    </div>
    <button type="submit">Login</button>
  </form>
  <RouterLink to="/signIn">Sing In</RouterLink>
</template>

<style scoped></style>
