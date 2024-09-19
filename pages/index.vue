<script setup lang="ts">
const { t } = useI18n()

const title = computed(() => 'Welcome to my portfolio website!')
const description = computed(() => t('index.description'))
useSeoMeta({
  title: title,
  description: description,

  ogTitle: title,
  ogDescription: description,

  twitterTitle: title,
  twitterDescription: description,
})

</script>

<template>
  <UPage>
    <div class="flex flex-col md:grid md:grid-cols-4 gap-3">
      <!-- Replace/remove animation if needed at : https://lottiefiles.com/ -->  
      <div 
          class="hidden md:block md:col-span-1 md:place-items-center"
          data-aos="fade-right">
          <client-only>
            <Vue3Lottie
              animationLink="https://lottie.host/fad7d8ad-d170-4e75-a0da-356cf7575831/zALdxGk45j.json"
            />
          </client-only>
        </div>
        <div class="md:col-span-3">
        <ULandingHero
          title="Data Science Full Stack Engineer"
          :description="t('index.description')"
          orientation="vertical"
        >
          <template #headline>
            <!-- your calendly link here -->
            <UButton
              color="gray"
              target="_blank"
              :label="t('index.button')"
              trailing-icon="i-heroicons-arrow-right"
              size="xs"
              class="rounded-full"
            />
          </template>
        </ULandingHero>
        </div>
      </div>
  </UPage>
</template>