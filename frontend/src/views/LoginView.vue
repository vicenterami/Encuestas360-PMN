<template>
    <div class="login">
      <h1>Login</h1>
      <form @submit.prevent="login">
        <input v-model="username" placeholder="Usuario" />
        <input v-model="password" type="password" placeholder="Contraseña" />
        <button>Entrar</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  const username = ref('')
  const password = ref('')
  function login() {
    // Aquí irá la llamada a Flask
    alert(`Intento de login: ${username.value}`)
  }
  </script>
  