<template>
  <div>

    <div class="header">
        <h1>LA MÚSICA ESTÁ EN NUESTRO ADN</h1>
        <h3>Lo que sucede en Patagonia Fest no tiene comparación:
            3 días con shows de más de 100 artistas, en 5 escenarios
            con variedad y calidad para que todos disfruten.
            Diferentes expresiones artísticas, shows y actividades infantiles,
            una oferta gastronómica para todos los gustos y una locación de ensueño!
        </h3>
    </div>
    <div class="info">
        <h2>Patagonia Festival</h2>
        <p>Podrás disfrutar del festival Patagonia 
        el 21, 22 y 23 de septiembre del 2024.
        El mismo se realizará en el Complejo Patagonia,
        ubicado en Av. Alvarez Thomas 700, Bariloche,
        Provincia de Rio Negro.</p>
        
    </div>
    <div class="info">
        <h2>Patagonia Food</h2>
        <p>¡La gastronomía también es una fiesta!
            Con opciones para todos los gustos en
            5 patios gastronómicos con más de 50
            puestos y más de 100 opciones,
            celebrando cocinas de todo el mundo,
            atendiendo a las necesidades de todos
            los paladares y elevando la vara de la
            calidad año tras año.
        </p>
    </div>
    <div class="info">
        <h2>Patagonia Spirit</h2>
        <p>Lo que vuelve único a #PatagoniaFest es la
            magia que se da durante esos 3 días. El 
            el cruce perfecto entre movimientos 
            artísticos y la naturaleza. Cada edición 
            cinsiste de grandes artistas locales e
            internacionales para convertir a la 
            Patagonia en una fiesta completa, con 
            instalaciones, arte digital, naturaleza y
            musica para que conectes al maximo.
        </p>
    </div>
  </div>

</template>

<script>
export default {

  data(){
    return {
      fechas:[],
      selectedDays: [],
    }
  },
    methods:{ 
      getFechas(){
        fetch('http://localhost:5000/fechas',{
          method:"GET",
          headers:{
            'Content-Type': 'application/json'
          }
        })
        .then(resp => resp.json())
        .then(data => {
          let fechas = data.fechas;
          // let bandas = data.fechas.banda
          console.log(fechas);
          fechas.forEach(fecha => {this.fechas.push(fecha)})
          //this.articles.push(...data)
        })
        .catch(error =>{
          console.log(error);
        })
      },
      saveDays(e){
        e.preventDefault()
        console.log(this.selectedDays)
        const daysToSave = []
        this.selectedDays.forEach( fecha => 
        {
          const obj = {
            id_dia: fecha,
            numero_dia: fecha
          }
          daysToSave.push(obj)
        }
        )
        localStorage.setItem("purchase", JSON.stringify({dias: daysToSave}))
        this.$router.push("/")
      }
    },
    // mounted(){
    //   fetch("http://localhost:5000/fechas")
    //   .then(response => response.json()).
    //   then(data => 
    //   this.fechas=data)  //actualiza data tomando lo que trae de backend
    // }
    //este se llama una vez creado el objeto, ver lifecicle hooks
    created(){
      this.getFechas();
    }
  }
</script>

<style>
    *{
        padding: 0;
        margin: 0;
    }
    .header{
        background-color: #8099B2;
        color: white;
        text-align: center;
        padding: 5%
    }
    .header h1{
        color: #003366;
        padding-bottom: 2%
    }
    .info{
        background-color: #6F6F6F;
        padding: 3% 10%;
        color: white;
    }
</style>