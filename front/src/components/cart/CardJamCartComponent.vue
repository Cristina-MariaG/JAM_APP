<script setup lang="ts">
import ContainerComponent from './ContainerComponent.vue'
import HeaderCardComponent from './HeaderCardComponent.vue'
import SyntheseCartComponent from './SyntheseCartComponent.vue'
</script>

<template>
  <v-card>
    <v-container fluid>
      <v-row dense>
        <v-col cols="8">
          <HeaderCardComponent />
          <div>
            <hr class="gray-line" />
            <ContainerComponent />
          </div>
        </v-col>
        <v-col col="4" class="ps-5">
          <SyntheseCartComponent />
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>
