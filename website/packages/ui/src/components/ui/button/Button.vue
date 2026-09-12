<script setup lang="ts">
import { type HTMLAttributes } from "vue";
import { type ButtonVariants, buttonVariants } from ".";
import { cn } from "../../../lib/utils";

const props = withDefaults(
  defineProps<{
    variant?: ButtonVariants["variant"];
    size?: ButtonVariants["size"];
    class?: HTMLAttributes["class"];
    type?: "button" | "submit" | "reset";
  }>(),
  { type: "button" },
);
</script>

<template>
  <button :type="props.type" :class="cn(buttonVariants({ variant, size }), props.class)">
    <slot />
  </button>
</template>
