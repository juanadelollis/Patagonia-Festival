<template>
    <div class="login-div">
        <h1>Iniciar Sesion</h1>
        <form class="login" @submit="checkUser">
            <input type="text" id="name" v-model="user.name" placeholder="Usuario">
            <input type="password" id="password" v-model="user.password" placeholder="Contraseña">
            <button type="submit">Iniciar Sesion</button>
    
        </form>
        <router-link class="link" to="/account"> Crear Cuenta </router-link>
    </div>
</template>

<script>
export default {
    name: "LoginPage",
    data () {
        return {
            user: {
                name: "",
                password: "",
            }
        }
    },
    methods: {
    checkUser(e) {
    e.preventDefault();

    if (!this.user.name || !this.user.password) {
        alert("Por favor, ingrese nombre de usuario y contraseña.");
        return;
    }

    fetch('http://localhost:5000/api/login', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.user)
    })
    .then(response => {
        if (response.ok) {
            localStorage.setItem('userValidated', this.user.name);
            this.$router.push('/fechas');
        } else {
            alert("Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.");
            console.error('Login failed');
        }
    })
    .catch(error => {
        console.error('Error during login:', error);
    });
}
    }
}

</script>

<style>
.login-div{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 6%;
    height: 100vh;
}

.login{
    background-color: #8099B2;
    text-align: center;
    padding: 20px;
    margin: 3%;
    padding: 3%;
    width: 50%;
}

.login-div h1{
    color: black;
    font-size: 3.5rem;
}

.login input{
    width: 95%;
    height: 2rem;
    margin: 1rem 0;
    padding: 0.5rem;
    border: 1px solid #8099B2;
    border-radius: 4px;
    background-color: #D9D9D9;
}

.login button {
display: flex;
align-items: center;
justify-content: center;
width: 95%;
height: 2.5rem;
padding: 0.8rem 1.8rem;
background-color: #003366;
color: white;
border: none;
border-radius: 4px;
font-size: 1rem;
font-weight: 500;
margin: 2vh 1vw;
}
.login button:hover {
scale: 1.02;
cursor: pointer;
}
.link{
    color: black;
}
</style>

