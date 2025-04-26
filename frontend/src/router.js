import { createRouter, createWebHistory } from 'vue-router'
import LoginView from './views/LoginView.vue'
import RegisterView from './views/RegisterView.vue'
import HomeView from './views/HomeView.vue'
import CreateSurveyView from './views/CreateSurveyView.vue'
import SendSurveyView from './views/SendSurveyView.vue'
import ResultsView from './views/ResultsView.vue'
import SearchClientsView from './views/SearchClientsView.vue'
import ClientsView from './views/ClientsView.vue'
import SurveyView from './views/SurveyView.vue'
import HistoryView from './views/HistoryView.vue'
import SupportView from './views/SupportView.vue'


const routes = [
  { path: '/', name: 'Login', component: LoginView },
  { path: '/register', name: 'Register', component: RegisterView },
  { path: '/home', name: 'Home', component: HomeView },
  { path: '/create-survey', name: 'CreateSurvey', component: CreateSurveyView },
  { path: '/send-survey', name: 'SendSurvey', component: SendSurveyView },
  { path: '/results', name: 'Results', component: ResultsView },
  { path: '/search-clients', name: 'SearchClients', component: SearchClientsView },
  { path: '/clients', name: 'Clients', component: ClientsView },
  { path: '/survey', name: 'Survey', component: SurveyView },
  { path: '/history', name: 'History', component: HistoryView },
  { path: '/support', name: 'Support', component: SupportView },

]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
