<script setup lang="ts">
import { type Ref } from 'vue'
import { ref, reactive, toRaw } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import { useValidationRules } from '@/composables/validateForm'
import Swal from 'sweetalert2'

const validationRules = useValidationRules()
const authStore = useAuthStore()
const router = useRouter()

const form = reactive({
  email: '',
  password: ''
})

const showEmptyFieldError = ref(false)

const password2: Ref<string | null> = ref(null)

const handleSubmit = async () => {
  if (form.password === password2.value) {
    const isEmailValid = validationRules.emailRule[0](form.email) === true
    const isPasswordValid = validationRules.passwordRule[0](form.password) === true

    if (form.email === '' || form.password === '') {
      showEmptyFieldError.value = true
      return
    }

    if (isEmailValid && isPasswordValid) {
      const success = await authStore.signup(toRaw(form))
      console.log(success)
      if (success) {
        router.push({ name: 'login' })
      } else {
        Swal.fire({
          icon: 'error',
          title: 'Bad credentials'
        })
      }
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
  <div style="width: 50%" class="mx-auto login">
    <h1 class="text-center">Inscription</h1>
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
      <v-text-field
        v-model="password2"
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
        >Inscription</v-btn
      >
    </form>
    <p class="text-center">
      Vous avez deja un compte ?
      <RouterLink to="/login">Login</RouterLink>
    </p>
  </div>
</template>

<style scoped></style>
