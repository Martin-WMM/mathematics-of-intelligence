<script setup lang="ts">
import { Button } from "@moi/ui";
import { computed, ref } from "vue";
import { useI18n } from "vue-i18n";
import { RouterLink, useRoute } from "vue-router";

const { t, locale } = useI18n();
const route = useRoute();
const isDark = ref(document.documentElement.classList.contains("dark"));

const links = computed(() => [
  { to: "/", label: t("nav.home") },
  { to: "/read", label: t("nav.read") },
  { to: "/mathematics", label: t("nav.mathematics") },
  { to: "/ai", label: t("nav.ai") },
  { to: "/topics", label: t("nav.topics") },
  { to: "/resources", label: t("nav.resources") },
]);

function isActive(path: string) {
  return path === "/" ? route.path === "/" : route.path.startsWith(path);
}

function toggleLocale() {
  const next = locale.value === "en" ? "zh-CN" : "en";
  locale.value = next;
  localStorage.setItem("moi-locale", next);
  document.documentElement.lang = next === "zh-CN" ? "zh-CN" : "en";
}

function toggleTheme() {
  isDark.value = document.documentElement.classList.toggle("dark");
  localStorage.setItem("moi-theme", isDark.value ? "dark" : "light");
}
</script>

<template>
  <header class="border-b border-border bg-background/90">
    <div class="mx-auto flex max-w-6xl flex-col gap-3 px-6 py-4">
      <div class="flex items-center justify-between gap-4">
        <RouterLink to="/" class="font-serif text-lg tracking-tight text-foreground">
          {{ t("meta.title") }}
        </RouterLink>
        <div class="flex items-center gap-2">
          <Button variant="ghost" size="sm" @click="toggleLocale">
            {{ locale === "en" ? "中文" : "EN" }}
          </Button>
          <Button variant="outline" size="sm" @click="toggleTheme">
            {{ isDark ? "Light" : "Dark" }}
          </Button>
        </div>
      </div>
      <nav class="flex flex-wrap items-center gap-x-5 gap-y-2 text-sm">
        <RouterLink
          v-for="link in links"
          :key="link.to"
          :to="link.to"
          class="hover:text-foreground"
          :class="isActive(link.to) ? 'text-foreground' : 'text-muted-foreground'"
        >
          {{ link.label }}
        </RouterLink>
      </nav>
    </div>
  </header>
</template>
