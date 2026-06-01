<template>
  <!-- HERO SECTION: ARCHIVE FOCUS -->
  <section class="relative overflow-hidden bg-slate-950">
    <div class="absolute inset-0 bg-gradient-to-br from-slate-950 via-emerald-900/40 to-slate-950"></div>
    
    <div class="relative mx-auto max-w-7xl px-6 py-24">
      <div class="grid gap-12 lg:grid-cols-[0.9fr_0.55fr]">
        <div class="space-y-8">
          <p class="text-xs uppercase tracking-[0.4em] text-emerald-400">Eastern Province // Operational Archive</p>
          <h1 class="text-6xl font-black leading-tight text-white">Wildlife, safari and conservation journeys</h1>
          <p class="max-w-2xl text-lg text-slate-300">The Eastern Province architecture blends premium safari experiences with wildlife conservation systems, engineered for immersive adventure travel.</p>
          
          <div class="grid gap-4 sm:grid-cols-3">
            <div class="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-md">
              <p class="text-xs uppercase tracking-[0.2em] text-slate-400">Wildlife</p>
              <p class="mt-2 text-2xl font-black">High</p>
            </div>
            <div class="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-md">
              <p class="text-xs uppercase tracking-[0.2em] text-slate-400">Safari guides</p>
              <p class="mt-2 text-2xl font-black">Expert</p>
            </div>
            <div class="rounded-3xl border border-white/10 bg-white/5 p-6 backdrop-blur-md">
              <p class="text-xs uppercase tracking-[0.2em] text-slate-400">Eco lodges</p>
              <p class="mt-2 text-2xl font-black">Premium</p>
            </div>
          </div>
        </div>

        <aside class="rounded-[32px] border border-white/10 bg-white/5 p-8 backdrop-blur-2xl shadow-2xl">
          <h2 class="text-xl font-bold text-white">Safari System Planner</h2>
          <p class="mt-2 text-sm text-slate-400">Integrated tracking for luxury logistics and conservation routes.</p>
          <div class="mt-8 space-y-4">
            <div class="rounded-2xl bg-black/40 p-5">
              <p class="text-xs uppercase tracking-[0.2em] text-slate-500">Best operational season</p>
              <p class="mt-1 font-bold">June – October</p>
            </div>
            <div class="rounded-2xl bg-black/40 p-5">
              <p class="text-xs uppercase tracking-[0.2em] text-slate-500">Active event</p>
              <p class="mt-1 font-bold">Conservation safari departures</p>
            </div>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <!-- DATA GRID SECTION -->
  <section class="bg-slate-50 py-20 text-slate-900">
    <div class="mx-auto max-w-7xl px-6">
      <div class="grid gap-8 lg:grid-cols-[0.9fr_0.55fr]">
        <div class="space-y-8">
          <article class="rounded-[32px] bg-white p-8 shadow-sm border border-slate-100">
            <h2 class="text-3xl font-black">Wildlife Explorer</h2>
            <p class="mt-3 text-slate-600">Access Akagera National Park streams, real-time night safari data, and bird species tracking.</p>
            <div class="mt-8 grid gap-4 sm:grid-cols-2">
              <div class="rounded-2xl bg-slate-100 p-6">
                <h3 class="font-bold text-slate-900">Safari logistics</h3>
                <p class="mt-2 text-sm text-slate-600">Optimized routes and secure lodge connections.</p>
              </div>
              <div class="rounded-2xl bg-slate-100 p-6">
                <h3 class="font-bold text-slate-900">Avian dashboard</h3>
                <p class="mt-2 text-sm text-slate-600">Species density mapping and hotspot tracking.</p>
              </div>
            </div>
          </article>

          <article class="rounded-[32px] bg-white p-8 shadow-sm border border-slate-100">
            <h2 class="text-3xl font-black">Core Experiences</h2>
            <div class="mt-6 grid gap-4 sm:grid-cols-2">
              <div class="rounded-2xl bg-slate-100 p-5">
                <p class="font-bold">Akagera circuit</p>
                <p class="mt-1 text-sm text-slate-600">Game drives and riparian exploration.</p>
              </div>
              <div class="rounded-2xl bg-slate-100 p-5">
                <p class="font-bold">Conservation ops</p>
                <p class="mt-1 text-sm text-slate-600">Ranger-led environmental field studies.</p>
              </div>
            </div>
          </article>
        </div>

        <aside class="space-y-8">
          <div class="rounded-[32px] bg-white p-8 shadow-sm border border-slate-100">
            <h3 class="text-2xl font-black">Registered Lodges</h3>
            <div class="mt-6 space-y-3">
              <article v-for="hotel in safariHotels" :key="hotel.id" class="rounded-2xl bg-slate-50 p-4 border border-slate-100">
                <p class="font-bold text-slate-900">{{ hotel.name }}</p>
                <p class="text-xs text-slate-500 uppercase tracking-wider">{{ hotel.rating }} stars • ${{ hotel.price }} per night</p>
              </article>
            </div>
          </div>

          <div class="rounded-[32px] bg-white p-8 shadow-sm border border-slate-100">
            <h3 class="text-2xl font-black">Local Events</h3>
            <div class="mt-6 rounded-2xl bg-slate-50 p-5">
              <p class="font-bold">Rwanda Culture Festival</p>
              <p class="mt-1 text-sm text-slate-600">Community-based tourism and traditional arts integration.</p>
            </div>
          </div>
        </aside>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useTourismStore } from '@/store'

const store = useTourismStore()
const safariHotels = computed(() => 
  store.hotels.filter((hotel) => hotel.destination === 'Eastern Province')
)
</script>