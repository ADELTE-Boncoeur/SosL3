<template>
  <section class="bg-gradient-to-br from-slate-950 via-emerald-900 to-slate-950 text-white">
    <div class="mx-auto max-w-7xl px-6 py-16">
      <div class="grid gap-10 lg:grid-cols-[0.9fr_0.55fr]">
        <div class="space-y-6">
          <p class="text-sm uppercase tracking-[0.35em] text-emerald-300">Southern Province Ultra</p>
          <h1 class="text-5xl font-black">Culture, heritage and immersive village travel</h1>
          <p class="max-w-3xl text-slate-200">The south invites you into Rwandan history, coffee landscapes, cultural villages and curated museum experiences.</p>
          <div class="grid gap-4 sm:grid-cols-3">
            <div class="rounded-3xl bg-white/10 p-6">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Culture</p>
              <p class="mt-3 text-3xl font-black text-white">Rich</p>
            </div>
            <div class="rounded-3xl bg-white/10 p-6">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Heritage</p>
              <p class="mt-3 text-3xl font-black text-white">Authentic</p>
            </div>
            <div class="rounded-3xl bg-white/10 p-6">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Eco-tourism</p>
              <p class="mt-3 text-3xl font-black text-white">Elegant</p>
            </div>
          </div>
        </div>

        <aside class="rounded-[32px] border border-white/10 bg-white/10 p-8 backdrop-blur-xl shadow-2xl">
          <h2 class="text-xl font-black text-white">Heritage guide</h2>
          <p class="mt-3 text-slate-200">Discover cultural villages, museums and local craft experiences with personalized travel guidance.</p>
          <div class="mt-6 space-y-4">
            <div class="rounded-3xl bg-slate-950/60 p-4">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-400">Focus</p>
              <p class="mt-2 text-2xl font-black">Cultural heritage</p>
            </div>
            <div class="rounded-3xl bg-slate-950/60 p-4">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-400">Experience</p>
              <p class="mt-2 font-semibold">Traditional kingdom explorer</p>
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
            <h2 class="text-3xl font-black text-slate-900">Cultural heritage center</h2>
            <p class="mt-4 text-slate-600">Explore Butare museums, traditional kingdoms and village tours designed for immersive storytelling.</p>
            <div class="mt-8 grid gap-4 sm:grid-cols-2">
              <div class="rounded-3xl bg-slate-50 p-5">
                <h3 class="font-semibold text-slate-900">Museum dashboard</h3>
                <p class="mt-2 text-sm text-slate-600">Guides to museum exhibitions and cultural site tours.</p>
              </div>
              <div class="rounded-3xl bg-slate-50 p-5">
                <h3 class="font-semibold text-slate-900">Kingdom explorer</h3>
                <p class="mt-2 text-sm text-slate-600">Discover royal history and traditional ceremony experiences.</p>
              </div>
            </div>
          </article>

          <article class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h2 class="text-3xl font-black text-slate-900">Top southern attractions</h2>
            <div class="mt-6 grid gap-4 sm:grid-cols-2">
              <div class="rounded-3xl bg-slate-50 p-5">
                <p class="font-semibold text-slate-900">Butare craft markets</p>
                <p class="mt-2 text-sm text-slate-600">Curated local crafts and artisan experiences.</p>
              </div>
              <div class="rounded-3xl bg-slate-50 p-5">
                <p class="font-semibold text-slate-900">Coffee landscapes</p>
                <p class="mt-2 text-sm text-slate-600">Tea and coffee tours with scenic plantation views.</p>
              </div>
            </div>
          </article>
        </div>

        <aside class="space-y-8">
          <div class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h3 class="text-2xl font-black text-slate-900">Hotel recommendations</h3>
            <div class="mt-5 space-y-4">
              <article v-for="hotel in southernHotels" :key="hotel.id" class="rounded-3xl bg-slate-50 p-4">
                <p class="font-semibold text-slate-900">{{ hotel.name }}</p>
                <p class="text-sm text-slate-600">{{ hotel.stars }}★ • {{ hotel.rating }} ★</p>
              </article>
            </div>
          </div>

          <div class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h3 class="text-2xl font-black text-slate-900">Travel tips</h3>
            <div class="mt-5 space-y-4">
              <div class="rounded-3xl bg-slate-50 p-4">
                <p class="font-semibold text-slate-900">Local etiquette</p>
                <p class="text-sm text-slate-600">Respect village host customs and community tourism guidelines.</p>
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
const southernHotels = computed(() => store.hotels.filter((hotel) => hotel.destination === 'Southern Province'))
</script>
