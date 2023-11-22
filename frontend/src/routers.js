import { createRouter, createWebHistory } from "vue-router";
import HomePage from './components/HomePage'
import FechasPage from './components/FechasPage'
import LoginPage from './components/LoginPage'
import InfoPage from './components/InfoPage'
import CheckOut from './components/CheckOut'
import ZonasPage from './components/ZonasPage'
import CreateAccountComponent from './components/CreateAccountComponent'
import FinalComponent from './components/FinalComponent'
import SucessComponent from './components/SucessComponent'

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
    },
    {
        path: '/account', //para la final component
        name: 'account',
        component: CreateAccountComponent
    },
    {
        path: '/final', //para la final component
        name: 'final',
        component: FinalComponent
    },
    {
        path: '/success', //para la final component
        name: 'success',
        component: SucessComponent
    }
    
]

const router = createRouter({
    history:createWebHistory(), //Navegación por defecto
    routes,
}) 

export default router;