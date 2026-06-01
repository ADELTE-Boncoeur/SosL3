<template>
  <section class="bg-gradient-to-br from-slate-950 via-emerald-900 to-slate-950 text-white">
    <div class="mx-auto max-w-7xl px-6 py-16">
      <div class="grid gap-10 lg:grid-cols-[0.9fr_0.55fr]">
        <div class="space-y-6">
          <p class="text-sm uppercase tracking-[0.35em] text-emerald-300">Western Province Ultra</p>
          <h1 class="text-5xl font-black">Lake Kivu, rainforest and premium adventure</h1>
          <p class="max-w-3xl text-slate-200">The west offers Lake Kivu luxury retreats, Nyungwe canopy walks, and volcano-edge adventure with modern eco-lodges.</p>
          <div class="grid gap-4 sm:grid-cols-3">
            <div class="rounded-3xl bg-white/10 p-6">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Lake escapes</p>
              <p class="mt-3 text-3xl font-black text-white">Exclusive</p>
            </div>
            <div class="rounded-3xl bg-white/10 p-6">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Rainforest</p>
              <p class="mt-3 text-3xl font-black text-white">Lush</p>
            </div>
            <div class="rounded-3xl bg-white/10 p-6">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Adventure</p>
              <p class="mt-3 text-3xl font-black text-white">Full</p>
            </div>
          </div>
        </div>

        <aside class="rounded-[32px] border border-white/10 bg-white/10 p-8 backdrop-blur-xl shadow-2xl">
          <h2 class="text-xl font-black text-white">Lake & rainforest guide</h2>
          <p class="mt-3 text-slate-200">Plan your Nyungwe canopy walk, Lake Kivu cruise and volcano-front relaxation with expert travel advice.</p>
          <div class="mt-6 space-y-4">
            <div class="rounded-3xl bg-slate-950/60 p-4">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-400">Top activity</p>
              <p class="mt-2 text-2xl font-black">Canopy walk</p>
            </div>
            <div class="rounded-3xl bg-slate-950/60 p-4">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-400">Best stay</p>
              <p class="mt-2 font-semibold">Lakefront retreat</p>
            </div>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <section class="bg-white py-20 text-slate-900">
    <div class="mx-auto max-w-7xl px-6">
      <div class="text-center mb-12">
        <p class="text-sm uppercase tracking-[0.35em] text-emerald-500">Western Province gallery</p>
        <h2 class="mt-4 text-4xl font-black">Lake Kivu and Nyungwe rainforest imagery</h2>
      </div>
      <div class="grid gap-6 md:grid-cols-3">
        <div class="rounded-[32px] overflow-hidden shadow-2xl border border-slate-200 bg-slate-50">
          <img src="@/assets/images/west.jpg" alt="Western Province lake view" class="h-72 w-full object-cover" />
        </div>
        <div class="rounded-[32px] overflow-hidden shadow-2xl border border-slate-200 bg-slate-50">
          <img src="@/assets/images/rwandans.jpg" alt="Forest walk" class="h-72 w-full object-cover" />
        </div>
        <div class="rounded-[32px] overflow-hidden shadow-2xl border border-slate-200 bg-slate-50">
          <img src="@/assets/images/vision.jpg" alt="Lake Kivu retreat" class="h-72 w-full object-cover" />
        </div>
      </div>
    </div>
  </section>

  <section class="bg-slate-100 py-16 text-slate-900">
    <div class="mx-auto max-w-7xl px-6">
      <div class="grid gap-8 lg:grid-cols-[0.9fr_0.55fr]">
        <div class="space-y-8">
          <article class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h2 class="text-3xl font-black text-slate-900">Lake Kivu cruise planner</h2>
            <p class="mt-4 text-slate-600">Book lake cruises, sunset experiences and waterfront dining with interactive itinerary suggestions.</p>
            <div class="mt-8 grid gap-4 sm:grid-cols-2">
              <div class="rounded-3xl bg-slate-50 p-5">
                <h3 class="font-semibold text-slate-900">Beach explorer</h3>
                <p class="mt-2 text-sm text-slate-600">Luxury lakeside beaches and chill retreats.</p>
              </div>
              <div class="rounded-3xl bg-slate-50 p-5">
                <h3 class="font-semibold text-slate-900">Canopy walk</h3>
                <p class="mt-2 text-sm text-slate-600">Guided Nyungwe forest treks and aerial trails.</p>
              </div>
            </div>
          </article>

          <article class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h2 class="text-3xl font-black text-slate-900">Western attractions</h2>
            <div class="mt-6 grid gap-4 sm:grid-cols-2">
              <div class="rounded-3xl bg-slate-50 p-5">
                <p class="font-semibold text-slate-900">Volcanoes National Park</p>
                <p class="mt-2 text-sm text-slate-600">Gorilla trekking and volcano trails.</p>
              </div>
              <div class="rounded-3xl bg-slate-50 p-5">
                <p class="font-semibold text-slate-900">Nyungwe rainforest</p>
                <p class="mt-2 text-sm text-slate-600">Rainforest adventures and canopy views.</p>
              </div>
            </div>
          </article>
        </div>

        <aside class="space-y-8">
          <div class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h3 class="text-2xl font-black text-slate-900">Recommended stays</h3>
            <div class="mt-5 space-y-4">
              <article v-for="hotel in westernHotels" :key="hotel.id" class="rounded-3xl bg-slate-50 p-4">
                <p class="font-semibold text-slate-900">{{ hotel.name }}</p>
                <p class="text-sm text-slate-600">{{ hotel.rating }} ★ • ${{ hotel.price }} / night</p>
              </article>
            </div>
          </div>

          <div class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h3 class="text-2xl font-black text-slate-900">Travel tips</h3>
            <div class="mt-5 space-y-4">
              <div class="rounded-3xl bg-slate-50 p-4">
                <p class="font-semibold text-slate-900">Best time</p>
                <p class="text-sm text-slate-600">Morning lake cruises and afternoon canopy walks.</p>
              </div>
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
const westernHotels = computed(() => store.hotels.filter((hotel) => hotel.destination === 'Western Province'))
</script>
