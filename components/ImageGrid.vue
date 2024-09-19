<script lang="ts">
import { defineProps, ref, watch, toRefs, defineComponent } from 'vue'

export default defineComponent({
  props: {
    prefix: {
      type: String,
      required: true
    },
  },
  setup(props) {
    const imageUrls = ref<Array<string>>([])
    const staticImageUrls = ref<Array<string>>([])

      const loadStaticImages = async () => {
      try {
        const response = await fetch(`/api/static_images?prefix=${encodeURIComponent(props.prefix)}`)
        if (response.ok) {
          const result = await response.json()
          staticImageUrls.value = result.urls
        } else {
          console.error('Error loading static images:', response.statusText)
        }
      } catch (error) {
        console.error('Error loading static images:', error)
      }
    }


    const { data, pending, error, refresh } = useAsyncData(
      `images-${props.prefix}`,
      async () => {
        const response = await fetch(`/api/images?prefix=${encodeURIComponent(props.prefix)}`)
        if (!response.ok) {
          await loadStaticImages()  // Load static images if the API call fails
          throw new Error('Failed to fetch image URLs')
        }
        const result = await response.json()
        return result.urls
      }
    )

    // Watch the data for changes and update imageUrls
    watch(data, (newData) => {
      if (newData) {
        imageUrls.value = newData
      }
    }, { immediate: true })

    const getFileName = (url: string) : string => {
      const parts = url.split('/')
      const fileName = parts[parts.length - 1]
      return fileName.replace(/\.[^/.]+$/, '')
    }

    return {
      imageUrls,
      staticImageUrls,
      getFileName,
      pending,
      error,
      refresh
    }
  }
})
</script>

<template>
  <div class="grid grid-cols-4 md:grid-cols-6 gap-4 place-items-center py-2" data-aos="fade-left">
    <div v-if="pending">
      <USkeleton v-for="index in 24" :key="index" width="50px" height="50px" />
    </div>
    
      <div v-for="(url, index) in imageUrls || staticImageUrls " :key="index">
        <img v-if="url" :src="url" width="50" :alt="getFileName(url)" :title="getFileName(url)" />
      </div>
  </div>
</template>

  