<script setup lang="ts">
import { Button, Card } from "@moi/ui";
import { useI18n } from "vue-i18n";
import { RouterLink } from "vue-router";

const { t } = useI18n();
</script>

<template>
  <div class="mx-auto max-w-6xl px-6 py-16">
    <p class="text-sm uppercase tracking-[0.16em] text-muted-foreground">
      {{ t("home.kicker") }}
    </p>
    <h1 class="mt-4 max-w-3xl font-serif text-4xl leading-tight text-foreground md:text-5xl">
      {{ t("meta.title") }}
    </h1>
    <p class="mt-3 font-serif text-xl text-muted-foreground">
      {{ t("meta.tagline") }}
    </p>
    <p class="mt-6 max-w-2xl text-base leading-7 text-foreground/90">
      {{ t("home.lead") }}
    </p>
    <p class="mt-4 font-serif text-lg text-primary">
      {{ t("home.spine") }}
    </p>
    <div class="mt-8 flex flex-wrap gap-3">
      <RouterLink to="/read">
        <Button size="lg">{{ t("home.ctaRead") }}</Button>
      </RouterLink>
      <RouterLink to="/resources">
        <Button size="lg" variant="outline">{{ t("home.ctaResources") }}</Button>
      </RouterLink>
    </div>

    <h2 class="mt-16 font-serif text-2xl">{{ t("home.threadsTitle") }}</h2>
    <div class="mt-6 grid gap-4 md:grid-cols-3">
      <Card class="p-5">
        <h3 class="font-serif text-lg">{{ t("home.mathTitle") }}</h3>
        <p class="mt-2 text-sm leading-6 text-muted-foreground">{{ t("home.mathBody") }}</p>
      </Card>
      <Card class="p-5">
        <h3 class="font-serif text-lg">{{ t("home.aiTitle") }}</h3>
        <p class="mt-2 text-sm leading-6 text-muted-foreground">{{ t("home.aiBody") }}</p>
      </Card>
      <Card class="p-5">
        <h3 class="font-serif text-lg">{{ t("home.topicsTitle") }}</h3>
        <p class="mt-2 text-sm leading-6 text-muted-foreground">{{ t("home.topicsBody") }}</p>
      </Card>
    </div>
  </div>
</template>
