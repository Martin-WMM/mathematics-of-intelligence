import { en } from "./en";
import { zhCN } from "./zh-CN";

export const locales = ["en", "zh-CN"] as const;

export type Locale = (typeof locales)[number];

export const messages = {
  en,
  "zh-CN": zhCN,
} as const;

export const defaultLocale: Locale = "en";
