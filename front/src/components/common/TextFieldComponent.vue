<script setup lang="ts">
import { defineProps } from 'vue'

const props = defineProps({
  modelValue: {
    type: String,
    required: true
  },
  label: {
    type: String,
    required: true
  },
  type: {
    type: String,
    default: 'text'
  },
  rules: {
    type: Array,
    default: () => []
  }
})
</script>

<template>
  <v-text-field v-model="modelValue" :label="label" :type="type" :rules="rules"></v-text-field>
</template>
