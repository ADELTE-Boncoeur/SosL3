<template>
  <section class="relative overflow-hidden">
    <img :src="heroImage" alt="Rwanda destinations background" class="absolute inset-0 h-full w-full object-cover opacity-50" />
    <div class="absolute inset-0 bg-gradient-to-br from-slate-950/85 via-emerald-950/30 to-slate-950/90"></div>

    <div class="relative mx-auto max-w-7xl px-4 py-20 text-white">
      <div class="grid gap-10 lg:grid-cols-[1.2fr_0.8fr] lg:items-center">
        <div>
          <p class="text-sm uppercase tracking-[0.35em] text-emerald-300">Destinations</p>
          <h1 class="mt-4 text-5xl font-black tracking-tight sm:text-6xl">Discover Rwanda with immersive destination visuals</h1>
          <p class="mt-6 max-w-3xl text-slate-200/80">From Kigali's modern city energy to safari plains, volcano forests and lakeside luxury, explore places with rich photography, stories and video inspiration.</p>
        </div>

        <div class="flex flex-wrap gap-3">
          <button @click="setProvince('All Provinces')" :class="filterClass('All Provinces')">All</button>
          <button @click="setProvince('Kigali')" :class="filterClass('Kigali')">Kigali</button>
          <button @click="setProvince('Northern Province')" :class="filterClass('Northern Province')">North</button>
          <button @click="setProvince('Southern Province')" :class="filterClass('Southern Province')">South</button>
          <button @click="setProvince('Eastern Province')" :class="filterClass('Eastern Province')">East</button>
          <button @click="setProvince('Western Province')" :class="filterClass('Western Province')">West</button>
        </div>
      </div>
    </div>
  </section>

  <section class="page-shell py-16 text-slate-900">
    <div class="mx-auto max-w-7xl px-4 md:px-8">
      <article class="rounded-[40px] border border-slate-200 bg-white/95 p-6 shadow-2xl md:p-10">
        <div class="grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
          <div>
            <h2 class="text-3xl font-black text-slate-900">Choose the province that matches your next travel mood</h2>
            <p class="mt-4 max-w-2xl text-slate-600">Each destination card includes a preview image, key highlights and local character so you can compare fast.</p>
          </div>
          <div class="grid gap-3 sm:grid-cols-2">
            <div class="rounded-3xl bg-slate-50 p-5 shadow-sm">
              <p class="text-xs uppercase tracking-[0.35em] text-slate-400">Best for</p>
              <p class="mt-3 text-lg font-bold text-slate-900">City life and culture</p>
            </div>
            <div class="rounded-3xl bg-slate-50 p-5 shadow-sm">
              <p class="text-xs uppercase tracking-[0.35em] text-slate-400">Travel style</p>
              <p class="mt-3 text-lg font-bold text-slate-900">Luxury nature escapes</p>
            </div>
          </div>
        </div>

        <div class="mt-10 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
          <article v-for="destination in filteredDestinations" :key="destination.id" class="group overflow-hidden rounded-[32px] border border-slate-200 bg-white shadow-xl transition hover:-translate-y-1 hover:shadow-2xl">
            <img :src="destination.image" :alt="destination.name" class="h-72 w-full object-cover transition duration-500 group-hover:scale-105" />
            <div class="p-6">
              <div class="flex flex-wrap items-center justify-between gap-4">
                <div>
                  <h3 class="text-2xl font-bold text-slate-900">{{ destination.name }}</h3>
                  <p class="mt-2 text-sm text-slate-500">{{ destination.province }}</p>
                </div>
                <span class="rounded-full bg-slate-100 px-3 py-1 text-xs uppercase tracking-[0.2em] text-slate-600">{{ destination.category }}</span>
              </div>
              <p class="mt-5 text-sm leading-7 text-slate-600">{{ destination.description }}</p>
              <div class="mt-5 flex flex-wrap gap-2">
                <span v-for="tag in destination.tags" :key="tag" class="rounded-full bg-slate-100 px-3 py-1 text-xs uppercase tracking-[0.2em] text-slate-600">{{ tag }}</span>
              </div>
            </div>
          </article>
        </div>

        <div class="mt-12 grid gap-6 lg:grid-cols-3">
          <article class="rounded-[32px] bg-slate-950 p-6 text-white shadow-2xl">
            <h3 class="text-2xl font-bold">Watch destination films</h3>
            <p class="mt-3 text-slate-300">Play curated video previews from nature, waterfalls and sunset drone footage.</p>
            <div class="mt-6 space-y-4">
              <video v-for="(source, index) in videoSources" :key="index" controls muted loop playsinline class="h-48 w-full rounded-3xl border border-slate-800 bg-slate-900 object-cover">
                <source :src="source" type="video/mp4" />
              </video>
            </div>
          </article>
          <article class="rounded-[32px] bg-white p-6 shadow-xl">
            <h3 class="text-2xl font-bold text-slate-900">Why Rwanda?</h3>
            <p class="mt-4 text-slate-600">A world-class destination with premium safari lodges, adventure hiking, luxury lakeside resorts and modern city culture in one compact country.</p>
          </article>
          <article class="rounded-[32px] bg-white p-6 shadow-xl">
            <h3 class="text-2xl font-bold text-slate-900">Plan faster</h3>
            <p class="mt-4 text-slate-600">Filter by province, compare highlights and use destination stories to choose the experience that feels most like you.</p>
          </article>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup>
