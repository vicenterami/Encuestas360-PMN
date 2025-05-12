<template>
  <div class="page-container">
    <h2>Crear Encuesta</h2>
    <form @submit.prevent="submitSurvey">
      <input type="text" 
             placeholder="Título de la encuesta" 
             v-model="form.title" 
             required />
      
      <textarea placeholder="Descripción" 
                v-model="form.description"></textarea>

      <!-- Sección de Preguntas Dinámicas -->
      <div v-for="(question, index) in form.questions" 
           :key="index" 
           class="question-item">
        <input type="text" 
               placeholder="Texto de la pregunta" 
               v-model="question.text" 
               required>
        
        <select v-model="question.type" class="type-selector">
          <option value="1">Opción múltiple</option>
          <option value="2">Texto abierto</option>
        </select>
        
        <button type="button" 
                @click="removeQuestion(index)" 
                class="btn-remove">
          ✕
        </button>
      </div>

      <div class="button-group">
        <button type="button" 
                @click="addQuestion" 
                class="btn-add-question">
          ＋ Añadir Pregunta
        </button>
        
        <button type="submit" class="btn-save">
          Guardar Encuesta
        </button>
      </div>
    </form>

    <div class="enviar-encuesta">
      <h3>¿Deseas enviar la encuesta ahora?</h3>
      <button @click="goToSendSurvey" class="btn-send">
        Ir a Enviar Encuesta
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import API from '../api.js'

const router = useRouter()

const form = ref({
  title: '',
  description: '',
  questions: []
})

const addQuestion = () => {
  form.value.questions.push({ text: '', type: '1' })
}

const removeQuestion = (index) => {
  form.value.questions.splice(index, 1)
}

const submitSurvey = async () => {
  try {
    const surveyRes = await API.post('/surveys', {
      title: form.value.title,
      description: form.value.description
    }); 
  
    console.log('Encuesta creada:', surveyRes.data)

    // Añadir preguntas usando el ID retornado
    await API.post(`/surveys/${surveyRes.data.id}/questions`, {
      questions: form.value.questions.map(q => ({
        text: q.text,
        type_id: parseInt(q.type)  // Asegurar tipo numérico
      }))
    })
    
    alert('Encuesta creada con éxito!')
    form.value = { title: '', description: '', questions: [] }
    
  } catch (error) {
    console.error('Error detallado:', error.response)
    alert(`Error: ${error.response?.data?.message || 'Revisa la consola'}`)
  }
}

const goToSendSurvey = () => {
  router.push('/send-survey')
}
</script>

<style scoped>
/* Estilos existentes se mantienen */
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

input, textarea, select {
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-family: inherit;
}

.button-group {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 2rem;
}

/* Nuevos estilos para preguntas */
.question-item {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.type-selector {
  flex-shrink: 0;
  width: 150px;
}

.btn-remove {
  background: #ff4444;
  padding: 0.5rem;
  width: 40px;
  transition: background 0.3s ease;
}

.btn-remove:hover {
  background: #cc0000;
}

.btn-add-question {
  background: #00C851;
}

.btn-add-question:hover {
  background: #007E33;
}

.btn-save {
  background: #0077cc;
}

.btn-send {
  background: #33b5e5;
}

.btn-send:hover {
  background: #0099CC;
}

button {
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  padding: 0.75rem;
  transition: background-color 0.3s ease;
}

.enviar-encuesta {
  margin-top: 2rem;
  text-align: center;
}
</style>