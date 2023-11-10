import { createRouter, createWebHistory } from "vue-router";
import HomePage from './components/HomePage'
import CreatePage from './components/CreatePage'
import FechasPage from './components/FechasPage'
import LoginPage from './components/LoginPage'
import InfoPage from './components/InfoPage'
import CheckOut from './components/CheckOut'


//Acá definimos las rutas
const routes = [
    {
        path: '/', //para la home page
        name: 'home',
        component:HomePage
    },
    {
        path: '/create', //para la create page
        name: 'create',
        component:CreatePage
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
<<<<<<< HEAD
=======
    
>>>>>>> 3794052cdf7d5501798accc586141db020a8463a
]

const router = createRouter({
    history:createWebHistory(), //Navegación por defecto
    routes,
}) 

export default router;