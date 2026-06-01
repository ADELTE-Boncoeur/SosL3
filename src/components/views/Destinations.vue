<template>
  <section class="relative overflow-hidden">
    <img :src="heroImage" alt="Rwanda destinations background" class="absolute inset-0 h-full w-full object-cover opacity-60" />
    <div class="absolute inset-0 bg-gradient-to-br from-slate-950/90 via-emerald-950/40 to-slate-950/90"></div>

    <div class="relative mx-auto max-w-7xl px-4 py-24 text-white">
      <div class="grid gap-12 lg:grid-cols-[1.2fr_0.8fr] lg:items-center">
        <div>
          <p class="text-sm uppercase tracking-[0.35em] text-emerald-300">Destinations</p>
          <h1 class="mt-4 text-5xl font-black tracking-tight sm:text-6xl">Discover Rwanda’s premium destinations with bold imagery.</h1>
          <p class="mt-6 max-w-3xl text-slate-200/80 animate-fade-in-up">From Kigali’s polished city scene to volcano treks, safari plains and lakeside retreats, explore curated travel stories with real photos and immersive details.</p>

          <div class="relative mt-10 max-w-md animate-fade-in-up">
            <label for="province-select" class="sr-only">Choose a province</label>
            <select
              id="province-select"
              v-model="activeProvince"
              class="w-full appearance-none rounded-full border border-white/20 bg-slate-950/75 px-5 py-3 pr-12 text-white shadow-lg outline-none transition duration-300 ease-out hover:border-white/40 focus:border-white/60 focus:ring-2 focus:ring-white/10"
            >
              <option v-for="option in provinceOptions" :key="option" :value="option">{{ option }}</option>
            </select>
            <span class="pointer-events-none absolute inset-y-0 right-4 flex items-center text-white/70">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="h-5 w-5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
              </svg>
            </span>
          </div>
        </div>

        <div class="rounded-[32px] border border-white/10 bg-white/10 p-6 backdrop-blur-xl shadow-2xl">
          <div class="space-y-6">
            <div>
              <p class="text-xs uppercase tracking-[0.35em] text-slate-300">Featured mood</p>
              <h2 class="mt-3 text-3xl font-black text-white">Iconic Rwanda moments</h2>
            </div>
            <div class="grid gap-4 sm:grid-cols-2">
              <div class="rounded-3xl bg-slate-950/60 p-5">
                <p class="text-sm uppercase tracking-[0.25em] text-slate-400">Best for</p>
                <p class="mt-3 text-2xl font-bold text-white">Culture & city</p>
              </div>
              <div class="rounded-3xl bg-slate-950/60 p-5">
                <p class="text-sm uppercase tracking-[0.25em] text-slate-400">Must see</p>
                <p class="mt-3 text-2xl font-bold text-white">Volcanoes & lakes</p>
              </div>
            </div>
            <div class="rounded-3xl bg-slate-950/70 p-5">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-400">Why choose Rwanda</p>
              <p class="mt-3 text-slate-200">Compact, safe and deeply scenic—Rwanda combines luxury safari, mountain adventure and refined urban living in one remarkable country.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-gradient-to-r from-sky-600 via-emerald-500 to-yellow-400 py-16 px-4 sm:px-6 lg:px-8">
    <div class="mx-auto max-w-7xl">
      <div class="mb-8 text-center text-white">
        <p class="text-sm uppercase tracking-[0.35em] text-white/80">Province photo guide</p>
        <h2 class="mt-3 text-4xl font-black">See each province in bright visual stories</h2>
      </div>
      <div class="grid gap-6 md:grid-cols-2 xl:grid-cols-5">
        <article v-for="province in provincePhotos" :key="province.id" class="overflow-hidden rounded-[32px] border border-white/10 bg-white/10 shadow-2xl backdrop-blur-xl transition hover:-translate-y-1 hover:bg-white/15">
          <img :src="province.image" :alt="province.name" class="h-48 w-full object-cover" />
          <div class="p-5">
            <h3 class="text-lg font-bold text-white">{{ province.name }}</h3>
            <p class="mt-2 text-sm text-white/90">{{ province.summary }}</p>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="page-shell py-20 text-slate-900">
    <div class="mx-auto max-w-7xl px-4 md:px-8">
      <div class="grid gap-10 lg:grid-cols-[1.1fr_0.9fr]">
        <div>
          <h2 class="text-4xl font-black text-slate-900">Plan your next stay with elegant destination previews</h2>
          <p class="mt-4 max-w-2xl text-slate-600">Each province is presented with destination highlights, travel style guidance and striking photography to help you choose the perfect Rwanda itinerary.</p>
        </div>

        <div class="grid gap-4 sm:grid-cols-2">
          <div class="rounded-[32px] bg-white p-6 shadow-lg">
            <p class="text-xs uppercase tracking-[0.35em] text-emerald-600">Popular</p>
            <h3 class="mt-3 text-xl font-black text-slate-900">Kigali Urban Escape</h3>
            <p class="mt-3 text-slate-600">Restaurants, museums, nightlife and modern Rwandan design.</p>
          </div>
          <div class="rounded-[32px] bg-white p-6 shadow-lg">
            <p class="text-xs uppercase tracking-[0.35em] text-sky-500">Adventure</p>
            <h3 class="mt-3 text-xl font-black text-slate-900">Volcano trails</h3>
            <p class="mt-3 text-slate-600">Luxury lodges, hiking, gorilla treks and mountain lodges.</p>
          </div>
        </div>
      </div>

      <div class="mt-12 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
        <article v-for="destination in filteredDestinations" :key="destination.id" class="group overflow-hidden rounded-[32px] border border-slate-200 bg-white shadow-xl transition duration-500 ease-out hover:-translate-y-3 hover:shadow-2xl hover:border-slate-300">
          <img :src="destination.image" :alt="destination.name" class="h-72 w-full object-cover transition duration-700 ease-out group-hover:scale-105" />
          <div class="p-6 transition-all duration-500 ease-out group-hover:bg-slate-50">
            <div class="flex flex-wrap items-center justify-between gap-4">
              <div>
                <h3 class="text-2xl font-bold text-slate-900">{{ destination.name }}</h3>
                <p class="mt-2 text-sm text-slate-500">{{ destination.province }}</p>
              </div>
              <span class="rounded-full bg-gradient-to-r from-sky-500 via-emerald-400 to-yellow-400 px-3 py-1 text-xs uppercase tracking-[0.2em] text-white shadow-sm">{{ destination.category }}</span>
            </div>
            <p class="mt-5 text-sm leading-7 text-slate-600">{{ destination.description }}</p>
            <div class="mt-6 flex flex-wrap gap-2">
              <span v-for="tag in destination.tags" :key="tag" class="rounded-full bg-slate-100 px-3 py-1 text-xs uppercase tracking-[0.2em] text-slate-600 transition duration-300 ease-out hover:bg-slate-200">{{ tag }}</span>
            </div>
          </div>
        </article>
      </div>

      <div class="mt-16 grid gap-6 lg:grid-cols-3">
        <article class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-2xl">
          <p class="text-sm uppercase tracking-[0.35em] text-emerald-600">Style</p>
          <h3 class="mt-4 text-2xl font-black text-slate-900">Luxury stays</h3>
          <p class="mt-4 text-slate-600">Premium lodges, curated suites, waterfront villas, and modern boutique hotels for discerning travelers.</p>
        </article>
        <article class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-2xl">
          <p class="text-sm uppercase tracking-[0.35em] text-yellow-500">Highlight</p>
          <h3 class="mt-4 text-2xl font-black text-slate-900">Adventure routing</h3>
          <p class="mt-4 text-slate-600">Combine city culture with safari, mountains, lakes and community experiences in one smart itinerary.</p>
        </article>
        <article class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-2xl">
          <p class="text-sm uppercase tracking-[0.35em] text-sky-500">Essentials</p>
          <h3 class="mt-4 text-2xl font-black text-slate-900">Local stories</h3>
          <p class="mt-4 text-slate-600">Travel with meaningful local interactions, cultural guides, museum visits and unforgettable performances.</p>
        </article>
      </div>

      <section class="mt-16 rounded-[32px] bg-gradient-to-r from-sky-600 via-emerald-500 to-yellow-400 p-8 text-white shadow-2xl">
        <div class="grid gap-6 lg:grid-cols-[1.2fr_0.8fr] lg:items-center">
          <div>
            <p class="text-sm uppercase tracking-[0.35em] text-white/80">AI concierge</p>
            <h3 class="mt-3 text-3xl font-black">Instant travel planning with smart support</h3>
            <p class="mt-4 max-w-2xl text-white/90">Chat with our AI travel assistant, book a premium itinerary, or connect instantly by phone and WhatsApp for your next Rwanda journey.</p>
          </div>
          <div class="grid gap-4 sm:grid-cols-2">
            <div class="flex items-center gap-4 rounded-3xl bg-white/15 p-5">
              <span class="inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-white/20 text-white">
                <svg viewBox="0 0 24 24" fill="currentColor" class="h-6 w-6">
                  <path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l1.82-1.82a1 1 0 011.11-.21 11.36 11.36 0 003.56.57 1 1 0 011 1V20a1 1 0 01-1 1A16 16 0 014 5a1 1 0 011-1h3.5a1 1 0 011 1 11.36 11.36 0 00.57 3.56 1 1 0 01-.21 1.11L6.62 10.79z"/>
                </svg>
              </span>
              <div>
                <p class="text-xs uppercase tracking-[0.35em] text-white/80">Phone</p>
                <p class="mt-1 font-semibold">+250 788 000 000</p>
              </div>
            </div>
            <div class="flex items-center gap-4 rounded-3xl bg-white/15 p-5">
              <span class="inline-flex h-12 w-12 items-center justify-center rounded-2xl bg-white/20 text-white">
                <svg viewBox="0 0 24 24" fill="currentColor" class="h-6 w-6">
                  <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.472-.149-.672.149-.198.297-.768.966-.942 1.165-.173.198-.347.223-.644.075-.297-.149-1.255-.462-2.39-1.475-.883-.786-1.48-1.754-1.653-2.051-.173-.297-.02-.458.13-.606.134-.131.297-.347.446-.52.149-.173.198-.298.298-.497.099-.198.05-.372-.025-.521-.075-.149-.672-1.612-.921-2.206-.242-.579-.487-.5-.672-.51l-.573-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.877 1.213 3.074c.149.198 2.1 3.2 5.076 4.487.709.306 1.26.489 1.69.626.71.227 1.36.195 1.87.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414-.074-.124-.273-.198-.57-.347z"/>
                  <path d="M12.004 2C6.486 2 2 6.486 2 12.003c0 2.112.643 4.069 1.743 5.72L2 22l4.417-1.712A9.957 9.957 0 0012.003 22C17.521 22 22 17.514 22 12.003S17.521 2 12.004 2zM12 20.008a8.013 8.013 0 01-4.114-1.136l-.294-.176-2.627 1.018.703-2.565-.191-.296A7.977 7.977 0 013.995 12.003C3.995 7.581 7.582 3.994 12 3.994c4.418 0 8.005 3.587 8.005 8.009C20.005 16.42 16.418 20.008 12 20.008z"/>
                </svg>
              </span>
              <div>
                <p class="text-xs uppercase tracking-[0.35em] text-white/80">WhatsApp</p>
                <p class="mt-1 font-semibold">+250 788 111 111</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div class="mt-16 grid gap-10 lg:grid-cols-[0.75fr_0.25fr]">
        <div class="rounded-[32px] border border-slate-200 bg-slate-950 p-8 text-white shadow-2xl">
          <p class="text-sm uppercase tracking-[0.35em] text-slate-400">Destination films</p>
          <h3 class="mt-4 text-3xl font-black">See the country through film</h3>
          <p class="mt-4 text-slate-300">Watch a trio of curated destination clips that capture Rwanda’s landscapes, city pulse and waterfall serenity.</p>
          <div class="mt-8 grid gap-4 sm:grid-cols-2">
            <video v-for="(source, index) in videoSources" :key="index" controls muted loop playsinline class="h-40 w-full rounded-3xl border border-slate-800 bg-slate-900 object-cover">
              <source :src="source" type="video/mp4" />
            </video>
          </div>
        </div>

        <div class="space-y-6">
          <div class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-2xl">
            <p class="text-sm uppercase tracking-[0.35em] text-emerald-600">Why visit</p>
            <h3 class="mt-4 text-2xl font-black text-slate-900">Compact yet varied</h3>
            <p class="mt-4 text-slate-600">Rwanda is easy to explore and offers mountains, savanna, lakes and vibrant city life within a short journey.</p>
          </div>
          <div class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-2xl">
            <p class="text-sm uppercase tracking-[0.35em] text-slate-500">Tip</p>
            <h3 class="mt-4 text-2xl font-black text-slate-900">Book premium experiences</h3>
            <p class="mt-4 text-slate-600">Choose curated tours, luxury transport and private guides to make every trip truly memorable.</p>
          </div>
        </div>
      </div>
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
const provinceOptions = [
  'All Provinces',
  'Kigali',
  'Northern Province',
  'Southern Province',
  'Eastern Province',
  'Western Province'
]

const provincePhotos = [
  {
    id: 'kigali',
    name: 'Kigali City',
    summary: 'A refined urban gateway with design hotels, galleries and city culture.',
    image: new URL('../../assets/images/kigali.jpg', import.meta.url).href
  },
  {
    id: 'eastern',
    name: 'Eastern Province',
    summary: 'Wide safari plains and wildlife lodges with luminous golden landscapes.',
    image: new URL('../../assets/images/eastern.jpg', import.meta.url).href
  },
  {
    id: 'northern',
    name: 'Northern Province',
    summary: 'Volcano forests and mountain views for premium treks and nature stays.',
    image: new URL('../../assets/images/north.jpg', import.meta.url).href
  },
  {
    id: 'southern',
    name: 'Southern Province',
    summary: 'Coffee hills, cultural villages and softly lit heritage scenes.',
    image: new URL('../../assets/images/south.jpg', import.meta.url).href
  },
  {
    id: 'western',
    name: 'Western Province',
    summary: 'Lakefront resorts, rainforest canopies and adventure-rich coastlines.',
    image: new URL('../../assets/images/west.jpg', import.meta.url).href
  }
]

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
</script>

<style scoped>
@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in-up {
  animation: fade-in-up 0.9s ease-out forwards;
}
</style>
