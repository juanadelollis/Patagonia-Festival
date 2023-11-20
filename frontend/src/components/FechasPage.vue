<template>
  <section>
    <form @submit.prevent="checkForm">
      <h1>Elige el día que quieres ir</h1>
      <div class="card-section">
        <div class="card--artista">
          <div v-for="fecha in fechas" :key="fecha.id_dia">
            <h2>Día {{ fecha.numeroDia }}: {{ fecha.headliner }}</h2>
            <h3>{{ fecha.fecha }}</h3>
            <div class="card--content">
              <div>
                <p>{{ fecha.profile_description }}</p>

              </div>
              <img :src="fecha.url_profile_picture" :alt="fecha.headliner" />
            </div>
          </div>
        </div>
      </div>
      <button @click="goToBuy" class="button">Comprar Ahora</button>
    </form>
  </section>
</template>

<script>
export default {
  data() {
    return {
      fechas: [],
      selectedDays: [],
    };
  },
  methods: {
    goToBuy(e) {
      e.preventDefault();
      this.$router.push('/final');
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
    
  }
,
  mounted() {
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
  width: 99.9vw;
  height: 60px;
  margin-top: 10px;
  font-size: 30px;
  background-color: #003366;
  color: #fff;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
}

.input-number{
  width: 60px
}

span{
  margin-left: 20px;
  color:red;
  font-weight: 700;
}

</style>