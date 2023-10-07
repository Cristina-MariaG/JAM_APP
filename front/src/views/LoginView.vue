<script setup lang="ts">
import { reactive, ref, toRaw } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'
import { useValidationRules } from '@/composables/validateForm' // Assurez-vous d'importer correctement le chemin du composable

const authStore = useAuthStore()
const router = useRouter()
const validationRules = useValidationRules()

const form = reactive({
  email: '',
  password: ''
})
const showEmptyFieldError = ref(false)

const handleSubmit = async () => {
  const isEmailValid = validationRules.emailRule[0](form.email) === true
  const isPasswordValid = validationRules.passwordRule[0](form.password) === true

  if (form.email === '' || form.password === '') {
    showEmptyFieldError.value = true
    return
  }

  if (isEmailValid && isPasswordValid) {
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
}
</script>

<template>
  <div style="width: 50%" class="mx-auto login">
    <h1 class="text-center">Login</h1>
    <form @submit.prevent="handleSubmit">
      <v-text-field
        v-model="form.email"
        label="Email"
        :rules="validationRules.emailRule"
      ></v-text-field>
      <v-text-field
        v-model="form.password"
        label="Password"
        :rules="validationRules.passwordRule"
      ></v-text-field>
      <v-alert class="my-5" v-if="showEmptyFieldError" type="error">
        Veuillez remplir tous les champs.
      </v-alert>
      <v-btn
        type="submit"
        block
        class="text-none mb-4"
        color="indigo-darken-3"
        size="x-large"
        variant="flat"
        >Login</v-btn
      >
    </form>
    <p class="text-center">
      Pas de compte ?
      <RouterLink to="/signup">Inscription</RouterLink>
    </p>
  </div>
</template>

<style>
.login {
  margin-top: 10rem;
}
</style>
