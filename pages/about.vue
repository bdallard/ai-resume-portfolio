<script setup lang="ts">
const { t } = useI18n()
const toast = useToast()

interface LanguageOption {
  label: string;
  value: string;
}
const form = reactive<{
  company?: string
  job?: string
  lang?: LanguageOption
}>({
  company: undefined,
  job: undefined,
  lang: undefined,
})

const llmResponse = ref('')
const error = ref('')
const loading = ref(false)

const options: LanguageOption[] = [
  { label: 'French', value: 'Français' },
  { label: 'English', value: 'English' },
  { label: 'Spanish', value: 'Spanish' },
  { label: 'Portuguese', value: 'Portuguese' }
]

const validate = (forml: typeof form) => {
  const errors = []
  if (!forml.company || !forml.company.trim() ) {
    errors.push({ path: 'company', message: 'Enter your company name' })
  }
  if (!forml.job || !forml.job.trim()) {
    errors.push({ path: 'job', message: 'Enter your job title' })
  }
  if (!forml.lang) {
    errors.push({ path: 'lang', message: 'Select a language' })
  }
  return errors
}

const title = computed(() => t('about.title'))
const description = computed(() => t('about.description1'))
useSeoMeta({
  title: title,
  description: description,

  ogTitle: title,
  ogDescription: description,

  twitterTitle: title,
  twitterDescription: description,
})

const isSectionVisible = ref(false)
const toggleSectionVisibility = () => {
  isSectionVisible.value = !isSectionVisible.value
}

watch(isSectionVisible, (newValue) => {
  if (newValue) {
    scrollToBottom()
  }
})

const scrollToBottom = () => {
  window.scrollTo({
    top: document.body.scrollHeight,
    behavior: 'smooth'
  })
}

const sendMessage = async () => {
  loading.value = true
  try {
    const response = await useFetch('/api/llm', {
      method: 'POST',
      body: {
        message: form.company,
        job: form.job,
        language: form.lang?.value
      }
    })

    if (response.error.value) {
      console.error('Failed to fetch LLM API:', response.error.value)
      error.value = t('about.llm_error')
    } else {
      llmResponse.value = response.data.value ?? ''
    }
  } catch (error) {
    throw createError({ statusCode: 500, statusMessage: 'Error processing your request' })
  } finally {
    loading.value = false
  }
}

//change your mail below
function onSubmit() {
  const subject = `I want to know your profile and your motivations for [ENTER OBJECT]`
  const mailtoLink = `mailto:your-mail-here?subject=${encodeURIComponent(subject)}`
  navigateTo(mailtoLink, { external: true, open: { target: '_blank' } })
}

// Function to remove text and toggle section visibility
function removeTxt() {
  isSectionVisible.value = false
  llmResponse.value = '' 
}


</script>

<template>
    <UPage>
        <UPageBody
          :ui="{
                wrapper: 'flex flex-col gap-4'
            }"
        >
        <UPageHero
            :title="t('about.title')"
            :description="t('about.description1')"
            :ui="{
                wrapper: 'py-0 md:py-4'
                }"
            />
          <UDivider type="dashed" />
          <UCard
            :ui="{
              header: {
                base: 'text-lg',
              }
          }">
            <template #header>
              Jonh Doe <br>
              Bourg Palette <br>
              X 🕯
            </template>
            <div class="px-4 text-lg text-gray-500 dark:text-gray-400">
            
            <div class="py-4 md:py-6 lg:py-8">
              {{ t('about.description2') }}
              <UButton 
                label="Click Here" 
                color="gray"
                to='https://novoresume.com/career-blog/cover-letter-examples'
                external="true"
                target="_blank"
                >
                <template #trailing>
                  <UIcon name="i-heroicons-arrow-right-20-solid" class="w-4 h-4" />
                </template>
              </UButton>  
            </div>

            <div class="py-4 md:py-6 lg:py-8">
              {{ t('about.description3') }}
              <UButton 
                @click="toggleSectionVisibility"
                label="Click Here" 
                color="gray">
                <template #trailing>
                  <UIcon name="i-heroicons-arrow-right-20-solid" class="w-4 h-4" />
                </template>
              </UButton>           
            </div>

            <div class="py-4 md:py-6 lg:py-8">
              {{ t('about.description4') }}
              <UButton 
                @click="onSubmit"
                label="Click Here" 
                color="gray"
                >
                <template #trailing>
                  <UIcon name="i-heroicons-arrow-right-20-solid" class="w-4 h-4" />
                </template>
              </UButton>
              {{ t('about.description5') }}       
              </div>

            </div>            
          </UCard>

          <!-- Section to hide/reveal -->
          <div 
            ref="revealedSection" 
            v-if="isSectionVisible"
            >
            <UDivider type="dashed" />

            <UPageHero
              title="AI Cover letter generator"
              :ui="{
                wrapper: 'py-4 md:py-8'
              }"
            />
            <UForm
              :state="form"
              :validate="validate"
              @submit="sendMessage"
              >
              <div class="gap-4 grid grid-cols-1 lg:grid-cols-2 text-lg">
              <UFormGroup
                :label="t('Company')"
                name="Company"
                class="lg:col-start-1"
              >
                <UInput
                  v-model="form.company"
                  :placeholder="t('Tape your company name here')"
                  size="lg"
                  required
                />
              </UFormGroup>
              <UFormGroup
                :label="t('Job Title')"
                name="jobTitle"
                class="lg:col-start-2"
              >
                <UInput
                  v-model="form.job"
                  :placeholder="t('Tape your job title here')"
                  :ui="{
                    wrapper: 'h-full',
                    base: 'h-full'
                  }"
                  size="lg"
                  required
                />
              </UFormGroup>

              <UFormGroup
                :label="t('Language')"
                name="lang"
                :ui="{
                  container: 'h-full'
                }"
                class="lg:col-start-1"
              >
              <UInputMenu 
                v-model="form.lang"
                :options="options"
                placeholder="Select Language"
                size="lg"
                required
                />
              </UFormGroup>
              <UButton
                class="lg:col-start-2"
                type="submit"
                size="sm"
                block
              >
                {{ t('contact.form.button') }}
              </UButton>
              </div>
            </UForm>     
          </div>
     
      <div v-if="error" class="text-red-500 items-center">{{ error }}</div>

      <UDivider type="dashed" />

      <div class="py-2">
        <ULandingCard
          :description="llmResponse"
          v-if="llmResponse"
          color="primary"
          :ui="{
            description: 'text-lg/6 text-gray-500 dark:text-gray-400 mt-1 whitespace-pre-line'
          }"
        />
        <div 
          ref="revealedSection" 
          v-if="isSectionVisible"
          class="flex flex-row space-x-2 py-2">
          <UButton 
            :padded="false" 
            color="gray" 
            variant="link" 
            icon="i-heroicons-x-mark" 
            @click="removeTxt" />
        </div>
      </div>
    </UPageBody>
  </UPage>  
</template>