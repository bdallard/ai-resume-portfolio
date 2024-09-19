export default defineAppConfig({
  ui: {
    primary: 'green',
    gray: 'slate',
    tooltip: {
      background: '!bg-background'
    },
    notifications: {
      // Show toasts at the top right of the screen
      position: 'top-0 bottom-auto'
    },
    page: {
      header: {
        wrapper: 'border-none pt-8 pb-0',
        headline: 'text-gray-400 font-normal text-xs',
        title: 'pb-4 font-serif font-normal',
      },
    },
    variables: {
      dark: {
        background: 'var(--color-gray-950)'
      },
      header: {
        height: '5rem'
      }
    },
    icons: {
      dark: 'i-ph-moon-duotone',
      light: 'i-ph-sun-duotone',
      search: 'i-ph-magnifying-glass-duotone',
      external: 'i-ph-arrow-up-right',
      chevron: 'i-ph-caret-down',
      hash: 'i-ph-hash-duotone'
    },
    header: {
      wrapper: 'lg:mb-0 lg:border-0',
      popover: {
        links: {
          active: 'dark:bg-gray-950/50',
          inactive: 'dark:hover:bg-gray-950/50'
        }
      }
    }
  }
})
