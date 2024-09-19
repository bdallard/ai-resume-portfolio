<script setup lang="ts">
const { t, tm } = useI18n()
const xps = [
{
        title: t('cvCard.job1.title'),
        date: t('cvCard.job1.date'),
        url: t('cvCard.job1.url'),
        company: t('cvCard.job1.company'),
        description: t('cvCard.job1.description'),
        stack: tm('cvCard.job1.stack') || []
    },
    {
        title: t('cvCard.job2.title'),
        date: t('cvCard.job2.date'),
        url: t('cvCard.job2.url'),
        company: t('cvCard.job2.company'),
        description: t('cvCard.job2.description'),
        stack: tm('cvCard.job2.stack') || []
    },
    {
        title: t('cvCard.job3.title'),
        date: t('cvCard.job3.date'),
        url: tm('cvCard.job3.url') || [],
        company: tm('cvCard.job3.company') || [],
        description: t('cvCard.job3.description'),
        stack: tm('cvCard.job3.stack') || []
    },
    {
        title: t('cvCard.job4.title'),
        date: t('cvCard.job4.date'),
        url: t('cvCard.job4.url'),
        company: t('cvCard.job4.company'),
        description: t('cvCard.job4.description'),
        stack: tm('cvCard.job4.stack') || []
    }
]

const title = computed(() => t('resume.title'))
const description = computed(() => t('resume.seo'))
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
    <UPageBody
      class="space-y-6 gap-6"
    >
      <UPageHero
      :title="t('resume.title')"
      description=""
      :ui="{
            wrapper: 'py-0 pb-10 md:pb-20 md:py-4'
          }"
      >
        <template #description>
          <p>
            {{ t('resume.description1') }}
          <ULink
            to="your-school-link-here"
            target="_blank"
            active-class="primary-500 underline underline-offset-4"
            inactive-class="underline underline-offset-4 text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200"
          >
          {{ t('resume.school') }}
          </ULink>

          </br>
          <p>
            {{ t('resume.description2') }}
          </p>    
          </br>
          <p class="font-bold pb-4 py-2">
            Tech keeps moving fast, and so do I 😎
          </p>
          </p>
        </template>
      </UPageHero>

      <UDivider type="dashed" />
      
      <div class="space-y-2 md:space-y-4 lg:space-y-6 py-2">
        <CVCard 
            v-for="xp in xps"
            :xp="xp"
        />
      </div>

      <UPageHero
        :title="t('resume.techTitle')"
        :description="t('resume.tech')"
        />
      
      <UDivider type="dashed" />
        
      <div class="flex flex-col px-4 py-4 md:grid md:grid-cols-2 md:gap-12">
        <div class="space-y-4 text-right md:text-right" data-aos="fade-right">
            <h2 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white md:text-4xl">
                {{ t('resume.techCard1') }}
            </h2>
            <p class="text-lg text-gray-500 dark:text-gray-400">
                {{ t('resume.techCardDescription1') }}
            </p>
        </div>
        <ImageGrid prefix="tech_logos_images/favourite"/>
      </div>

      <UDivider type="dashed" />
      <!-- WEB category -->
      <div class="flex flex-col px-4 py-4 md:grid md:grid-cols-2 md:gap-12">
        <div class="col-span-1 space-y-4 md:text-right" data-aos="fade-right">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white md:text-4xl">
            {{ t('resume.techCard2') }}
          </h2>
          <p class="text-lg/6 text-gray-500 dark:text-gray-400">
            {{ t('resume.techCardDescription2') }}
          </p>
        </div>
        <ImageGrid prefix="tech_logos_images/web"/>
      </div>
      
      <UDivider type="dashed" />
      <!-- DATA category -->
      <div class="flex flex-col px-4 py-4 md:grid md:grid-cols-2 md:gap-12">
        <div class="col-span-1 space-y-4 md:text-right" data-aos="fade-right">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white md:text-4xl">
            {{ t('resume.techCard3') }}
          </h2>
          <p class="text-lg/6 text-gray-500 dark:text-gray-400">
            {{ t('resume.techCardDescription3') }}
          </p>
        </div>
        <ImageGrid prefix="tech_logos_images/data"/>
      </div>
      

      <UDivider type="dashed" />
      <!-- PLAYGROUND category -->
      <div class="flex flex-col px-4 py-4 md:grid md:grid-cols-2 md:gap-12">
        <div class="col-span-1 space-y-4 md:text-right" data-aos="fade-right">
          <h2 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white md:text-4xl">
            {{ t('resume.techCard4') }}
          </h2>
          <p class="text-lg/6 text-gray-500 dark:text-gray-400 py-2">
            {{ t('resume.techCardDescription4') }}
          </p>
        </div>
        <ImageGrid prefix="tech_logos_images/playground"/>
      </div>
      
    </UPageBody>
  </UPage>
</template>