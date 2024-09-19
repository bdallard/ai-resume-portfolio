<script setup lang="ts">
import type { NuxtError } from '#app'

defineProps<{
error: NuxtError
}>()
</script>

<template>
    <div>
      <Header />
      <UContainer>
        <UMain>
          <UPage>
            <UPageError 
            :error="error" 
            :status="404"
            name="Not here"
            message="Sorry the page you are looking for does not exist here 🏝"/>
          </UPage>
        </UMain>
        <Footer />
      </UContainer>
    </div>
  </template>
  
  