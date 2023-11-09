<template>
 <VideoHero/>
    <div class="event-banner">
        <h1> Conoce nuestro Line Up</h1>
        <div class="banners">
            <div v-for="banner in banners" :key="banner.id" class="banner">
                <img :src="banner.image" :alt="banner.alt" />
            </div>
        </div>
        <button @click="reservar">Reserva tus tickets ahora</button>
    </div>

    <div class="simple-component">
        <h2> ¿Quiere saber mas del evento? </h2>
        <p>Es la primera edicion del mejor festival de 
        primavera para estudiantes de la Argentina.
        El evento se llevara acabo en el Complejo Patagonia.</p>
        <p> En el Festival Patagonia, cada compás es único:
        3 días vibrantes con actuaciones de más de 100 artistas, repartidos en 5 escenarios
        que ofrecen diversidad y calidad para todos los gustos.
        Explora expresiones artísticas diversas, disfruta de shows y actividades para los más pequeños,
        saborea una oferta gastronómica que abraza todos los sabores, y todo en un entorno de ensueño. ¡Una sinfonía de experiencias!</p>
      <button @click="onButtonClick">Conoce más</button>
    </div>

</template>

<script>
import VideoHero from './VideoHero.vue'
export default {
    data() {
        return {
            articles: [],
        };
    },
    props: {
    title: String,
    banners: Array,
    },
    methods: {
        getArticles() {
            fetch('http://localhost:5000/articles', {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(resp => resp.json())
                .then(data => {
                let articulos = data.articles;
                console.log(articulos);
                articulos.forEach(articulo => { this.articles.push(articulo); });
                //this.articles.push(...data)
            })
                .catch(error => {
                console.log(error);
            });
        },
        onButtonClick() {
            // Lógica que se ejecutará cuando se haga clic en el botón
        },
        reservar() {
        // Lógica para reservar tus tickets
        // Puedes redirigir a una página de reserva o realizar alguna acción específica aquí
    },

    },
    //este se llama una vez creado el objeto, ver lifecicle hooks
    created() {
        this.getArticles();
    },
    components: { VideoHero }
}
</script>

<style>
    .simple-component {
    text-align: center;
    padding: 5% 13%;
    
  }

  .simple-component h2{
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
  background-color: #8099B2;

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


</style>