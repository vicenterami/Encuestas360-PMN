<template>
    <div class="page-container">
      <h2>Responder Encuesta</h2>
      <form @submit.prevent="submitResponse">
        <label>¿Cómo calificarías nuestro servicio?</label>
        <select v-model="response" required>
          <option disabled value="">Seleccione</option>
          <option>Excelente</option>
          <option>Bueno</option>
          <option>Regular</option>
          <option>Malo</option>
        </select>
        <button type="submit">Enviar Respuesta</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const response = ref('')
  
  function submitResponse() {
    alert(`Respuesta enviada: ${response.value} (simulado)`)
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
  
  select {
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
  