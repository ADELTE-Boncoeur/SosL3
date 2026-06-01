import { createApp } from 'vue'
import { createPinia } from 'pinia'
import AOS from 'aos'
import 'aos/dist/aos.css'
import App from './App.vue'
import './style.css'
import router from './router/index.js'

const app = createApp(App)
const pinia = createPinia()

app.use(router)
app.use(pinia)

app.mount('#app')

AOS.init({
  once: true,
  duration: 900,
  easing: 'ease-out-cubic',
  offset: 80
})