import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import ProductView from '../views/ProductView.vue'
import InscriptionView from '../views/Inscription.vue'
import ShoppingCart from '../views/ShoppingCartView.vue'
import SuccessView from '../views/SuccessView.vue'
import SearchView from '@/views/SearchView.vue'
import CancelPaymentView from '@/views/CancelPaymentView.vue'

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
      path: '/inscription',
      name: 'inscription ',
      component: InscriptionView
    },
    {
      path: '/cart',
      name: 'cart',
      component: ShoppingCart
    },
    {
      path: '/success',
      name: 'success',
      component: SuccessView
    },
    {
      path: '/cancel-payment',
      name: 'cancel',
      component: CancelPaymentView
    },
    {
      path: '/search/:searched',
      name: 'search',
      component: SearchView,
      props: true
    },
    {
      path: '/product-details/:productId',
      name: 'product-details',
      component: ProductView,
      props: true
    }
  ]
})

export default router
