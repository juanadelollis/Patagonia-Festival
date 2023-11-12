import { createRouter, createWebHistory } from "vue-router";
import HomePage from './components/HomePage'
import FechasPage from './components/FechasPage'
import LoginPage from './components/LoginPage'
import InfoPage from './components/InfoPage'
import CheckOut from './components/CheckOut'
import ZonasPage from './components/ZonasPage'

//Acá definimos las rutas
const routes = [
    {
        path: '/', //para la home page
        name: 'home',
        component:HomePage
    },
    {
        path: '/zonas', //para la create page
        name: 'zonas',
        component:ZonasPage
    },
    {
        path: '/fechas', //para la fechas page
        name: 'fechas',
        component: FechasPage
    },
    {
        path: '/login', //para la login page
        name: 'login',
        component: LoginPage
    }
    ,
    {
        path: '/informacion', //para la login page
        name: 'info',
        component: InfoPage
    },
    {
        path: '/checkout', //para la check page
        name: 'checkout',
        component: CheckOut
    }
    
]

const router = createRouter({
    history:createWebHistory(), //Navegación por defecto
    routes,
}) 

export default router;