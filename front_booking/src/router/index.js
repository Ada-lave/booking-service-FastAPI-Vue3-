import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterPageView from '../views/RegisterPageView.vue'
import MainView from "../views/MainView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/register",
      name: 'register',
      component: RegisterPageView
    },
    {
      path: "/",
      name: 'main',
      component: MainView
    },

    
  ]
})

export default router
