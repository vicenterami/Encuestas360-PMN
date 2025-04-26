<template>
    <div class="page-container">
      <h2>Soporte Técnico</h2>
      <p>Si tienes algún problema técnico, por favor contáctanos.</p>
      <button @click="reportIssue">Reportar un problema</button>
    </div>
  </template>
  
  <script setup>
  function reportIssue() {
    alert('Se ha reportado el problema (simulado)')
  }
  </script>
  
  <style scoped>
  .page-container {
    max-width: 600px;
    margin: auto;
    padding: 2rem;
    text-align: center;
  }
  
  button {
    margin-top: 1rem;
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
  