<script setup lang="ts">
import { Vue3Lottie } from 'vue3-lottie'
const { t } = useI18n()

const form = reactive<{
  firstname?: string
  lastname?: string
  email?: string
  phone?: string
  address?: string
  city?: string
  message?: string
}>({
  firstname: undefined,
  lastname: undefined,
  email: undefined,
  phone: undefined,
  address: undefined,
  message: undefined,
})

const validate = (state: typeof form) => {
  const errors = []
  if (!state.lastname?.trim()) { errors.push({ path: 'lastname', message: 'Required' }) }
  if (!state.firstname?.trim()) { errors.push({ path: 'firstname', message: 'Required' }) }
  if (!state.email?.trim()) { errors.push({ path: 'email', message: 'Required' }) }
  if (!state.message?.trim()) { errors.push({ path: 'message', message: 'Required' }) }
  return errors
}

function onError (event: any) {
  const element = document.getElementById(event.errors[0].id)
  element?.focus()
  element?.scrollIntoView({ behavior: 'smooth', block: 'center' })
}
//change your mail
function onSubmit () {
  const subject = `Contact Request from Name: ${form.firstname} ${form.lastname}`
  const body = `${form.message}%0D%0A%0D%0A%0D%0A from ${form.firstname} ${form.lastname}%0D%0AEmail: ${form.email}%0D%0APhone: ${form.phone}`
  const mailtoLink = `mailto:your@mail.com?subject=${JSON.stringify(subject)}&body=${JSON.stringify(body)}`
  navigateTo(mailtoLink, { external: true, open: { target: '_blank' } })
}

const title = computed(() => t('contact.title'))
const description = computed(() => t('contact.description'))
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
          :title="t('contact.title')"
          :description="t('contact.description')"
          :ui="{
            wrapper: 'py-0 md:py-4'
          }"
        />
        <UDivider type="dashed" />

      <div class="flex flex-col md:grid md:grid-cols-2 space-x-2">
      <div class="lg:col-span-1 lg:items-center" data-aos="fade-right">
        <!-- change/remove animation if needed -->
        <client-only>
          <Vue3Lottie
            animationLink="https://lottie.host/a4c73176-802c-469f-8cb2-e34c51c6ecde/1QvUQBDyug.json"
          />
        </client-only>
      </div>
      <div class="col-span-1 flex flex-col">
        <div class="space-y-4">
          <UForm
        :state="form"
        :validate="validate"
        @error="onError"
        @submit="onSubmit"
        class="space-y-2"
        >
        <UFormGroup
            :label="t('contact.form.lastname')"
            name="lastname"
            required
            class="lg:col-start-1"
          >
            <UInput
              v-model="form.lastname"
              :placeholder="t('contact.form.lastname')"
              size="md"
            />
          </UFormGroup>
          <UFormGroup
            :label="t('contact.form.firstname')"  
            name="firstname"
            required
            class="lg:col-start-1"
          >
            <UInput
              v-model="form.firstname"
              :placeholder="t('contact.form.firstname')"
              size="md"
            />
          </UFormGroup>
          <UFormGroup
            :label="t('contact.form.email')"
            name="email"
            required
            class="lg:col-start-1"
          >
            <UInput
              v-model="form.email"
              type="email"
              :placeholder="t('contact.form.email')"
              size="md"
            />
          </UFormGroup>
          <UFormGroup
            :label="t('contact.form.phone')"
            name="phone"
            class="lg:col-start-1"
          >
            <UInput
              v-model="form.phone"
              :placeholder="t('contact.form.phone')"
              size="md"
            />
          </UFormGroup>
          <UFormGroup
            :label="t('contact.form.message')"
            name="message"
            required
            class="lg:col-start-3 lg:row-start-1 row-span-3 flex flex-col"
            :ui="{
              container: 'h-full'
            }"
          >
            <UTextarea
              v-model="form.message"
              :placeholder="t('contact.form.messagePlaceholder')"
              :ui="{
                wrapper: 'h-full',
                base: 'h-full'
              }"
              size="md"
            />
          </UFormGroup>
          <UButton
            class="lg:col-start-3 lg:row-start-4 self-end space-y-2"
            type="submit"
            size="xl"
            block
            :ui="{
              rounded: 'rounded-full'
            }"
          >
            {{ t('contact.form.button') }}
          </UButton>
        </UForm>
        </div>
        
          </div>
      </div>
    </UPageBody>
    </UPage>
        
</template>