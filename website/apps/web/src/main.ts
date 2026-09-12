import { createApp } from "vue";
import { createI18n } from "vue-i18n";
import { defaultLocale, messages } from "@moi/i18n";
import App from "./App.vue";
import { router } from "./router";
import "@moi/ui/style.css";

const savedLocale = localStorage.getItem("moi-locale");
const locale = savedLocale === "zh-CN" || savedLocale === "en" ? savedLocale : defaultLocale;

const i18n = createI18n({
  legacy: false,
  locale,
  fallbackLocale: "en",
  messages,
});

const savedTheme = localStorage.getItem("moi-theme");
if (savedTheme === "dark") {
  document.documentElement.classList.add("dark");
}

createApp(App).use(router).use(i18n).mount("#app");
