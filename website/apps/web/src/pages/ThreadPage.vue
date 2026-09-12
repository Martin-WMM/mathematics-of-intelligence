<script setup lang="ts">
import { Card } from "@moi/ui";
import { PARTS, TOPICS, type ThreadId } from "@moi/shared";
import { computed } from "vue";
import { useI18n } from "vue-i18n";
import { useRoute } from "vue-router";

const { t } = useI18n();
const route = useRoute();

const thread = computed(() => route.params.thread as ThreadId);

const title = computed(() => t(`thread.${thread.value}.title`));
const body = computed(() => t(`thread.${thread.value}.body`));
</script>

<template>
  <div class="mx-auto max-w-6xl px-6 py-16">
    <h1 class="font-serif text-3xl">{{ title }}</h1>
    <p class="mt-3 max-w-2xl text-muted-foreground">{{ body }}</p>

    <div v-if="thread === 'topics'" class="mt-8 grid gap-4 md:grid-cols-2">
      <Card v-for="topic in TOPICS" :key="topic.id" class="p-5">
        <h2 class="font-serif text-lg">{{ topic.label }}</h2>
        <p class="mt-2 font-mono text-xs text-muted-foreground">topics/{{ topic.id }}/</p>
      </Card>
    </div>

    <div v-else class="mt-8 space-y-6">
      <section v-for="part in PARTS" :key="part.id">
        <h2 class="font-serif text-xl">{{ part.title }}</h2>
        <ul class="mt-2 list-disc space-y-1 pl-5 text-sm text-muted-foreground">
          <li v-for="chapter in part.chapters" :key="chapter.id">{{ chapter.title }}</li>
        </ul>
      </section>
    </div>
  </div>
</template>
