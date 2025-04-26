<template>
    <div class="page-container">
      <h2>Clientes Registrados</h2>
  
      <!-- Formulario para agregar nuevo cliente -->
      <form class="add-client-form" @submit.prevent="addClient">
        <input v-model="newName" type="text" placeholder="Nombre Completo" required />
        <input v-model="newEmail" type="email" placeholder="Correo Electrónico" required />
        <button type="submit">Agregar Cliente</button>
      </form>
  
      <!-- Tabla de clientes -->
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Email</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="client in clients" :key="client.id">
            <td>{{ client.name }}</td>
            <td>{{ client.email }}</td>
            <td class="acciones">
              <button @click="editClient(client)">✏️</button>
              <button @click="deleteClient(client)">🗑️</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const clients = ref([
    { id: 1, name: 'Juan Pérez', email: 'juan@example.com' },
    { id: 2, name: 'Ana López', email: 'ana@example.com' },
  ])
  
  const newName = ref('')
  const newEmail = ref('')
  
  function addClient() {
    const newClient = {
      id: Date.now(),
      name: newName.value,
      email: newEmail.value
    }
    clients.value.push(newClient)
    alert(`Cliente ${newClient.name} agregado (simulado)`)
    newName.value = ''
    newEmail.value = ''
  }
  
  function editClient(client) {
    alert(`Editar cliente: ${client.name} (simulado)`)
  }
  
  function deleteClient(client) {
    if (confirm(`¿Seguro que quieres eliminar a ${client.name}?`)) {
      clients.value = clients.value.filter(c => c.id !== client.id)
      alert(`Cliente eliminado (simulado)`)
    }
  }
  </script>
  
  <style scoped>
  .page-container {
    max-width: 800px;
    margin: auto;
    padding: 2rem;
  }
  
  .add-client-form {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
  }
  
  .add-client-form input {
    flex: 1;
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 6px;
  }
  
  .add-client-form button {
    padding: 0.75rem;
    background-color: #0077cc;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
  }
  
  .add-client-form button:hover {
    background-color: #005fa3;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
  }
  
  th, td {
    padding: 0.75rem;
    border: 1px solid #ccc;
    text-align: center;
  }
  
  th {
    background-color: #0077cc;
    color: white;
  }
  
  td {
    background-color: white;
  }
  
  .acciones {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
  }
  
  .acciones button {
    padding: 0.3rem 0.6rem;
    background-color: transparent;
    border: none;
    cursor: pointer;
    font-size: 1.2rem;
  }
  
  .acciones button:hover {
    background-color: #e0eafc;
    border-radius: 6px;
  }
  </style>
  