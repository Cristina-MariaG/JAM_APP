<script setup lang="ts">
import { reactive, ref, toRaw } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import { useValidationRules } from '@/composables/validateForm'
import Swal from 'sweetalert2'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const validationRules = useValidationRules()
const authStore = useAuthStore()
const router = useRouter()

const form = reactive({
  email: '',
  password: ''
})
const showEmptyFieldError = ref(false)
const validForm = ref(false)

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
      router.push({ name: 'home' })
    } else {
      Swal.fire({
        icon: 'error',
        title: t('error.badCredentials')
      })
    }
  }
}
</script>

<template>
  <div style="width: 50%" class="mx-auto login">
    <h1 class="text-center">{{ $t('login.login') }}</h1>
    <v-form
      v-model="validForm"
      color="primary"
      class="map-right-menu-source-card__source-to-district-form mt-2"
    >
      <v-text-field
        v-model="form.email"
        :label="$t('login.email')"
        :rules="validationRules.emailRule"
      ></v-text-field>
      <v-text-field
        v-model="form.password"
        :label="$t('login.password')"
        type="password"
        :rules="validationRules.passwordRule"
      ></v-text-field>
      <v-alert class="my-5" v-if="showEmptyFieldError" type="error">
        {{ $t('login.fillInput') }}
      </v-alert>
      <v-btn
        type="submit"
        block
        class="text-none mb-4"
        id="submit"
        :disabled="!validForm"
        color="indigo-darken-3"
        size="x-large"
        @click.prevent="handleSubmit"
        variant="flat"
        >{{ $t('login.login') }}</v-btn
      >
    </v-form>
    <div>
      <p class="text-center">
        {{ $t('login.noAccountYet') }}
        <RouterLink class="routerLink" to="/inscription">{{ $t('login.inscription') }}</RouterLink>
      </p>
    </div>
  </div>
</template>

<style>
.login {
  margin-top: 10rem;
}
.routerLink {
  color: var(--vt-c-black);
}
</style>
