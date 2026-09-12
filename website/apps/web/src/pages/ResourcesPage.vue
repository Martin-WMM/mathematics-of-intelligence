<script setup lang="ts">
import { Card } from "@moi/ui";
import { useI18n } from "vue-i18n";

const { t } = useI18n();
</script>

<template>
  <div class="mx-auto max-w-6xl px-6 py-16">
    <h1 class="font-serif text-3xl">{{ t("resources.title") }}</h1>
    <p class="mt-3 max-w-2xl text-muted-foreground">{{ t("resources.subtitle") }}</p>
    <div class="mt-8 grid gap-4 md:grid-cols-3">
      <Card class="p-5">
        <h2 class="font-serif text-lg">{{ t("resources.animations") }}</h2>
        <p class="mt-2 text-sm leading-6 text-muted-foreground">{{ t("resources.animationsBody") }}</p>
        <p class="mt-4 font-mono text-xs text-muted-foreground">animations/</p>
      </Card>
      <Card class="p-5">
        <h2 class="font-serif text-lg">{{ t("resources.ppts") }}</h2>
        <p class="mt-2 text-sm leading-6 text-muted-foreground">{{ t("resources.pptsBody") }}</p>
        <p class="mt-4 font-mono text-xs text-muted-foreground">ppts/</p>
      </Card>
      <Card class="p-5">
        <h2 class="font-serif text-lg">{{ t("resources.examples") }}</h2>
        <p class="mt-2 text-sm leading-6 text-muted-foreground">{{ t("resources.examplesBody") }}</p>
        <p class="mt-4 font-mono text-xs text-muted-foreground">examples/</p>
      </Card>
    </div>
  </div>
</template>
