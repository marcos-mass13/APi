import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/home.vue'
import Page from '../pages/page.vue'
import Sobre from '../pages/sobre.vue'
import Login from '../pages/login.vue'

const routes = [
  {path: '/', name:'home', component:Home},
  {path: '/page', name:'page', component:Page},
  {path: '/sobre', name:'sobre', component:Sobre},
  {path: '/login', name:'login', component:Login},
]
const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router