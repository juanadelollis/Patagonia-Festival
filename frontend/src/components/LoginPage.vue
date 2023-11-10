<template>
    <div class="login-div">
        <h1>Iniciar Sesion</h1>
        <form class="login" @submit="checkUser">
            <input type="text" id="name" v-model="user.name" placeholder="Usuario">
            <input type="password" id="password" v-model="user.password" placeholder="Contraseña">
            <button type="submit">Registrarse</button>
    
        </form>
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
            },usuarios:[]
        }
    },
    methods: {
    chechUser(e){
        e.preventDefault();

        fetch('http://localhost:5000/api/login',{
          method:"POST",
          headers:{
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.user)
        })
        .then(resp => resp.json())
        .then(data => {
          let usuarios = data.usuarios;
          console.log(usuarios);
          usuarios.forEach(usuario => {this.usuarios.push(usuario)})
        })
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
</style>

