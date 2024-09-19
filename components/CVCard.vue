<script setup lang="ts">
import type { CvXP } from '~/types'

defineProps<{
    xp: CvXP
}>()

</script>

<template>
    <ULandingCard
                color="primary"
                orientation="horizontal"
                :ui="{
                    body: {
                        base: 'md:gap-x-8 gap-x-2 md:gap-y-2 rounded-xl sm:flex max-lg:grid max-lg:grid-cols-5 rounded',
                    },
                }"
            >
                <div class="flex-col max-md:col-span-1">
                    <p class="line-clamp-2 text-lg/8 text-gray-400">
                        {{ xp.date }}
                    </p>
                </div>  
               
                <div class="flex-col max-md:col-span-3 max-md:col-start-2 md:px-6">
                    <div class="font-bold text-xl mb-2">
                        
                        <p class="md:group md:relative md:w-max">
                            <span>
                                {{ xp.title }}
                            </span>
                            <span class="absolute -bottom-1 left-0 w-0 transition-all h-0.5 bg-green-500 group-hover:w-full"></span>
                        </p>
                        <p>
                            <template v-if="Array.isArray(xp.company)">
                                <span v-for="(company, index) in xp.company" :key="index">
                                    <ULink
                                        :to="xp.url[index]" 
                                        active-class="text-primary"
                                        inactive-class="text-gray-400 text-lg dark:text-gray-400"
                                        target="_blank">
                                            {{ company }}
                                    </ULink>
                                    <span v-if="index < xp.company.length - 1" class="text-gray-400 text-lg dark:text-gray-400">, </span>
                                </span>
                            </template>
                            <template v-else>
                                <ULink
                                    :to="xp.url" 
                                    active-class="text-primary"
                                    inactive-class="text-gray-400 text-lg dark:text-gray-400"
                                    target="_blank">
                                        {{ xp.company }}
                                </ULink>
                                
                            </template>
                        </p>
                    </div>
                    <p
                        v-if="xp.description"
                        class="py-2 md:py-3 text-gray-700 text-base dark:text-gray-400">
                            {{ xp.description }}
                    </p>
                    <div
                        v-if="xp.stack"
                        class="grid grid-cols-1 gap-1 md:flex md:flex-row md:gap-2 place-items-center">
                        <div 
                            class="gap-2" 
                            v-for="(item, index) in xp.stack" :key="index" >
                            <UBadge color="green">{{ item }}</UBadge>
                            
                        </div>
                    </div> 
                </div>            
    </ULandingCard>
</template>