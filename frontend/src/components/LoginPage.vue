<template>
    <div>
        <h1>Login</h1>
        <form @submit="checkUser">
            <input type="text" v-model="user.name" placeholder="User">
            <input type="password" v-model="user.password" placeholder="Password">
            <input type="submit" value="Login">
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

</style>

