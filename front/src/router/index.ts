import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import ProductView from '../views/ProductView.vue'
import SignupView from '../views/SignupView.vue'
import ShoppingCart from '../views/ShoppingCartView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/cart',
      name: 'cart',
      component: ShoppingCart
    },
    {
      path: '/product-details/:productId', // Déclarez le paramètre dynamique ":productID"
      name: 'product-details',
      component: ProductView,
      props: true // Permet de passer le paramètre en tant que prop au composant
    }
  ]
})

export default router
