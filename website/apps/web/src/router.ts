import { createRouter, createWebHistory } from "vue-router";
import HomePage from "./pages/HomePage.vue";
import ReadPage from "./pages/ReadPage.vue";
import ResourcesPage from "./pages/ResourcesPage.vue";
import ThreadPage from "./pages/ThreadPage.vue";

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", name: "home", component: HomePage },
    { path: "/read", name: "read", component: ReadPage },
    { path: "/resources", name: "resources", component: ResourcesPage },
    { path: "/:thread(mathematics|ai|topics)", name: "thread", component: ThreadPage },
  ],
  scrollBehavior() {
    return { top: 0 };
  },
});
