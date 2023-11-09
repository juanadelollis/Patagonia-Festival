<template>
  <div class="container mt-5">
    <div v-for="fecha in fechas" :key="fecha.id_dia">
        <h3>Dia {{fecha.numero_dia}}: {{fecha.headliner}}</h3>
        <h4>{{fecha.fecha}}</h4>
          
    </div>
  </div>
</template>

<script>
export default {

  data(){
    return {
      fechas:[],
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
      }
    },
    //este se llama una vez creado el objeto, ver lifecicle hooks
    created(){
      this.getFechas();
    }
  }
</script>

<style>

</style>