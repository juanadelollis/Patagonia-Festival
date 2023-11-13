<template>
    <main>
        <div class="card-zona">
            <h2>Elige la zona</h2>
            <img src="../assets/images/Mapa_Plateas.svg" alt="Mapa plateas" class="Mapa_Plateas">
            <form @submit.prevent="checkForm">

                <div class="card-content-zona">                
                    <input type="radio" name="concert-zona" id="Campo" value="Campo" v-model="selectedZona">
                    <div class="zona-description">
                        <h3>Campo</h3>
                        <h4>Precio $100.000</h4>
                        <p class="description">Ofrece la mejor vista al escenario para vivir el concierto de cerca. Asegura tu entrada y sé parte de una experiencia musical inolvidable.</p>
                    </div>
                </div>
                
                <div class="card-content-zona">                
                    <input type="radio" name="concert-zona" id="Platea" value="Platea" v-model="selectedZona">
                    <div class="zona-description">
                        <h3>Platea</h3>
                        <h4>Precio $50.000</h4>
                        <p class="description">Ofrece comodidad y una vista óptima del escenario, proporcionando una experiencia única para disfrutar del concierto con detalle y estilo. Con amplio espacio y ubicación estratégica, tu asiento en la Platea asegura una vivencia inigualable para sumergirte en la magia de la música.</p>
                    </div>
                </div>
                <button class="button">Siguiente Etapa</button>
            </form>
        </div>
    </main>
        
</template>

<script>
export default {
data(){
    return{
        selectedZona:"",
    };
},
methods:{
    checkForm(e) {
      e.preventDefault();

      const datosCompra = JSON.parse(localStorage.getItem('datos')) || {};
      datosCompra.zona = this.selectedZona;

        localStorage.setItem('datos', JSON.stringify(datosCompra));

      this.$router.push('/checkout');
    },

}


};     

</script>
<style>

h2{
    align-self  : center;
    font-size: 60px;
}

.card-zona{
    display:flex;
    flex-direction:column;
    justify-content: flex-start;
}

.Mapa_Plateas {
    width: 30%;
    align-self: center;
    justify-self: center;
}
.card-content-zona {
    background-color: #88b280;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    padding: 8px;
}

.zona-description {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

h3 {
    display: flex;
    justify-content: flex-start;
    font-weight: bold;
}

p{
    display: flex;
    justify-self: flex-start;

}


input{
    height: 30px;
    width:30px;
    align-self: center;
    justify-content: center;
}

.button{
    text-decoration:none;
    display:flex;
    justify-content: center;
    width: 100vw;
    height: 60px;
    margin-top: 10px;
    font-size: 30px;
    background-color: #003366;
    color: #fff;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
  }

</style>