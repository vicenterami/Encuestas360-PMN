<template>
  <div class="home-container">
    <header>
      <h1>Panel de Administración - Encuestas360</h1>
      <p>Bienvenido, Administrador</p>
    </header>

    <main>
      <section>
        <h2>Crear Nueva Encuesta</h2>
        <button @click="goTo('/create-survey')">Comenzar Encuesta</button>
      </section>

      <section>
        <h2>Resultados de Encuestas</h2>
        <button @click="goTo('/results')">Ver Resultados</button>
      </section>

      <section>
        <h2>Buscar Clientes</h2>
        <button @click="goTo('/search-clients')">Buscar Clientes</button>
      </section>

      <section>
        <h2>Administrar Clientes</h2>
        <button @click="goTo('/clients')">Administrar</button>
      </section>

      <section>
        <h2>Historial de Encuestas</h2>
        <button @click="goTo('/history')">Ver Historial</button>
      </section>

      <section>
        <h2>Soporte Técnico</h2>
        <button @click="goTo('/support')">Soporte</button>
      </section>
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

function goTo(route) {
  router.push(route)
}
</script>

<style scoped>
.home-container {
  padding: 1rem;
  max-width: 800px;
  margin: auto;
}

header {
  background-color: #0077cc;
  color: white;
  padding: 1rem;
  border-radius: 10px;
  margin-bottom: 2rem;
}

main section {
  background: white;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 1rem;
}

button {
  margin-top: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: #0077cc;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
