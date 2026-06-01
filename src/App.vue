<script setup>
import { onMounted, ref } from 'vue'
import { RouterView, useRouter } from 'vue-router'
import Navbar from './components/Navbar.vue'
import Footer from './components/views/footer.vue'

const router = useRouter()
const progress = ref(0)
let progressInterval = null

const startProgress = () => {
  progress.value = 16
  clearInterval(progressInterval)
  progressInterval = setInterval(() => {
    if (progress.value < 88) {
      progress.value += 8
    }
  }, 180)
}

const endProgress = () => {
  clearInterval(progressInterval)
  progress.value = 100
  setTimeout(() => {
    progress.value = 0
  }, 320)
}

onMounted(() => {
  router.beforeEach((to, from, next) => {
    startProgress()
    next()
  })
  router.afterEach(() => {
    endProgress()
  })
})
</script>

<template>
  <div class="fixed inset-x-0 top-0 z-[60] h-1 overflow-hidden bg-transparent">
    <div class="h-full bg-gradient-to-r from-emerald-400 via-cyan-400 to-amber-300 transition-all duration-200 ease-out" :style="{ width: progress + '%' }"></div>
  </div>

  <Navbar />

  <main class="min-h-screen">
    <Transition name="route-fade" mode="out-in">
      <RouterView v-slot="{ Component }">
        <component :is="Component" />
      </RouterView>
    </Transition>
  </main>

  <Footer />

  <div class="fixed bottom-6 right-6 z-50 flex flex-col gap-3">
    <a href="https://wa.me/250722635461" target="_blank" rel="noreferrer" class="flex h-14 w-14 items-center justify-center rounded-full bg-emerald-500 text-white shadow-2xl shadow-emerald-500/30 transition hover:-translate-y-1" aria-label="WhatsApp chat">
      <span>WA</span>
    </a>
    <a href="tel:+250722635461" class="flex h-14 w-14 items-center justify-center rounded-full bg-sky-500 text-white shadow-2xl shadow-sky-500/30 transition hover:-translate-y-1" aria-label="Call support">
      <span>Call</span>
    </a>
    <button class="flex h-14 w-14 items-center justify-center rounded-full bg-violet-500 text-white shadow-2xl shadow-violet-500/30 transition hover:-translate-y-1" aria-label="Open chatbot">
      <span>AI</span>
    </button>
  </div>
</template>

<style>
.route-fade-enter-active,
.route-fade-leave-active {
  transition: opacity 0.35s ease, transform 0.35s ease;
}
.route-fade-enter-from,
.route-fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>