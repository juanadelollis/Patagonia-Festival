<template>
  <div>
    <VideoHero />
    <div class="event-banner">
      <h1 class="title">Conoce nuestro Line Up</h1>
      <div class="banners">
        <div v-for="banner in fechas" :key="banner.idDia" class="banner">
          <img class="img_banner" v-bind:src="banner.url_bannerHomePage" :alt="banner.headliner" />
        </div>
      </div>
      <button @click="reservar">Reserva tus tickets ahora</button>
    </div>

    

    <div class="simple-component">
      <img src="../assets/images/above.png" class="banner-info"/>
      <h2>¿Quiere saber mas del evento?</h2>
      <p>
        Es la primera edicion del mejor festival de primavera para estudiantes
        de la Argentina. El evento se llevara acabo en el Complejo Patagonia.
      </p>
      <p>
        En el Festival Patagonia, cada compás es único: 3 días vibrantes con
        actuaciones de más de 100 artistas, repartidos en 5 escenarios que
        ofrecen diversidad y calidad para todos los gustos. Explora expresiones
        artísticas diversas, disfruta de shows y actividades para los más
        pequeños, saborea una oferta gastronómica que abraza todos los sabores,
        y todo en un entorno de ensueño. ¡Una sinfonía de experiencias!
      </p>
      <button @click="irInformacion">Conoce más</button>
    </div>
  </div>
</template>

<script>
import VideoHero from "./VideoHero.vue";
export default {
  data() {
    return {
      fechas: [],
    };
  },
  props: {
    title: String,
    banners: Array,
  },
  methods: {
    getArticles() {
      fetch("http://localhost:5000/fechas", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          let fechas = data.fechas;
          console.log(fechas);
          fechas.forEach((fecha) => {
            this.fechas.push(fecha);
          });
          //this.articles.push(...data)
        })
        .catch((error) => {
          console.log(error);
        });
    },
    irInformacion() {
      this.$router.push('/informacion');
    },
    reservar() {
      this.$router.push('/fechas');
    },
  },
  //este se llama una vez creado el objeto, ver lifecicle hooks
  created() {
    this.getArticles();
  },
  components: { VideoHero },
};
</script>

<style>
.simple-component {
  text-align: center;
  padding: 5% 10%;
}

.simple-component h2 {
  text-align: center;
  margin-bottom: 3%;
  color: #003366;

}

button {
  background-color: #003366;
  color: #fff;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.event-banner {
  text-align: center;
  background-color: #8099b2;
  padding: 4% 2%;
}

.banners {
  display: flex;
  justify-content: space-between;
  margin: 20px 0;
}

.banner {
  flex: 1;
  margin: 0 10px;
}

.banner-info{
    width: 100%;
}

.img_banner{
  width:100%;
  height:100%;
}
.title{
  padding-bottom: 2%;}

</style>