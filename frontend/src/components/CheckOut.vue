<template>
    <div class="checkout">
            <h1>Checkout</h1>
            <h2>Dias seleccionados</h2>
            <div v-for="fecha in fechas" :key="fecha.idDia">
                <h3>Dia {{fecha.numeroDia}}: {{fecha.headliner}}</h3>
                <h4>Fecha del Boleto: {{fecha.fecha}}</h4>
            </div>
        <form class="checkout-form">
            <label>Número de Tarjeta</label>
            <input type="number" placeholder="1234 5678 9101 1121">
            <label for="">Mes de Vencimiento</label>
            <input type="number">
            <label for="">Año de Vencimiento</label>
            <input type="number">
            <label for="">Código de Seguridad</label>
            <input type="number">
            <button type="submit" v-on:click="buy" >Comprar</button>
        </form>
    </div>
</template>

<script>
export default {
    data(){
        return{
            quantity: 0,
            fechas: []
        }
    },
    mounted(){
        let purchase = JSON.parse(localStorage.getItem("purchase")).dias
        this.fechas = purchase
    },
    methods:{
        buy (){
            localStorage.setItem("quantity", JSON.stringify(this.quantity))
        }
    }   
}
</script>

<style>
    *{
        margin: 0;
        padding: 0;
    }
    .checkout{
        background-color: #8099B2;
        color: white;
        text-align: center;
        padding: 5%;
        height: 100vh;
    }
    .checkout-form{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 3%;
    }
    .checkout-form input{
        margin-bottom: 3%;
    }
    .checkout a{
        width: 20%;
    }
</style>