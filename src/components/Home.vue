<template>
  <section class="relative min-h-screen overflow-hidden text-white">

    <!-- ================= BACKGROUND SLIDER ================= -->
    <div class="absolute inset-0">
      <transition name="zoom-fade" mode="out-in">
        <div
          :key="current"
          class="absolute inset-0 scale-110 bg-cover bg-center"
          :style="{ backgroundImage: `url(${images[current]})` }"
        ></div>
      </transition>
    </div>

    <!-- ================= RWANDA GRADIENT ================= -->
    <div class="absolute inset-0 bg-[linear-gradient(135deg,rgba(4,120,87,0.35),rgba(15,23,42,0.25),rgba(245,158,11,0.18))]"></div>

    <!-- ================= HERO ================= -->
    <div class="relative z-10 mx-auto flex min-h-screen max-w-7xl flex-col justify-center px-6 py-16 lg:px-10">

      <!-- TOP BAR -->
      <div class="flex flex-wrap items-center justify-between gap-4 rounded-full border border-white/15 bg-white/10 px-4 py-3 text-sm backdrop-blur-xl shadow-xl">
        <span class="bg-gradient-to-r from-green-300 via-yellow-300 to-blue-300 bg-clip-text text-transparent font-black uppercase tracking-[0.3em]">
          Premium Rwanda Travel
        </span>
      </div>

      <!-- MAIN GRID -->
      <div class="mt-12 grid items-center gap-12 lg:grid-cols-[1.1fr_0.9fr]">

        <!-- LEFT CONTENT -->
        <article class="text-center lg:text-left">

          <p class="text-sm uppercase tracking-[0.35em] text-white/70">
            Discover Rwanda
          </p>

          <h1 class="text-5xl md:text-7xl font-black relative">
  <span class="bg-gradient-to-r from-green-400 via-yellow-300 to-blue-400 bg-clip-text text-transparent drop-shadow-lg">
    Tembera Rwanda
  </span>
