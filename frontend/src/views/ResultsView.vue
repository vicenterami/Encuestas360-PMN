<template>
    <canvas id="grafico" width="400" height="200"></canvas>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
  import Chart from 'chart.js/auto'
  
  onMounted(() => {
    new Chart(document.getElementById('grafico'), {
      type: 'bar',
      data: {
        labels: ['Excelente', 'Bueno', 'Regular', 'Malo'],
        datasets: [{
          label: 'Respuestas',
          data: [20, 15, 5, 1],
          backgroundColor: ['#0077cc', '#00b4d8', '#90e0ef', '#caf0f8']
        }]
      }
    })
  })
  </script>
  