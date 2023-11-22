<template>
    <div class="myTickets--section">
        <h1>Mis Entradas</h1>
        <div class="tickets">
            <h2 class="tickets--Title">
                {{ datosCompra.user.name }} {{ datosCompra.user.lastname }}
            </h2>
            <div v-for="fecha in datosCompra.fechas" :key="fecha.idDia">
                <h3> Día {{ fecha }}: Tickets {{ datosCompra.quantity }}</h3>
            </div>
            <h3 class="tickets--Title">Zona: {{ datosCompra.zones }}</h3>
            <h3 class="tickets--Title">Total Pagado = {{ datosCompra.quantity * valorEntrada }}</h3>
            
            <img src="https://i.imgur.com/sbuLurE.png" alt="QR CODE">
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      datosCompra: JSON.parse(localStorage.getItem("Order")),
      valorEntrada: 5000, 
    };
  },
  methods: {
  
  },
};
</script>

<style>
* {
    margin: 0;
    padding: 0;
  }

.tickets--Title {
    display:flex;
    align-items: center;
    justify-content: center;
}

.tickets{
    color:black;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-self: center;
    background: rgba(0, 51, 102, 0.50);
    padding-bottom: 40px;

}

.myTickets--section{
    display: flex;
    flex-direction: column;
    justify-content: center;

}
</style>