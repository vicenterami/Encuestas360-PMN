<template>
    <div class="page-container">
      <h2>Buscar Clientes</h2>
      <input type="text" v-model="search" placeholder="Buscar por nombre o email" />
      <ul>
        <li v-for="client in filteredClients" :key="client.id">{{ client.name }} ({{ client.email }})</li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  
  const search = ref('')
  const clients = ref([
    { id: 1, name: 'Juan Pérez', email: 'juan@example.com' },
    { id: 2, name: 'Ana López', email: 'ana@example.com' },
  ])
  
  const filteredClients = computed(() => {
    return clients.value.filter(c => 
      c.name.toLowerCase().includes(search.value.toLowerCase()) ||
      c.email.toLowerCase().includes(search.value.toLowerCase())
    )
  })
  </script>
  
  <style scoped>
  .page-container {
    max-width: 800px;
    margin: auto;
    padding: 2rem;
  }
  
  h2 {
    text-align: center;
    margin-bottom: 1.5rem;
  }
  
  input {
    padding: 0.75rem;
    width: 100%;
    border: 1px solid #ccc;
    border-radius: 6px;
    margin-bottom: 1rem;
  }
  
  ul {
    list-style: none;
    padding: 0;
  }
  
  li {
    background: white;
    padding: 0.75rem;
    margin-bottom: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 6px;
  }
  </style>
  