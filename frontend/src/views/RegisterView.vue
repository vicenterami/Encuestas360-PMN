<template>
  <div class="login-container">
    <div class="login-box">
      <h1>Registro de Cliente</h1>
      <form @submit.prevent="register">
        <input v-model="name" type="text" placeholder="Nombre Completo" required />
        <input v-model="email" type="email" placeholder="Correo Electrónico" required />
        <input v-model="password" type="password" placeholder="Contraseña" required />
        <input v-model="phone_number" type="text" placeholder="Número de Teléfono" />
        <input v-model="address_id" type="number" placeholder="ID de Dirección" />
        <select v-model="gender_id">
          <option disabled value="">Seleccione Género</option>
          <option value="1">Masculino</option>
          <option value="2">Femenino</option>
          <option value="3">Otro</option>
        </select>
        <button type="submit">Registrarse</button>
      </form>
      <p v-if="errorMessage" style="color:red;">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import API from '../api.js'
import { useRouter } from 'vue-router'

const name = ref('')
const email = ref('')
const password = ref('')
const phone_number = ref('')
const address_id = ref('')
const gender_id = ref('')
const errorMessage = ref('')
const router = useRouter()

async function register() {
  try {
    const res = await API.post('/register', {
      name: name.value,
      email: email.value,
      password: password.value,
      phone_number: phone_number.value || null,
      address_id: address_id.value ? parseInt(address_id.value) : null,
      gender_id: gender_id.value ? parseInt(gender_id.value) : null
    })
    if (res.data.success) {
      alert('Registro exitoso. Ahora puedes iniciar sesión.')
      router.push('/')
    } else {
      errorMessage.value = res.data.message || 'Error desconocido.'
    }
  } catch (err) {
    errorMessage.value = err.response?.data?.message || 'Error al registrar.'
  }
}
</script>

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

input, select {
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

@media (max-width: 480px) {
  .login-box {
    padding: 1.5rem;
  }
  h1 {
    font-size: 1.4rem;
  }
  input, button, select {
    font-size: 0.95rem;
  }
}
</style>
