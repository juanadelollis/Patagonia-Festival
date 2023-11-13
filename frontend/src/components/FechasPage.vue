<template>
  <section>
    <form>
      <h1>Elige el día que quieres ir</h1>
      <div class="card-section">
        <div class="card--artista">
          <div v-for="fecha in fechas" :key="fecha.id_dia">
            <h2>Día {{ fecha.numeroDia }}: {{ fecha.headliner }}</h2>
            <h3>{{ fecha.fecha }}</h3>
            <div class="card--content">
              <div>
                <p>{{ fecha.profile_description }}</p>
                <label for="">Cantidad de entradas</label>
                <br>
                <input type="number" required v-bind:name="fecha.headliner" v-model="fecha.cantidadEntradas">
                <span v-if="!esCantidadValida(fecha.cantidadEntradas)">Ingrese una cantidad válida</span>
              </div>
              <img v-bind:src="fecha.url_profile_picture" v-bind:alt="fecha.headliner">
            </div>
          </div>
        </div>
      </div>
      <router-link class="button" to="/zonas" @click="reservar">Siguiente Etapa</router-link>
    </form>
  </section>
</template>

<script>
export default {
  data() {
    return {
      fechas: [],
    };
  },
  methods: {
    chechForm(e) {
      e.preventDefault();
      function getFechas() {
        fetch("http://localhost:5000/fechas", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((resp) => resp.json())
          .then((data) => {
            let fechas = data.fechas;
            // let bandas = data.fechas.banda
            console.log(fechas);
            fechas.forEach((fecha) => {
              this.fechas.push(fecha);
            });
            //this.articles.push(...data)
          })
          .catch((error) => {
            console.log(error);
          });

      function esCantidadValida(cantidad) {
          return cantidad > 0;
        }
      }

      function handleCounterChange({ name, value }) {
        localStorage.setItem(name, value);
      }
    }
  },
  //este se llama una vez creado el objeto, ver lifecicle hooks
  created() {
    this.getFechas();
  },
};
</script>

<style>
.card--artista {
  width: 40%;
}

.card--content {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.card--content p {
  width: 90%;
  font-size: 26px;
}

.card-section {
  display: flex;
  align-content: center;
  justify-content: center;
}

h2,
h3 {
  display: flex;
  justify-content: flex-start;
  font-weight: bold;
  width: 85%;
}

h2 {
  font-size: 30px;
}

h1 {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px;
}

.button {
  text-decoration: none;
  display: flex;
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