import { computed, ref } from 'vue'

const heroImage = new URL('../../assets/images/background2.jpg', import.meta.url).href
const videoSources = [
  new URL('../../assets/images/rwanda.mp4', import.meta.url).href,
  new URL('../../assets/images/urugary.mp4', import.meta.url).href,
  new URL('../../assets/images/waterfall.mp4', import.meta.url).href
]

const activeProvince = ref('All Provinces')

const destinations = [
  {
    id: 'kigali',
    name: 'Kigali City',
    province: 'Kigali',
    category: 'City',
    description: 'Modern innovation hub with museums, rooftop dining and premium city experiences.',
    image: new URL('../../assets/images/kigali.jpg', import.meta.url).href,
    tags: ['Nightlife', 'Culture', 'City']
  },
  {
    id: 'eastern',
    name: 'Eastern Province',
    province: 'Eastern Province',
    category: 'Safari',
    description: 'Savanna safari routes, wildlife lodges and open landscapes for immersive nature travel.',
    image: new URL('../../assets/images/eastern.jpg', import.meta.url).href,
    tags: ['Wildlife', 'Safari', 'Adventure']
  },
  {
    id: 'northern',
    name: 'Northern Province',
    province: 'Northern Province',
    category: 'Mountains',
    description: 'Volcanic highlands, rainforest treks and premium mountain lodges with scenic views.',
    image: new URL('../../assets/images/north.jpg', import.meta.url).href,
    tags: ['Trekking', 'Volcanoes', 'Nature']
  },
  {
    id: 'southern',
    name: 'Southern Province',
    province: 'Southern Province',
    category: 'Culture',
    description: 'Heritage sites, coffee landscapes and cultural villages with authentic local stays.',
    image: new URL('../../assets/images/south.jpg', import.meta.url).href,
    tags: ['Culture', 'Heritage', 'History']
  },
  {
    id: 'western',
    name: 'Western Province',
    province: 'Western Province',
    category: 'Adventure',
    description: 'Lakefront resorts, rainforest canopy walks and adrenaline-filled adventure routes.',
    image: new URL('../../assets/images/west.jpg', import.meta.url).href,
    tags: ['Lakes', 'Forest', 'Adventure']
  }
]

const filteredDestinations = computed(() => {
  if (activeProvince.value === 'All Provinces') return destinations
  return destinations.filter((item) => item.province === activeProvince.value)
})

const setProvince = (province) => {
  activeProvince.value = province
}

const filterClass = (province) => activeProvince.value === province
  ? 'rounded-full bg-emerald-900 px-4 py-2 text-sm font-semibold text-white shadow-lg border border-emerald-900'
  : 'rounded-full border border-slate-200 bg-white/10 px-4 py-2 text-sm text-white backdrop-blur-md transition hover:bg-white/20'
</script>