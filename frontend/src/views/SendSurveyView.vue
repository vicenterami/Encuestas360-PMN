<template>
  <div class="page-container">
    <h2>Enviar Encuesta</h2>
    <form @submit.prevent="sendSurvey">
      <input type="email" placeholder="Correo del cliente" v-model="email" required />
      <button type="submit">Enviar Encuesta</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const email = ref('')

function sendSurvey() {
  alert(`Encuesta enviada a ${email.value} (simulado)`)
}
</script>

<style scoped>
.page-container {
  max-width: 600px;
  margin: auto;
  padding: 2rem;
}

h2 {
  text-align: center;
  margin-bottom: 1.5rem;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

input {
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
}

button:hover {
  background-color: #005fa3;
}
</style>
