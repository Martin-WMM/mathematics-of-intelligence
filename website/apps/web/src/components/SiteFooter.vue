<script setup lang="ts">
import { useI18n } from "vue-i18n";

const { t } = useI18n();
</script>

<template>
  <footer class="border-t border-border">
    <div class="mx-auto max-w-6xl px-6 py-8 text-sm text-muted-foreground">
      {{ t("footer.note") }}
    </div>
  </footer>
</template>
