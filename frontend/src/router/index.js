import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import TestView from '../views/test/TestView_execShell.vue'
import MainView from '../views/MainView.vue'
import BlogInfo from '../components/BlogInfo.vue'
import BlogManager from '../components/BlogManager.vue'
import BlogScript from '../components/BlogScript.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Login',
      component: LoginView
    },
    {
      path: '/test',
      name: 'test',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: TestView
    },
    {
      path: '/main',
      name: 'main',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: MainView,
      children: [
        {
          path: 'bloginfo',
          name: 'bloginfo',
          component: BlogInfo,
        },
        {
          path: 'blogmanager',
          name: 'blogmanager',
          component: BlogManager,
        },
        {
          path: 'blogscript',
          name: 'blogscript',
          component: BlogScript,
        },
      ]
    }
  ]
})

export default router
