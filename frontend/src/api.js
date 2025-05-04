import axios from 'axios'

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:5000/api',  // cambia esto según tu back
  headers: {
    'Content-Type': 'application/json'
  }
})

export default API
