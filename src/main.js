import { createApp } from 'vue'
import App from './App.vue'
import './style.css'
import router from './router/index.js'

const app = createApp(App)

/* ================= ADDITION (optional global setup point) ================= */
// You can add global plugins here later (pinia, i18n, etc.)

app.use(router)

app.mount('#app')