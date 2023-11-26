<template>
  <div class="checkout">
    <h1>Resumen de la compra:</h1>
    <h2>
      {{ datosCompra.user.name }} {{ datosCompra.user.lastname }}
    </h2>
    <div v-for="fecha in datosCompra.fechas" :key="fecha.idDia">
      <h3> Día {{ fecha }}: Tickets {{ datosCompra.quantity }}</h3>
    </div>
    <h3>Zona: {{ datosCompra.zones }}</h3>
    <h3>Total a pagar = {{ (datosCompra.quantity * datosCompra.fechas.length) * (valorEntrada + datosCompra.valorAdicional) }}</h3>
    <form class="checkout-form">
      <h2>Inserte los datos de su Tarjeta:</h2>
      <label>Número de Tarjeta</label>
      <input type="number" placeholder="1234 5678 9101 1121" v-model="card_number" />
      <label>Mes de Vencimiento</label>
      <input type="number" placeholder="11"  v-model="card_mes_vencimiento"/>
      <label>Año de Vencimiento</label>
      <input type="number" placeholder="2027"  v-model="card_anio_vencimiento"/>
      <label>Código de Seguridad</label>
      <input type="number" placeholder="123"  v-model="card_ccv"/>
      <button type="submit" @click="buy">Comprar</button>
    </form>
  </div>
</template>
  
<script>
export default {
  data() {
    return {
      datosCompra: JSON.parse(localStorage.getItem("Order")),
      valorEntrada: 5000, 
      card_number: "",
      card_mes_vencimiento: "",
      card_anio_vencimiento: "",
      card_ccv: "",
    };
  },
  methods: {
    buy() {
      console.log( "número de tarjeta" , this.card_number)
      console.log( "Fecha de Vencimiento" , this.card_mes_vencimiento + "/" + this.card_anio_vencimiento)
      console.log( "Código de seguridad" , this.card_ccv)
      alert("¡Gracias por tu compra!");
      this.$router.push('/success');
    },
  
  },
};
</script>


<style>
* {
  margin: 0;
  padding: 0;
}
.checkout {
  background-color: #8099b2;
  color: white;
  text-align: center;
  padding: 5%;
  height: 190vh;
}
.checkout-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3%;
}
.checkout-form input {
  margin-bottom: 3%;
  width:150px;
}
.checkout a {
  width: 20%;
}

</style>