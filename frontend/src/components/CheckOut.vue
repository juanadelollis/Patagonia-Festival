<template>
  <div class="checkout">
    <h1>Checkout</h1>
    <h2>Resumen de la compra:</h2>
    <div v-for="fecha in fechas" :key="fecha.idDia">
      <h3>Día {{ fecha.numeroDia }}: {{ fecha.headliner }}</h3>
      <h4>Fecha del Boleto: {{ fecha.fecha }}</h4>
      <p>
        Cantidad de Entradas {{ datosCompra.dias[fecha.headliner] }} x
        {{ valorEntrada }}
      </p>
      <p>
        <b>{{ datosCompra.dias[fecha.headliner] * valorEntrada }}</b>
      </p>
    </div>
    <h3>Total a pagar = {{ CantidadPagar }}</h3>
    <form class="checkout-form">
      <h2>Inserte los datos de su Tarjeta:</h2>
      <label>Número de Tarjeta</label>
      <input type="number" placeholder="1234 5678 9101 1121" />
      <label>Mes de Vencimiento</label>
      <input type="number" placeholder="11"/>
      <label>Año de Vencimiento</label>
      <input type="number" placeholder="2027"/>
      <label>Código de Seguridad</label>
      <input type="number" placeholder="123" />
      <button type="submit" @click="buy">Comprar</button>
    </form>
  </div>
</template>
  
  <script>
export default {
  data() {
    return {
      datosCompra: JSON.parse(localStorage.getItem("datos")) || {},
      fechas: [],
    };
  },
  computed: {
    valorEntrada() {
      const nombreZona = this.datosCompra.zona;
      return nombreZona === "Campo"
        ? 50000
        : nombreZona === "Platea"
        ? 100000
        : 0;
    },
    CantidadPagar() {
      let CatidadTotal = 0;
      for (const key in this.datosCompra.dias) {
        const cantidad = this.datosCompra.dias[key] || 0;
        CatidadTotal += cantidad * this.valorEntrada;
      }
      return CatidadTotal;
    },
  },
  mounted() {
    this.getFechas();
  },
  methods: {
    getFechas() {
      fetch("http://localhost:5000/fechas", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.fechas = data.fechas.map((fecha) => ({
            ...fecha,
            cantidadEntradas: 0,
          }));
        })
        .catch((error) => {
          console.log(error);
        });
    },
    buy() {
    this.$router.push('/');
    alert("¡Gracias por tu compra!");
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