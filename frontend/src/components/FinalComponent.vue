<template>
<div>
    <div>
            <div class="card-zona">
                <h1>Compra tus Tickets</h1>
                <img src="../assets/images/Mapa_Plateas.svg" alt="Mapa plateas" class="Mapa_Plateas">

                <div class="card-content-zona">                
                    <div class="zona-description">
                        <h3>Campo</h3>
                        <h4>Precio $100.000</h4>
                        <p class="description">Ofrece la mejor vista al escenario para vivir el concierto de cerca. Asegura tu entrada y sé parte de una experiencia musical inolvidable.</p>
                    </div>
                </div>
                <div class="card-content-zona">                
                    <div class="zona-description">
                        <h3>Platea</h3>
                        <h4>Precio $50.000</h4>
                        <p class="description">Ofrece comodidad y una vista óptima del escenario, proporcionando una experiencia única para disfrutar del concierto con detalle y estilo. Con amplio espacio y ubicación estratégica, tu asiento en la Platea asegura una vivencia inigualable para sumergirte en la magia de la música.</p>
                    </div>
                </div>
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
                <input type="checkbox" :value="fecha.numeroDia" v-model="selectedfechas">
            </div>
        </div>
        <button type="submit">Pagar</button>
    </form>
</div>
</template>

<script>
export default {
    data(){
        return {
            user: {
                name: "",
                lastname: "",
                email: ""
            },
            dia: [],
            zones: [],
            selectedZone: "",
            selectedfechas: [],
            numberOfTickers: 0,
            pricePerDay: []

        }
    },mounted () {
        this.getFechas(),
        this.getZonas()


        
    }, methods: {
        buyTickets(){
            console.log("dias ", this.selectedfechas)
            console.log("zonas ", this.selectedZone)
            console.log("tickets ", this.numberOfTickers)
            console.log("user ", this.user)
            this.calculatePrice()

            const purchase = {
                fechas: this.selectedfechas,
                zones: this.selectedZone,
                quantity: this.numberOfTickers,
                user: this.user
            }
 

        fetch("http://localhost:5000/buy", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(purchase),
        }).then(response => response.json()).
        then(data=> console.log(data))

        },
        calculatePrice(){
            this.selectedfechas.forEach(selectedDay =>{
                this.fechas.forEach(day => {
                    if(day.numeroDia === selectedDay){
                        this.pricePerDay.push(day.precio)
                    }
            }) }
            )
            const zonePrice = this.zones.find(zona => zona.descripcion === this.selectedZone).adicional
            console.log("zonePrice", zonePrice)
            const finalPrice = this.pricePerDay.map(price => (price + zonePrice) * this.numberOfTickers)
            console.log("finalPrice", finalPrice)

            const order = {
                fechas: this.selectedfechas,
                zones: this.selectedZone,
                quantity: this.numberOfTickers,
                user: this.user,
                finalPrice: finalPrice
            }
            
            localStorage.setItem("Order", JSON.stringify(order));
            this.$router.push('/checkout');

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
        getZonas(){
        fetch("http://localhost:5000/zones")
        .then(response =>response.json()).
            then(data => {
            this.zones = data           
            console.log(this.zones)
            }
        ).catch(error => console.log(error));
        },
    

    
    }

}
</script>

<style>
.final{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 6% 0%;
    height: 100vh;

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