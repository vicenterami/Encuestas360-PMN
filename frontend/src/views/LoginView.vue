<template>
  <div class="login-container">
    <div class="login-box">
      <h1>Iniciar Sesión</h1>
      <form @submit.prevent="login">
        <input v-model="email" type="text" placeholder="Email" required />
        <input v-model="password" type="password" placeholder="Contraseña" required />
        <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
        <button type="submit">Entrar</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import API from '../api.js'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const errorMessage = ref('')
const router = useRouter()

async function login() {
  try {
    const res = await API.post('/login', {
      email: email.value,
      password: password.value
    });

    if (res.data.success) {
      localStorage.setItem('access_token', res.data.access_token);
      // Usar directamente res.data.is_admin
      router.push(res.data.is_admin ? '/home' : '/survey'); 
    }
  } catch (err) {
    // Mostrar mensaje de error en la interfaz
    errorMessage.value = err.response?.data?.message || 'Error al iniciar sesión.';
  }
}

// Obtener usuarios al cargar
API.get('/usuarios')
  .then(response => {
    console.log(response.data)
  })
  .catch(error => {
    console.error('Error al obtener usuarios:', error)
  })
</script>


<style scoped>
.error-message {
  color: red;
  margin-top: 1rem;
}
</style>

<style scoped>
.login-container {
  width: 100%;
  min-height: 100vh;
  padding: 2rem 1rem;
  display: grid;
  place-items: center;
  background: linear-gradient(to right, #e0eafc, #cfdef3);
  overflow: hidden;
}

.login-box {
  background-color: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  box-sizing: border-box;
}

h1 {
  text-align: center;
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

input {
  padding: 0.75rem 1rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 1rem;
}

button {
  padding: 0.75rem 1rem;
  background-color: #0077cc;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #005fa3;
}

/* Asegura buena visualización en pantallas pequeñas */
@media (max-width: 480px) {
  .login-box {
    padding: 1.5rem;
  }
  h1 {
    font-size: 1.4rem;
  }
  input, button {
    font-size: 0.95rem;
  }
}
</style>
