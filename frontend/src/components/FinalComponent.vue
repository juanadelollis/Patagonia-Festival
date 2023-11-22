
<template>
    <div>
      <div>
        <div class="card-zona">
          <h1>Compra tus Tickets</h1>
          <img src="https://i.imgur.com/ZRz4n7b.png" alt="Mapa plateas" class="Mapa_Plateas">
        </div>
      </div>
      <form class="final" @submit.prevent="buyTickets">
        <div class="form-group">
          <label for="name"> Nombre </label>
          <input v-model="user.name" type="text" id="name">
        </div>
  
        <div class="form-group">
          <label for="lastname"> Apellido </label>
          <input v-model="user.lastname" type="text" id="lastname">
        </div>
  
        <div class="form-group">
          <label for="email"> Email </label>
          <input v-model="user.email" type="email" id="email">
        </div>
  
        <div class="form-group">
          <label for="qty"> Numero de entradas </label>
          <input v-model="numberOfTickers" type="number" id="qty">
        </div>
  
        <div class="form-group">
          <label for="zones-select"> Selecciona la zona</label>
          <select id="zones-select" v-model="selectedZone">
            <option v-for="zone in zones" :key="zone.id" v-bind:value="zone.descripcion">{{zone.descripcion}} </option>
          </select>
        </div>
  
        <div class="form-group">
          <div v-for="fecha in fechas" :key="fecha.id_dia" class="days-checkbox">
            <label> Dia {{fecha.idDia}}: {{fecha.headliner}} </label>
            <input type="checkbox" :value="fecha.fecha" v-model="selectedfechas">
          </div>
        </div>
  
        <button type="submit">Pagar</button>
      </form>

  
      <div v-if="buyResponse">
        <p>Compra realizada con éxito!</p>
        <p>Número de orden: {{ buyResponse.orderNumber }}</p>
      </div>
    </div>
  </template>
  

<script>
export default {
  data() {
    return {
      user: {
        name: "",
        lastname: "",
        email: "",
      },
      fechas: [],
      zones: [],
      selectedZone: "",
      selectedfechas: [],
      numberOfTickers: 0,
      pricePerDay: [],
      buyResponse: null,
    };
  },
  mounted() {
    this.getFechas();
    this.getZonas();
  },
  methods: {


    
    buyTickets() {
  console.log("dias ", this.selectedfechas);
  console.log("zonas ", this.selectedZone);
  console.log("tickets ", this.numberOfTickers);
  console.log("user ", this.user);
  this.calculatePrice();

  const selectedZoneObject = this.zones.find(
    (zona) => zona.descripcion === this.selectedZone
  );
  const valorAdicional = selectedZoneObject.adicional;

  const order = {
    fechas: this.selectedfechas,
    zones: this.selectedZone,
    quantity: this.numberOfTickers,
    user: this.user,
    valorAdicional: valorAdicional,
  };

  fetch("http://localhost:5000/buy", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(order),
  })
    .then((response) => response.json())
    .then((data) => {
      this.buyResponse = data;
    })
    .catch((error) => {
      console.error(error);
    });

  localStorage.setItem("Order", JSON.stringify(order));

  this.$router.push("/checkout");
},
    calculatePrice() {
      this.selectedfechas.forEach((selectedFecha) => {
        this.fechas.forEach((fecha) => {
          if (fecha.numeroDia === selectedFecha) {
            this.pricePerDay.push(fecha.precio);
          }
        });
      });

      const zonePrice = this.zones.find(
        (zona) => zona.descripcion === this.selectedZone
      ).adicional;
      console.log("zonePrice", zonePrice);

      const finalPrice = this.pricePerDay.map(
        (price) => (price + zonePrice) * this.numberOfTickers
      );
      console.log("finalPrice", finalPrice);

      this.$router.push("/checkout");
    },
    getFechas() {
      fetch("http://localhost:5000/fechas", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => {
          if (!resp.ok) {
            throw new Error("Error fetching fechas");
          }
          return resp.json();
        })
        .then((data) => {
          this.fechas = data.fechas.map((fecha) => ({
            ...fecha,
            cantidadEntradas: 0,
          }));
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getZonas() {
      fetch("http://localhost:5000/zones")
        .then((response) => response.json())
        .then((data) => {
          this.zones = data;
          console.log(this.zones);
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style>
.Mapa_Plateas{
    width:60%;
}

.final{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 6% 0%;
    height: 100vh;
    color: black;
    font-size: 25px;
    font-weight: 500;
    background: rgba(0, 51, 102, 0.50);
}
.form-group{
    width: 50%;
    display: flex;
    align-items: center;
    justify-content: space-between;

}

.form-group input{
    width:150px;
    padding-right: 0%;
    
}
.form-group select{
    width:150px;
    
}
.days-checkbox{
    display:flex;

}
</style>