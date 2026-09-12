<script setup lang="ts">
import { Button } from "@moi/ui";
import { computed, ref } from "vue";
import { useI18n } from "vue-i18n";

const { t } = useI18n();
const edition = ref<"light" | "dark">("light");
const missing = ref(false);

const pdfSrc = computed(() =>
  edition.value === "light" ? "/pdfs/book-light.pdf" : "/pdfs/book-dark.pdf",
);

function onFrameError() {
  missing.value = true;
}

function checkPdf() {
  missing.value = false;
  fetch(pdfSrc.value, { method: "HEAD" })
    .then((response) => {
      missing.value = !response.ok;
    })
    .catch(() => {
      missing.value = true;
    });
}

checkPdf();

function setEdition(next: "light" | "dark") {
  edition.value = next;
  checkPdf();
}
</script>

<template>
  <div class="mx-auto flex max-w-6xl flex-col gap-4 px-6 py-8">
    <div>
      <h1 class="font-serif text-3xl">{{ t("read.title") }}</h1>
      <p class="mt-2 max-w-2xl text-sm leading-6 text-muted-foreground">
        {{ t("read.subtitle") }}
      </p>
    </div>
    <div class="flex flex-wrap items-center gap-2">
      <Button :variant="edition === 'light' ? 'default' : 'outline'" size="sm" @click="setEdition('light')">
        {{ t("read.light") }}
      </Button>
      <Button :variant="edition === 'dark' ? 'default' : 'outline'" size="sm" @click="setEdition('dark')">
        {{ t("read.dark") }}
      </Button>
      <a :href="pdfSrc" target="_blank" rel="noreferrer" class="ml-auto">
        <Button variant="ghost" size="sm">{{ t("read.openTab") }}</Button>
      </a>
    </div>
    <p v-if="missing" class="rounded-md border border-border bg-card px-4 py-3 text-sm text-muted-foreground">
      {{ t("read.missing") }}
    </p>
    <iframe
      v-else
      :src="pdfSrc"
      :title="t('read.title')"
      class="h-[78vh] w-full rounded-md border border-border bg-card"
      @error="onFrameError"
    />
  </div>
</template>
