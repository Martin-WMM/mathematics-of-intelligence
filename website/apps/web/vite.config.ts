import { fileURLToPath, URL } from "node:url";
import vue from "@vitejs/plugin-vue";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: [
      {
        find: "@moi/ui/style.css",
        replacement: fileURLToPath(new URL("../../packages/ui/src/style.css", import.meta.url)),
      },
      { find: "@moi/ui", replacement: fileURLToPath(new URL("../../packages/ui/src/index.ts", import.meta.url)) },
      { find: "@moi/i18n", replacement: fileURLToPath(new URL("../../packages/i18n/src/index.ts", import.meta.url)) },
      { find: "@moi/shared", replacement: fileURLToPath(new URL("../../packages/shared/src/index.ts", import.meta.url)) },
      { find: "@", replacement: fileURLToPath(new URL("./src", import.meta.url)) },
    ],
  },
  server: {
    port: 5173,
    fs: {
      allow: ["../.."],
    },
  },
});
