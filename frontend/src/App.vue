<script setup>
</script>

<template>
  
  <nav>
    <router-link to="/">Login</router-link>
    <router-link to="/register">Register</router-link>
    <router-link to="/home">Home</router-link>
    <router-link to="/survey">Encuesta</router-link>
    <router-link to="/create-survey">Crear Encuesta</router-link>
    <router-link to="/send-survey">Enviar Encuesta</router-link>
    <router-link to="/clients">Clientes</router-link>
    <router-link to="/search-clients">Buscar Clientes</router-link>
    <router-link to="/results">Resultados</router-link>
    <router-link to="/history">Historial</router-link>
    <router-link to="/support">Soporte</router-link>
  </nav>

  <main>
    <router-view />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}
</style>