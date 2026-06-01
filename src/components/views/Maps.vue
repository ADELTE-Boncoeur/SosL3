<template>
  <section class="page-shell py-12 text-slate-900">
    <div class="mx-auto grid max-w-7xl gap-8 px-4 md:px-8 xl:grid-cols-[1.05fr_0.95fr]">
      <article class="page-card overflow-hidden p-0">
        <div class="bg-[linear-gradient(135deg,#14532d,#15803d,#38bdf8)] p-8 text-white">
          <p class="text-sm uppercase tracking-[0.35em] text-emerald-100">Maps & directions</p>
          <h1 class="mt-4 text-4xl font-black md:text-5xl">Plan every route with confidence</h1>
          <p class="mt-4 max-w-2xl text-emerald-50/90">A premium travel planner for Rwanda with elegant route previews, scenic stops, and clear destination guidance.</p>
        </div>

        <div class="p-8">
          <div class="rounded-[28px] border border-emerald-100 bg-[linear-gradient(180deg,#ecfdf5,#ffffff)] p-5 shadow-xl shadow-emerald-100/80">
            <label class="text-sm font-semibold uppercase tracking-[0.25em] text-emerald-700">Search destination</label>
            <div class="mt-4 flex flex-wrap gap-3">
              <input v-model="searchLocation" type="text" placeholder="Try Kigali, Musanze, Lake Kivu..." class="min-w-[220px] flex-1 rounded-full border border-emerald-200 bg-white px-4 py-3 text-sm shadow-sm outline-none" @keyup.enter="handleSearch" />
              <button @click="handleSearch" class="rounded-full bg-[linear-gradient(135deg,#22c55e,#facc15,#38bdf8)] px-5 py-3 text-sm font-black text-emerald-950 shadow-lg transition hover:-translate-y-0.5">Search</button>
            </div>
          </div>

          <div class="mt-6 grid gap-6 lg:grid-cols-[0.65fr_0.35fr]">
            <div class="overflow-hidden rounded-[32px] border border-emerald-100 bg-white shadow-2xl shadow-emerald-100/80">
              <iframe class="h-[340px] w-full md:h-[420px]" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3987.414592303462!2d30.061!3d-1.944!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x19dca6a!2sKigali!5e0!3m2!1sen!2srw!4v1710000000000" allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>

            <div class="rounded-[32px] border border-emerald-100 bg-white p-6 shadow-2xl shadow-emerald-100/80">
              <h2 class="text-xl font-bold text-slate-900">Province hotspots</h2>
              <div class="mt-5 space-y-4">
                <button v-for="province in provinces" :key="province" class="w-full rounded-3xl border border-slate-200 bg-slate-50 px-4 py-4 text-left text-sm font-semibold text-slate-900 transition hover:bg-emerald-50">{{ province }}</button>
              </div>
            </div>
          </div>
        </div>
      </article>

      <article class="page-card p-8">
        <div class="flex flex-wrap items-center justify-between gap-4">
          <div>
            <p class="text-sm uppercase tracking-[0.35em] text-emerald-600">Popular routes</p>
            <h2 class="mt-4 text-3xl font-black text-emerald-800">Top Rwanda itineraries</h2>
          </div>
          <span class="rounded-full bg-emerald-100 px-4 py-2 text-xs font-semibold uppercase tracking-[0.25em] text-emerald-800">Interactive</span>
        </div>
        <p class="mt-3 text-slate-600">Choose a route, explore scenic stops, and compare travel plans across Rwanda.</p>

        <div class="mt-6 space-y-4">
          <div v-for="route in routes" :key="route.id" class="rounded-[28px] border border-slate-200 bg-[linear-gradient(180deg,#f0fdf4,#ffffff)] p-5 shadow-xl shadow-emerald-100/80">
            <div class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
              <div>
                <h3 class="text-xl font-bold text-emerald-800">{{ route.from }} → {{ route.to }}</h3>
                <p class="mt-1 text-sm text-slate-600">Distance: {{ route.distance }} · Estimated time: {{ route.duration }}</p>
              </div>
              <button class="rounded-full bg-gradient-to-r from-emerald-500 to-cyan-500 px-5 py-3 text-sm font-black text-slate-950 shadow-md transition hover:-translate-y-0.5">View route</button>
            </div>
          </div>
        </div>

        <div class="mt-10 rounded-[32px] bg-gradient-to-br from-emerald-500 to-cyan-500 p-6 text-white shadow-2xl">
          <h2 class="text-xl font-bold">Tourism heatmap</h2>
          <p class="mt-3 text-white/80">Visualize tourism density and trending districts in every province.</p>
          <div class="mt-6 grid gap-3 text-sm">
            <div class="rounded-3xl bg-white/10 p-4">Kigali: high city traffic, great for business tourism.</div>
            <div class="rounded-3xl bg-white/10 p-4">Western Province: premium adventure and lake escapes.</div>
            <div class="rounded-3xl bg-white/10 p-4">Eastern Province: safari demand and wildlife safaris.</div>
          </div>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const searchLocation = ref('')
const provinces = ['Kigali City', 'Northern Province', 'Southern Province', 'Western Province', 'Eastern Province']
const routes = ref([
  { id: 1, from: 'Kigali', to: 'Musanze', distance: '110 km', duration: '3 hrs' },
  { id: 2, from: 'Kigali', to: 'Lake Kivu', distance: '250 km', duration: '5 hrs' },
  { id: 3, from: 'Kigali', to: 'Huye', distance: '140 km', duration: '3.5 hrs' }
])

const handleSearch = () => {
  if (!searchLocation.value.trim()) {
    alert('Type a destination to preview travel ideas.')
    return
  }
  alert(`Showing route ideas for ${searchLocation.value}`)
}
</script>

