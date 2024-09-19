// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  extends: ['@nuxt/ui-pro'],
  modules: [
    '@nuxt/ui',
    '@nuxt/fonts',
    '@nuxtjs/i18n',
    '@nuxtjs/seo',
    'nuxt-aos',
    'nuxt-rate-limit',
    '@dargmuesli/nuxt-cookie-control',
  ],
  plugins: [
    "~/plugins/Vue3Lottie.client.ts",
    { src: '~/plugins/typebot.client.js', mode: 'client' }
  ],
  runtimeConfig: {
    public: {
      url: 'http://localhost:3001',
    },
  },
  i18n: {
    strategy: 'no_prefix',
    locales: ['en', 'fr'],
    defaultLocale: 'en',
    detectBrowserLanguage: {
      useCookie: true,
      fallbackLocale: 'en',
    },
  },
  ui: {
    icons: ['ph', 'simple-icons']
  },
  colorMode: {
    preference: 'light'
  },
  site: {
    url: 'https://dallard.tech',
    name: 'My portfolio website',
    description: 'Welcome to my portfolio website!'
  },
  nuxtRateLimit: {
    routes: {
      '/api/llm': {
        maxRequests: 3,
        intervalSeconds: 120,
      },
      '/api/minio': {
        maxRequests: 10,
        intervalSeconds: 30,
      },
      '/api/static_images': {
        maxRequests: 10,
        intervalSeconds: 30,
      },
      '/api/images': {
        maxRequests: 10,
        intervalSeconds: 30,
      },
    },
  },
  cookieControl: {
    cookies: {
      necessary: [
        {
          id: 'i18n',
          name: {
            en: 'Internationalization',
            fr: 'Internationalisation',
          },
          description: {
            en: 'This cookie is set by the i18n module to remember the user\'s language preference.',
            fr: 'Ce cookie est défini par le module i18n pour se souvenir de la préférence de langue de l\'utilisateur',
          },
        },
      ],
      optional: [],
    },
    locales: ['en', 'fr'],
    colors: {
      checkboxActiveBackground: 'rgb(var(--color-primary-500))',
    },
  },
})