<script setup lang="ts">
import type { HeaderLink } from '#ui-pro/types'

const { setLocale, t, locale } = useI18n()
// TODO: add pt + es lang
const links = computed<HeaderLink[]>(() => [
  {
  label: 'Resume',
  icon: 'i-heroicons-paint-brush',
  to: '/resume'
  }, 
  {
  label: 'About Me',
  icon: 'i-heroicons-qr-code',
  to: '/about'
  }, 
  {
  label: 'Contact',
  icon: 'i-heroicons-chat-bubble-bottom-center-text',
  to: '/contact'
  }, 
  {
    label: locale.value.toUpperCase(),
    children: [
      {
        label: '🇬🇧',
        click: () => setLocale('en'),
        active: locale.value === 'en',
      },
      {
        label: '🇫🇷',
        click: () => setLocale('fr'),
        active: locale.value === 'fr',
      },
      ],
    },
  ]
)

const light = '/favicon.svg'
const dark = '/favicon_dark.svg'

</script>

<template>
    <UHeader 
      :links="links"
      :ui="{
      center: 'uppercase',
      }"
    >

    <template #logo>
      <UColorModeImage class="w-auto h-8" :light="light" :dark="dark" />
    </template>

    <template #right>
      <UButton icon="i-simple-icons-github" to="https://github.com/your-git" target="_blank" color="gray" variant="ghost" />
      <UButton icon="i-simple-icons-linkedin" to="https://linkedin.com/in/your-linkedin/" target="_blank" color="gray" variant="ghost" />
      <UColorModeButton />
    </template>
  </UHeader>
</template>