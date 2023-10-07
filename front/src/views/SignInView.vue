<script setup lang="ts">
import { type Ref } from 'vue'
import { ref, reactive, toRaw } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

import Swal from 'sweetalert2'

const authStore = useAuthStore()
const router = useRouter()

const form = reactive({
  email: '',
  password: ''
})

const password2: Ref<string | null> = ref(null)

const handleSubmit = async () => {
  if (form.password === password2.value) {
    const success = await authStore.signIn(toRaw(form))
    console.log(success)
    if (success) {
      router.push({ name: 'home' })
    } else {
      Swal.fire({
        icon: 'error',
        title: 'Bad credentials'
      })
    }
  } else {
    Swal.fire({
      icon: 'error',
      title: 'Password not the same'
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
    <div>
      <label for="password2">Password</label>
      <input type="password2" v-model="password2" id="password" />
    </div>
    <button type="submit">Login</button>
  </form>
</template>

<style scoped></style>