</h1>

          <p class="mt-6 max-w-2xl text-lg text-white/85 md:text-xl">
            Explore Rwanda’s mountains, wildlife, cities, and culture in one modern travel experience.
          </p>

          <!-- BUTTONS -->
          <div class="mt-8 flex flex-wrap justify-center gap-4 lg:justify-start">
            <RouterLink
              to="/destinations"
              class="rounded-full bg-gradient-to-r from-green-500 via-yellow-400 to-blue-400 px-7 py-3 font-black text-emerald-950 shadow-xl transition hover:scale-105"
            >
              Start planning
            </RouterLink>

            <RouterLink
              to="/gallery"
              class="rounded-full border border-white/30 bg-white/10 px-7 py-3 font-black text-white hover:bg-white/20"
            >
              Explore gallery
            </RouterLink>
          </div>

          <!-- TAGS -->
          <div class="mt-6 flex flex-wrap justify-center gap-3 lg:justify-start">
            <span class="rounded-full bg-white/10 px-4 py-2 text-sm">Luxury stays</span>
            <span class="rounded-full bg-white/10 px-4 py-2 text-sm">Scenic routes</span>
            <span class="rounded-full bg-white/10 px-4 py-2 text-sm">Culture tours</span>
          </div>

          <!-- ================= TRANSLATOR (CLEAN UI) ================= -->
          <div class="mt-8 flex justify-center lg:justify-start">

            <div class="relative">
              <div class="absolute -inset-1 rounded-2xl bg-gradient-to-r from-green-500 via-yellow-400 to-blue-500 blur opacity-40"></div>

              <div class="relative rounded-2xl border border-white/20 bg-white/10 px-4 py-3 backdrop-blur-xl">
                <div class="text-center text-xs uppercase tracking-[0.3em] text-white/60 mb-2">
                  Language
                </div>
                <div id="google_translate_element"></div>
              </div>
            </div>

          </div>

        </article>

        <!-- RIGHT IMAGE CARD -->
        <aside class="rounded-[32px] border border-white/15 bg-white/10 p-4 backdrop-blur-xl shadow-2xl">

          <div class="overflow-hidden rounded-[28px]">
            <transition name="zoom-fade" mode="out-in">
              <img
                :key="current"
                :src="images[current]"
                class="h-72 w-full object-cover md:h-96 lg:h-[420px]"
              />
            </transition>
          </div>

          <!-- MINI CARDS -->
          <div class="mt-4 grid gap-3 md:grid-cols-2">
            <div class="rounded-2xl bg-emerald-900/60 p-4">
              <h2 class="font-bold text-emerald-200">Nature</h2>
              <p class="text-sm text-white/70">Mountains & parks</p>
            </div>

            <div class="rounded-2xl bg-white/10 p-4">
              <h2 class="font-bold">Culture</h2>
              <p class="text-sm text-white/70">City & traditions</p>
            </div>
          </div>

        </aside>

      </div>
    </div>

    <!-- SCROLL -->
    <div class="absolute bottom-6 left-1/2 -translate-x-1/2 animate-bounce">
      <div class="flex h-10 w-6 justify-center rounded-full border border-white/60">
        <div class="mt-2 h-2 w-1 bg-white rounded-full"></div>
      </div>
    </div>

  </section>

  <!-- ================= HIGHLIGHTS ================= -->
  <section class="bg-black py-20 px-6 text-white">

    <div class="mx-auto max-w-6xl text-center">
      <h2 class="text-4xl font-bold">Explore Rwanda Highlights</h2>
      <p class="mt-3 text-white/70">Luxury experiences across the country</p>
    </div>

    <div class="mx-auto mt-10 grid max-w-6xl gap-8 md:grid-cols-3">

      <div class="group overflow-hidden rounded-3xl bg-white/5 border border-white/10">
        <img src="@/assets/images/background.jpg" class="h-72 w-full object-cover group-hover:scale-110 transition" />
        <div class="p-5">
          <h3 class="text-green-300 font-bold">Nature</h3>
          <p class="text-white/70 text-sm">Wildlife & parks</p>
        </div>
      </div>

      <div class="group overflow-hidden rounded-3xl bg-white/5 border border-white/10">
        <img src="@/assets/images/background1.jpg" class="h-72 w-full object-cover group-hover:scale-110 transition" />
        <div class="p-5">
          <h3 class="text-yellow-300 font-bold">City Life</h3>
          <p class="text-white/70 text-sm">Kigali experience</p>
        </div>
      </div>

      <div class="group overflow-hidden rounded-3xl bg-white/5 border border-white/10">
        <img src="@/assets/images/background2.jpg" class="h-72 w-full object-cover group-hover:scale-110 transition" />
        <div class="p-5">
          <h3 class="text-blue-300 font-bold">Adventure</h3>
          <p class="text-white/70 text-sm">Hiking & safaris</p>
        </div>
      </div>

    </div>

  </section>
</template>

<script setup>
import { ref, onMounted } from "vue"

import img1 from "@/assets/images/background.jpg"
import img2 from "@/assets/images/background1.jpg"
import img3 from "@/assets/images/background2.jpg"

const images = [img1, img2, img3]
const current = ref(0)

onMounted(() => {
  setInterval(() => {
    current.value = (current.value + 1) % images.length
  }, 6000)

  const script = document.createElement("script")
  script.src = "https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"
  script.async = true
  document.body.appendChild(script)

  window.googleTranslateElementInit = () => {
    new window.google.translate.TranslateElement(
      {
        pageLanguage: "en",
        includedLanguages: "en,fr,rw",
        autoDisplay: false
      },
      "google_translate_element"
    )
  }
})
</script>

<style>
.zoom-fade-enter-active {
  animation: zoomIn 1.5s ease;
}
.zoom-fade-leave-active {
  animation: zoomOut 1.5s ease;
}

@keyframes zoomIn {
  from { opacity: 0; transform: scale(1.2); }
  to { opacity: 1; transform: scale(1.1); }
}

@keyframes zoomOut {
  from { opacity: 1; transform: scale(1.1); }
  to { opacity: 0; transform: scale(1.2); }
}
</style>