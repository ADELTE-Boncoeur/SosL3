<template>
  <nav class="sticky top-0 z-50 border-b border-emerald-800/20 bg-gradient-to-r from-emerald-950/95 via-emerald-900/95 to-emerald-950/95 shadow-2xl shadow-emerald-950/30 backdrop-blur-md transition-all duration-300">
    <div class="mx-auto flex w-full max-w-7xl flex-col items-center justify-between gap-4 px-4 py-3 md:flex-row md:px-6">
      <!-- Logo and branding -->
      <a href="#" class="group flex items-center gap-3 rounded-full bg-gradient-to-r from-white/15 to-white/5 px-3 py-2 backdrop-blur-sm border border-white/10 hover:border-white/20 transition-all duration-300 md:mr-6">
        <img src="../assets/images/logos.png" alt="Tembera logo" class="h-12 w-12 rounded-full object-cover ring-2 ring-white/30 group-hover:ring-white/50 transition-all" />
        <div>
          <h1 class="text-base font-black uppercase tracking-[0.25em] text-white md:text-lg group-hover:text-emerald-200 transition-colors">Rwanda Travel</h1>
          <p class="text-[11px] text-emerald-100/80">Discover simple, beautiful journeys</p>
        </div>
      </a>

      <!-- Navigation menu -->
      <div class="flex flex-wrap items-center justify-between gap-4 text-sm font-bold uppercase tracking-widest text-white md:gap-8 lg:gap-12">
        <ul class="flex flex-wrap items-center gap-3 md:gap-6">
          <li>
            <RouterLink 
              to="/" 
              class="nav-link relative px-3 py-2 rounded-lg transition-all duration-300 hover:text-yellow-300 hover:bg-emerald-700/50 group"
            >
              Home
              <span class="absolute bottom-0 left-0 w-0 h-1 bg-gradient-to-r from-emerald-300 to-cyan-300 rounded-full group-hover:w-full transition-all duration-300"></span>
            </RouterLink>
          </li>
          <li>
            <RouterLink 
              to="/about" 
              class="nav-link relative px-3 py-2 rounded-lg transition-all duration-300 hover:text-yellow-300 hover:bg-emerald-700/50 group"
            >
              About
              <span class="absolute bottom-0 left-0 w-0 h-1 bg-gradient-to-r from-emerald-300 to-cyan-300 rounded-full group-hover:w-full transition-all duration-300"></span>
            </RouterLink>
          </li>
          <li>
            <RouterLink 
              to="/gallery" 
              class="nav-link relative px-3 py-2 rounded-lg transition-all duration-300 hover:text-yellow-300 hover:bg-emerald-700/50 group"
            >
              Gallery
              <span class="absolute bottom-0 left-0 w-0 h-1 bg-gradient-to-r from-emerald-300 to-cyan-300 rounded-full group-hover:w-full transition-all duration-300"></span>
            </RouterLink>
          </li>
          
          <!-- Destinations dropdown with premium styling -->
          <li class="relative group">
            <button class="nav-link relative px-3 py-2 rounded-lg transition-all duration-300 hover:text-yellow-300 hover:bg-emerald-700/50 flex items-center gap-1">
              Destinations 
              <span class="group-hover:rotate-180 transition-transform duration-300">▾</span>
              <span class="absolute bottom-0 left-0 w-0 h-1 bg-gradient-to-r from-emerald-300 to-cyan-300 rounded-full group-hover:w-full transition-all duration-300"></span>
            </button>
            
            <!-- Premium dropdown menu with glassmorphism -->
            <ul class="invisible opacity-0 group-hover:visible group-hover:opacity-100 absolute bg-gradient-to-b from-emerald-900/95 to-emerald-950/95 backdrop-blur-md text-white rounded-2xl shadow-2xl w-56 top-full left-0 z-50 transition-all duration-300 border border-white/10 py-2">
              <li class="px-1 py-2 hover:bg-emerald-800/50 transition-colors mx-2 rounded-lg">
                <RouterLink to="/destinations/kigali-city" class="block px-3 py-2 text-xs font-bold uppercase tracking-wider hover:text-cyan-300">
                  <span class="font-black text-emerald-300">🏙️</span> Kigali City
                </RouterLink>
              </li>
              <li class="px-1 py-2 hover:bg-emerald-800/50 transition-colors mx-2 rounded-lg">
                <RouterLink to="/destinations/southern-province" class="block px-3 py-2 text-xs font-bold uppercase tracking-wider hover:text-cyan-300">
                  <span class="font-black text-yellow-300">🌾</span> Southern
                </RouterLink>
              </li>
              <li class="px-1 py-2 hover:bg-emerald-800/50 transition-colors mx-2 rounded-lg">
                <RouterLink to="/destinations/western-province" class="block px-3 py-2 text-xs font-bold uppercase tracking-wider hover:text-cyan-300">
                  <span class="font-black text-blue-300">🏞️</span> Western
                </RouterLink>
              </li>
              <li class="px-1 py-2 hover:bg-emerald-800/50 transition-colors mx-2 rounded-lg">
                <RouterLink to="/destinations/northern-province" class="block px-3 py-2 text-xs font-bold uppercase tracking-wider hover:text-cyan-300">
                  <span class="font-black text-red-300">⛰️</span> Northern
                </RouterLink>
              </li>
              <li class="px-1 py-2 hover:bg-emerald-800/50 transition-colors mx-2 rounded-lg">
                <RouterLink to="/destinations/eastern-province" class="block px-3 py-2 text-xs font-bold uppercase tracking-wider hover:text-cyan-300">
                  <span class="font-black text-orange-300">🦁</span> Eastern
                </RouterLink>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useI18n } from '@/composables/useI18n'

const { locale, availableLocales, t, setLocale } = useI18n()
</script>

