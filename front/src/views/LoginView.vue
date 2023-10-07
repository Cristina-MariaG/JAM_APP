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

<!-- <script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

import { ref, reactive } from 'vue'
const loading = ref(false)

const email = ref('')
const password = ref('')
const rule1 = [
  (value: string | null) => {
    if (value?.length && value.length > 3) return true
    return 'Le prénom doit contenir au moins 3 caractères.'
  }
]
const rule2 = [
  (value: string | null) => {
    if (value?.length && value.length > 3) return true
    return 'Le prénom doit contenir au moins 3 caractères.'
  }
]
</script>

<template>
  <div>
    <h1>Login Page</h1>
    <v-sheet width="300" class="mx-auto">
      <v-form fast-fail @submit.prevent>
        <v-text-field v-model="email" label="First name" :rules="rule1"></v-text-field>

        <v-text-field v-model="password" label="Last name" :rules="rule2"></v-text-field>

        <v-btn type="submit" block class="mt-2">Submit</v-btn>
      </v-form>
    </v-sheet>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/signIn">PAs de compte ? Sign In</RouterLink>
    <hr />
    fgvdfg
 <RouterView />
  </div>
</template>

<style scoped></style> -->
