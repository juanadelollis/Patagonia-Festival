<template>
    <div id="app" class="container mt-5">
    <form @submit.prevent="submitForm">
      <h2 class="mb-4">Formulario de Registro</h2>

      <!-- Nombre -->
      <div class="form-group">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" v-model="usuario.nombre" class="form-control" required>
      </div>

      <!-- Correo electrónico -->
      <div class="form-group">
        <label for="email">Correo Electrónico:</label>
        <input type="email" id="email" v-model="usuario.email" class="form-control" required>
        <small v-if="!validarEmail(usuario.email)" class="text-danger">Ingrese un correo electrónico válido.</small>
      </div>

      <!-- Contraseña -->
      <div class="form-group">
        <label for="password">Contraseña:</label>
        <input type="password" id="password" v-model="usuario.password" class="form-control" required>
      </div>

      <!-- Repetir Contraseña -->
      <div class="form-group">
        <label for="repeatPassword">Repetir Contraseña:</label>
        <input type="password" id="repeatPassword" v-model="usuario.repeatPassword" class="form-control" required>
        <small v-if="usuario.password !== usuario.repeatPassword" class="text-danger">Las contraseñas no coinciden. Por favor, inténtelo de nuevo.</small>
      </div>

      <!-- Botón de envío -->
      <button type="submit" class="btn btn-primary">Registrar</button>
    </form>
  </div>

</template>

<script>
new Vue({
  data: {
    usuario: {
      nombre: '',
      email: '',
      password: '',
      repeatPassword: ''
    }
  },
  methods: {
    submitForm() {
      if (this.validarEmail(this.usuario.email) && this.validarContraseñas()) {
        // Aquí puedes realizar acciones adicionales antes de enviar el formulario
        // Por ejemplo, realizar una solicitud HTTP para registrar al usuario
        console.log('Formulario enviado:', this.usuario);
        alert('¡Usuario registrado con éxito!');
      } else {
        alert('Por favor, revise los campos y asegúrese de que las contraseñas coincidan.');
      }
    },
    validarContraseñas() {
      return this.usuario.password === this.usuario.repeatPassword;
    },
    validarEmail(email) {
      // Validación simple de correo electrónico
      const emailRegex = /\S+@\S+\.\S+/;
      return emailRegex.test(email);
    }
  }
});


</script>

<style>

</style>

