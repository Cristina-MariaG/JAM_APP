<script setup lang="ts">
import { ref } from 'vue'

const validForm = ref(false)
const label = 'Login'
const emit = defineEmits(['click'])
const handleClick = () => {
  emit('click')
}
</script>

<template>
  <v-btn
    type="submit"
    block
    class="text-none mb-4"
    :disabled="!validForm"
    color="indigo-darken-3"
    size="x-large"
    @click="handleClick"
    variant="flat"
  >
    {{ label }}
  </v-btn>
</template>


