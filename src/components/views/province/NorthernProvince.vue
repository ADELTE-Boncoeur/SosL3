<template>
  <section class="bg-gradient-to-br from-slate-950 via-emerald-900 to-slate-950 text-white">
    <div class="mx-auto max-w-7xl px-6 py-16">
      <div class="grid gap-10 lg:grid-cols-[0.9fr_0.55fr]">
        <div class="space-y-6">
          <p class="text-sm uppercase tracking-[0.35em] text-emerald-300">Northern Province Ultra</p>
          <h1 class="text-5xl font-black">Gorilla trekking and volcano adventures</h1>
          <p class="max-w-3xl text-slate-200">The north is Rwanda’s most dramatic landscape with high-altitude trekking, gorilla permits, volcano views and elevated mountain luxury.</p>
          <div class="grid gap-4 sm:grid-cols-3">
            <div class="rounded-3xl bg-white/10 p-6">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Gorillas</p>
              <p class="mt-3 text-3xl font-black text-white">Premium</p>
            </div>
            <div class="rounded-3xl bg-white/10 p-6">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Hiking</p>
              <p class="mt-3 text-3xl font-black text-white">Epic</p>
            </div>
            <div class="rounded-3xl bg-white/10 p-6">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Culture</p>
              <p class="mt-3 text-3xl font-black text-white">Authentic</p>
            </div>
          </div>
        </div>

        <aside class="rounded-[32px] border border-white/10 bg-white/10 p-8 backdrop-blur-xl shadow-2xl">
          <h2 class="text-xl font-black text-white">Adventure dashboard</h2>
          <p class="mt-3 text-slate-200">Prepare for gorilla trekking, volcano hikes and premium mountain lodges with curated guidance.</p>
          <div class="mt-6 space-y-4">
            <div class="rounded-3xl bg-slate-950/60 p-4">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-400">Best route</p>
              <p class="mt-2 text-2xl font-black">Volcano circuit</p>
            </div>
            <div class="rounded-3xl bg-slate-950/60 p-4">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-400">Top experience</p>
              <p class="mt-2 font-semibold">Gorilla trekking in Musanze</p>
            </div>
          </div>
        </aside>
      </div>
    </div>
  </section>

  <section class="bg-slate-100 py-16 text-slate-900">
    <div class="mx-auto max-w-7xl px-6">
      <div class="grid gap-8 lg:grid-cols-[0.9fr_0.55fr]">
        <div class="space-y-8">
          <article class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h2 class="text-3xl font-black text-slate-900">Gorilla trekking planner</h2>
            <p class="mt-4 text-slate-600">Track gorilla groups, reserve premium permits, and connect with expert guides for a once-in-a-lifetime mountain adventure.</p>
            <div class="mt-8 grid gap-4 sm:grid-cols-2">
              <div class="rounded-3xl bg-slate-50 p-5">
                <h3 class="font-semibold text-slate-900">Volcano explorer</h3>
                <p class="mt-2 text-sm text-slate-600">Trek the Birunga chain and enjoy crater viewpoints.</p>
              </div>
              <div class="rounded-3xl bg-slate-50 p-5">
                <h3 class="font-semibold text-slate-900">Hiking planner</h3>
                <p class="mt-2 text-sm text-slate-600">Curated trails for forest, waterfall and cultural village routes.</p>
              </div>
            </div>
          </article>

          <article class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h2 class="text-3xl font-black text-slate-900">Top adventure experiences</h2>
            <div class="mt-6 grid gap-4 sm:grid-cols-2">
              <div class="rounded-3xl bg-slate-50 p-5">
                <p class="font-semibold text-slate-900">Gorilla tracking</p>
                <p class="mt-2 text-sm text-slate-600">Luxury safari lodges and guided trails.</p>
              </div>
              <div class="rounded-3xl bg-slate-50 p-5">
                <p class="font-semibold text-slate-900">Musanze caves</p>
                <p class="mt-2 text-sm text-slate-600">Cave exploration and mountain scenery.</p>
              </div>
            </div>
          </article>
        </div>

        <aside class="space-y-8">
          <div class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h3 class="text-2xl font-black text-slate-900">Adventure lodges</h3>
            <div class="mt-5 space-y-4">
              <article v-for="hotel in northernHotels" :key="hotel.id" class="rounded-3xl bg-slate-50 p-4">
                <p class="font-semibold text-slate-900">{{ hotel.name }}</p>
                <p class="text-sm text-slate-600">{{ hotel.stars }}★ • {{ hotel.rating }} ★</p>
              </article>
            </div>
          </div>

          <div class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h3 class="text-2xl font-black text-slate-900">Weather tips</h3>
            <div class="mt-5 space-y-4">
              <div class="rounded-3xl bg-slate-50 p-4">
                <p class="font-semibold text-slate-900">Cool mist days</p>
                <p class="text-sm text-slate-600">Best for trekking and clear mountain views.</p>
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
const northernHotels = computed(() => store.hotels.filter((hotel) => hotel.destination === 'Northern Province'))
</script>
