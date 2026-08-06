import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/home.vue'
import Page from '../pages/page.vue'
import Sobre from '../pages/sobre.vue'
import Login from '../pages/login.vue'
import Publicacoes from '../pages/publicacoes.vue'
import Produtos from '../pages/produtos.vue'

const routes = [
  {path: '/', name:'home', component:Home},
  {path: '/publicacoes', name:'publicacoes', component:Publicacoes, meta:{requiresAuth: true}},
  {path: '/produtos', name:'produtos', component:Produtos, meta:{requiresAuth: true}},
  {path: '/sobre', name:'sobre', component:Sobre},
  {path: '/login', name:'login', component:Login},
]
const router = createRouter({
  history: createWebHistory(),
  routes
})

// Guarda de rota que verifica autenticação
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('userToken');

  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login'); // Redireciona para o login se não estiver autenticado
  } else {
    next();
  }
});

export default router