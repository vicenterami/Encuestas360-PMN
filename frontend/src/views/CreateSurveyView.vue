<template>
  <div class="page-container">
    <h2>Crear Encuesta</h2>
    <form @submit.prevent="createSurvey">
      <input type="text" placeholder="Título de la encuesta" v-model="title" required />
      <textarea placeholder="Descripción" v-model="description"></textarea>
      <button type="submit">Guardar Encuesta</button>
    </form>

    <div class="enviar-encuesta">
      <h3>¿Deseas enviar la encuesta ahora?</h3>
      <button @click="goToSendSurvey">Ir a Enviar Encuesta</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const title = ref('')
const description = ref('')
const router = useRouter()

function createSurvey() {
  alert(`Encuesta "${title.value}" creada (simulado)`)
}

function goToSendSurvey() {
  router.push('/send-survey')
}
</script>

<style scoped>
.page-container {
  max-width: 800px;
  margin: auto;
  padding: 2rem;
}

h2, h3 {
  text-align: center;
  margin-bottom: 1.5rem;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

input, textarea {
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 6px;
}

button {
  padding: 0.75rem;
  background-color: #0077cc;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  margin-top: 1rem;
}

button:hover {
  background-color: #005fa3;
}

.enviar-encuesta {
  margin-top: 2rem;
  text-align: center;
}
</style>
