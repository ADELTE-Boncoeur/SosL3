<template>
  <section class="relative overflow-hidden text-white">
    <img :src="heroImage" alt="Rwanda aerial view" class="absolute inset-0 h-full w-full object-cover opacity-70" />
    <div class="absolute inset-0 bg-gradient-to-br from-slate-950/90 via-slate-900/40 to-emerald-950/80"></div>

    <div class="relative z-10 mx-auto max-w-7xl px-6 py-24 lg:px-10">
      <div class="grid gap-12 lg:grid-cols-[1.1fr_0.9fr] lg:items-center">
        <div>
          <p class="text-sm uppercase tracking-[0.35em] text-emerald-300">About Rwanda Luxury Travel</p>
          <h1 class="mt-6 text-5xl font-black tracking-tight sm:text-6xl">Crafting the premium Rwanda travel story with vision and authenticity.</h1>
          <p class="mt-6 max-w-3xl text-lg text-slate-200/90 sm:text-xl">Tembera Urwanda blends smart tourism, destination storytelling and cultural respect to create a modern platform for luxury guests, investors and travel partners.</p>

          <div class="mt-10 flex flex-wrap gap-4">
            <router-link to="/destinations" class="inline-flex items-center justify-center rounded-full bg-emerald-400 px-8 py-3 text-sm font-black text-slate-950 transition hover:scale-105">
              Explore destinations
            </router-link>
            <a href="#values" class="inline-flex items-center justify-center rounded-full border border-white/20 bg-white/10 px-8 py-3 text-sm font-black text-white transition hover:bg-white/20">
              Read our values
            </a>
          </div>
        </div>

        <div class="grid gap-4 sm:grid-cols-2">
          <div class="rounded-[32px] border border-white/10 bg-white/10 p-6 backdrop-blur-xl shadow-2xl">
            <p class="text-xs uppercase tracking-[0.35em] text-slate-300">Experience</p>
            <h2 class="mt-4 text-4xl font-black">15+</h2>
            <p class="mt-3 text-slate-200">Luxury travel concepts and destination designs curated for Rwanda.</p>
          </div>
          <div class="rounded-[32px] border border-white/10 bg-white/10 p-6 backdrop-blur-xl shadow-2xl">
            <p class="text-xs uppercase tracking-[0.35em] text-slate-300">Focus</p>
            <h2 class="mt-4 text-4xl font-black">Sustainable</h2>
            <p class="mt-3 text-slate-200">Responsible tourism, culture-led hospitality and exceptional guest journeys.</p>
          </div>
          <div class="rounded-[32px] border border-white/10 bg-white/10 p-6 backdrop-blur-xl shadow-2xl">
            <p class="text-xs uppercase tracking-[0.35em] text-slate-300">Design</p>
            <h2 class="mt-4 text-4xl font-black">Bespoke</h2>
            <p class="mt-3 text-slate-200">Curated brand experiences with photography, motion, and rich content at every touchpoint.</p>
          </div>
          <div class="rounded-[32px] border border-white/10 bg-white/10 p-6 backdrop-blur-xl shadow-2xl">
            <p class="text-xs uppercase tracking-[0.35em] text-slate-300">Culture</p>
            <h2 class="mt-4 text-4xl font-black">Authentic</h2>
            <p class="mt-3 text-slate-200">Local stories, heritage rituals and people-first narratives throughout the platform.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-slate-950 py-20 px-6 text-white" id="values">
    <div class="mx-auto max-w-6xl">
      <div class="text-center">
        <p class="text-sm uppercase tracking-[0.35em] text-emerald-400">Our purpose</p>
        <h2 class="mt-4 text-4xl font-black">Why Tembera Urwanda exists</h2>
        <p class="mt-4 max-w-2xl mx-auto text-slate-300">We create a compelling luxury tourism experience for Rwanda with clear storytelling, immersive photography, and seamless access to each region’s finest attractions.</p>
      </div>

      <div class="mt-16 grid gap-6 md:grid-cols-3">
        <article class="rounded-[32px] border border-white/10 bg-white/5 p-8 shadow-2xl">
          <h3 class="text-xl font-bold text-emerald-300">Showcase Rwanda</h3>
          <p class="mt-4 text-slate-200">Highlight premium destinations, cultural experiences, and modern hospitality with a polished visual language.</p>
        </article>
        <article class="rounded-[32px] border border-white/10 bg-white/5 p-8 shadow-2xl">
          <h3 class="text-xl font-bold text-yellow-300">Inspire travel</h3>
          <p class="mt-4 text-slate-200">Turn curiosity into high-value trips through beautiful storytelling, destination insights, and local imagery.</p>
        </article>
        <article class="rounded-[32px] border border-white/10 bg-white/5 p-8 shadow-2xl">
          <h3 class="text-xl font-bold text-sky-300">Build trust</h3>
          <p class="mt-4 text-slate-200">Provide a professional platform for partners, guests and decision makers to explore Rwanda’s tourism potential.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="py-20 px-6 text-slate-900">
    <div class="mx-auto max-w-6xl grid gap-12 lg:grid-cols-[0.65fr_0.35fr]">
      <div class="space-y-10 rounded-[32px] border border-slate-200 bg-white p-10 shadow-2xl">
        <div class="space-y-4">
          <p class="text-sm uppercase tracking-[0.35em] text-emerald-500">Our story</p>
          <h2 class="text-4xl font-black">A modern tourism platform with deep local roots</h2>
        </div>
        <p class="text-slate-600 leading-8">Tembera Urwanda brings together Rwanda’s strength in innovation, sustainability and hospitality. The platform is designed to reflect the country’s dynamic cities, rainforest escapes, volcano treks and lakeside luxury while giving travelers an intuitive path to explore and book.</p>
        <p class="text-slate-600 leading-8">Every section is built to tell a richer story—whether through curated photo galleries, destination summaries, or intelligent trip guidance. The goal is to make Rwanda feel both aspirational and accessible without losing the authenticity of local culture.</p>
      </div>

      <div class="grid gap-6">
        <div class="rounded-[32px] overflow-hidden shadow-2xl">
          <img :src="storyImageA" alt="Rwanda heritage" class="h-80 w-full object-cover" />
        </div>
        <div class="rounded-[32px] overflow-hidden shadow-2xl">
          <img :src="storyImageB" alt="Rwanda landscapes" class="h-80 w-full object-cover" />
        </div>
      </div>
    </div>
  </section>

  <section class="bg-slate-950 py-20 px-6 text-white">
    <div class="mx-auto max-w-6xl">
      <div class="grid gap-6 lg:grid-cols-3">
        <div class="rounded-[32px] bg-white/5 p-8 shadow-2xl">
          <p class="text-sm uppercase tracking-[0.35em] text-emerald-300">What we deliver</p>
          <h3 class="mt-4 text-3xl font-black">Complete tourism storytelling</h3>
          <p class="mt-4 text-slate-300">Visual direction, destination copy, immersive imagery, and premium interaction design for every traveler.</p>
        </div>
        <div class="rounded-[32px] bg-white/5 p-8 shadow-2xl">
          <h3 class="text-2xl font-bold text-white">Destination photography</h3>
          <p class="mt-4 text-slate-300">A curated suite of visuals for Kigali, national parks, tea hills, waterfalls, and cultural moments.</p>
        </div>
        <div class="rounded-[32px] bg-white/5 p-8 shadow-2xl">
          <h3 class="text-2xl font-bold text-white">Premium user journeys</h3>
          <p class="mt-4 text-slate-300">From browsing destinations to planning itineraries and viewing partner opportunities, every experience feels deliberate.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="py-20 px-6 text-slate-900">
    <div class="mx-auto max-w-6xl text-center">
      <p class="text-sm uppercase tracking-[0.35em] text-emerald-500">Photo showcase</p>
      <h2 class="mt-4 text-4xl font-black">Visual moments from Rwanda</h2>
      <p class="mt-4 max-w-3xl mx-auto text-slate-600">A gallery of inviting landscapes, city life and cultural connection helps guests imagine the next premium trip.</p>
    </div>

    <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
      <div class="overflow-hidden rounded-[28px] shadow-2xl">
        <img :src="galleryA" alt="Rwanda city scene" class="h-72 w-full object-cover" />
      </div>
      <div class="overflow-hidden rounded-[28px] shadow-2xl">
        <img :src="galleryB" alt="Rwanda nature" class="h-72 w-full object-cover" />
      </div>
      <div class="overflow-hidden rounded-[28px] shadow-2xl">
        <img :src="galleryC" alt="Rwanda culture" class="h-72 w-full object-cover" />
      </div>
      <div class="overflow-hidden rounded-[28px] shadow-2xl">
        <img :src="galleryD" alt="Rwanda tourism" class="h-72 w-full object-cover" />
      </div>
    </div>
  </section>
</template>

<script setup>
const heroImage = new URL('../../assets/images/background1.jpg', import.meta.url).href
const storyImageA = new URL('../../assets/images/president.jpg', import.meta.url).href
const storyImageB = new URL('../../assets/images/tea plantation.jpg', import.meta.url).href
const galleryA = new URL('../../assets/images/kigali.jpg', import.meta.url).href
const galleryB = new URL('../../assets/images/eastern.jpg', import.meta.url).href
const galleryC = new URL('../../assets/images/rwandans.jpg', import.meta.url).href
const galleryD = new URL('../../assets/images/west.jpg', import.meta.url).href
</script>
