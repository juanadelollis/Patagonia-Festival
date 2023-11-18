<template>
    <div class="account-div">
      <h1>Crear Cuenta</h1>
        <form class="account" @submit.prevent="submitForm">
            <input type="text" id="name" v-model="user.name" placeholder="Usuario">
            <input type="password" id="password" v-model="user.password" placeholder="Contraseña">
            <input type="password" id="repeatPassword" v-model="user.repeatPassword" placeholder="Repetir Contraseña">
            <button type="submit">Crear Cuenta</button>
        </form>
    </div>

</template>

<script>
export default { 
  data(){
    return{
      user: {
        name: "",
        password: "",
        repeatPassword: "",
      },
    };
  },
  methods: {
    validarContraseñas() {
      if (this.user.password === this.user.repeatPassword){
        return ("Usuario Creado")}  
},
},
};
</script>

<style>
*{
    padding: 0;
    margin: 0;
}
.account-div{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 6%;
    height: 100vh;
}

.account{
    background-color: #8099B2;
    text-align: center;
    padding: 20px;
    margin: 3%;
    padding: 3%;
    width: 50%;
}

.account-div h1{
    color: black;
    font-size: 3.5rem;
}

.account input{
    width: 95%;
    height: 2rem;
    margin: 1rem 0;
    padding: 0.5rem;
    border: 1px solid #8099B2;
    border-radius: 4px;
    background-color: #D9D9D9;
}

.account button {
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
.account button:hover {
    scale: 1.02;
    cursor: pointer;
}

</style>

