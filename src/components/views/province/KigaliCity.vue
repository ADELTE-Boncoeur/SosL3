<template>
  <section class="bg-gradient-to-br from-slate-950 via-emerald-900 to-slate-950 text-white">
    <div class="mx-auto max-w-7xl px-6 py-16">
      <div class="grid gap-10 lg:grid-cols-[0.9fr_0.55fr]">
        <div class="space-y-6">
          <p class="text-sm uppercase tracking-[0.35em] text-emerald-300">Kigali Ultra</p>
          <h1 class="text-5xl font-black">Kigali City: Rwanda’s smart capital</h1>
          <p class="max-w-3xl text-slate-200">Modern urban energy, tech hubs, premium dining, conferences and cultural landmarks connected by an intelligent tourism experience.</p>
          <div class="grid gap-4 sm:grid-cols-3">
            <div class="rounded-3xl bg-white/10 p-6">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Visitor score</p>
              <p class="mt-3 text-3xl font-black text-white">98</p>
            </div>
            <div class="rounded-3xl bg-white/10 p-6">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Nightlife</p>
              <p class="mt-3 text-3xl font-black text-white">Luxury</p>
            </div>
            <div class="rounded-3xl bg-white/10 p-6">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Business tourism</p>
              <p class="mt-3 text-3xl font-black text-white">Premium</p>
            </div>
          </div>
        </div>

        <aside class="rounded-[32px] border border-white/10 bg-white/10 p-8 backdrop-blur-xl shadow-2xl">
          <h2 class="text-xl font-black text-white">Kigali smart insights</h2>
          <p class="mt-3 text-slate-200">Weather, top hotels, events and recommended itineraries for Kigali.</p>
          <div class="mt-6 space-y-4">
            <div class="rounded-3xl bg-slate-950/60 p-4">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-400">Local weather</p>
              <p class="mt-2 text-2xl font-black">24°C</p>
              <p class="text-sm text-slate-300">Sunny, perfect for city tours.</p>
            </div>
            <div class="rounded-3xl bg-slate-950/60 p-4">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-400">Top event</p>
              <p class="mt-2 font-semibold">East Africa Tourism Summit</p>
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
            <h2 class="text-3xl font-black text-slate-900">Kigali skyline & smart city</h2>
            <p class="mt-4 text-slate-600">Experience modern Kigali with luxury hotels, conference centers, startup hubs and rooftop dining. The city blends innovation with Rwandan hospitality.</p>
            <div class="mt-8 grid gap-4 sm:grid-cols-2">
              <div class="rounded-3xl bg-slate-50 p-5">
                <h3 class="font-semibold text-slate-900">Nightlife guide</h3>
                <p class="mt-2 text-sm text-slate-600">Rooftop bars, live music and premium dining experiences.</p>
              </div>
              <div class="rounded-3xl bg-slate-50 p-5">
                <h3 class="font-semibold text-slate-900">Business tourism</h3>
                <p class="mt-2 text-sm text-slate-600">Conference venues, meetings and innovation tourism services.</p>
              </div>
            </div>
          </article>

          <article class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h2 class="text-3xl font-black text-slate-900">Top Kigali attractions</h2>
            <div class="mt-6 grid gap-4 sm:grid-cols-2">
              <div class="rounded-3xl bg-slate-50 p-5">
                <p class="font-semibold text-slate-900">Kigali Genocide Memorial</p>
                <p class="mt-2 text-sm text-slate-600">A thoughtful cultural site with modern interpretation spaces.</p>
              </div>
              <div class="rounded-3xl bg-slate-50 p-5">
                <p class="font-semibold text-slate-900">Kimironko Market</p>
                <p class="mt-2 text-sm text-slate-600">Local markets, crafts and lively city culture experiences.</p>
              </div>
            </div>
          </article>

          <article class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h2 class="text-3xl font-black text-slate-900">Suggested itinerary</h2>
            <div class="mt-6 space-y-4">
              <div class="rounded-3xl bg-slate-50 p-5">
                <p class="font-semibold text-slate-900">Day 1: Kigali city discovery</p>
                <p class="text-sm text-slate-600">Museums, city market and rooftop dinner.</p>
              </div>
              <div class="rounded-3xl bg-slate-50 p-5">
                <p class="font-semibold text-slate-900">Day 2: Innovation & culture</p>
                <p class="text-sm text-slate-600">Business hub tour, local coffee tasting and heritage sites.</p>
              </div>
            </div>
          </article>
        </div>

        <aside class="space-y-8">
          <div class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h3 class="text-2xl font-black text-slate-900">Hotels</h3>
            <div class="mt-5 space-y-4">
              <article v-for="hotel in cityHotels" :key="hotel.id" class="rounded-3xl bg-slate-50 p-4">
                <p class="font-semibold text-slate-900">{{ hotel.name }}</p>
                <p class="text-sm text-slate-600">{{ hotel.stars }}★ • {{ hotel.rating }} ★ • ${{ hotel.price }} / night</p>
              </article>
            </div>
          </div>

          <div class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-xl">
            <h3 class="text-2xl font-black text-slate-900">Restaurants</h3>
            <div class="mt-5 space-y-4">
              <article v-for="restaurant in cityRestaurants" :key="restaurant.id" class="rounded-3xl bg-slate-50 p-4">
                <p class="font-semibold text-slate-900">{{ restaurant.name }}</p>
                <p class="text-sm text-slate-600">{{ restaurant.cuisine }} • {{ restaurant.rating }} ★</p>
              </article>
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

const cityHotels = computed(() => store.hotels.filter((hotel) => hotel.destination === 'Kigali City'))
const cityRestaurants = computed(() => store.restaurants.filter((restaurant) => restaurant.cuisine && restaurant.name.includes('Kigali') || restaurant.rating > 4.7))
</script>
