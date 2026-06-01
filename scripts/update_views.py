from pathlib import Path

about_content = """<template>
  <section class=\"relative overflow-hidden text-white\">
    <img :src=\"heroImage\" alt=\"Rwanda aerial view\" class=\"absolute inset-0 h-full w-full object-cover opacity-70\" />
    <div class=\"absolute inset-0 bg-gradient-to-br from-slate-950/90 via-slate-900/40 to-emerald-950/80\"></div>

    <div class=\"relative z-10 mx-auto max-w-7xl px-6 py-24 lg:px-10\">
      <div class=\"grid gap-12 lg:grid-cols-[1.1fr_0.9fr] lg:items-center\">
        <div>
          <p class=\"text-sm uppercase tracking-[0.35em] text-emerald-300\">About Rwanda Luxury Travel</p>
          <h1 class=\"mt-6 text-5xl font-black tracking-tight sm:text-6xl\">Crafting the premium Rwanda travel story with vision and authenticity.</h1>
          <p class=\"mt-6 max-w-3xl text-lg text-slate-200/90 sm:text-xl\">Tembera Urwanda blends smart tourism, destination storytelling and cultural respect to create a modern platform for luxury guests, investors and travel partners.</p>

          <div class=\"mt-10 flex flex-wrap gap-4\">
            <router-link to=\"/destinations\" class=\"inline-flex items-center justify-center rounded-full bg-emerald-400 px-8 py-3 text-sm font-black text-slate-950 transition hover:scale-105\">
              Explore destinations
            </router-link>
            <a href=\"#values\" class=\"inline-flex items-center justify-center rounded-full border border-white/20 bg-white/10 px-8 py-3 text-sm font-black text-white transition hover:bg-white/20\">
              Read our values
            </a>
          </div>
        </div>

        <div class=\"grid gap-4 sm:grid-cols-2\">
          <div class=\"rounded-[32px] border border-white/10 bg-white/10 p-6 backdrop-blur-xl shadow-2xl\">
            <p class=\"text-xs uppercase tracking-[0.35em] text-slate-300\">Experience</p>
            <h2 class=\"mt-4 text-4xl font-black\">15+</h2>
            <p class=\"mt-3 text-slate-200\">Luxury travel concepts and destination designs curated for Rwanda.</p>
          </div>
          <div class=\"rounded-[32px] border border-white/10 bg-white/10 p-6 backdrop-blur-xl shadow-2xl\">
            <p class=\"text-xs uppercase tracking-[0.35em] text-slate-300\">Focus</p>
            <h2 class=\"mt-4 text-4xl font-black\">Sustainable</h2>
            <p class=\"mt-3 text-slate-200\">Responsible tourism, culture-led hospitality and exceptional guest journeys.</p>
          </div>
          <div class=\"rounded-[32px] border border-white/10 bg-white/10 p-6 backdrop-blur-xl shadow-2xl\">
            <p class=\"text-xs uppercase tracking-[0.35em] text-slate-300\">Design</p>
            <h2 class=\"mt-4 text-4xl font-black\">Bespoke</h2>
            <p class=\"mt-3 text-slate-200\">Curated brand experiences with photography, motion, and rich content at every touchpoint.</p>
          </div>
          <div class=\"rounded-[32px] border border-white/10 bg-white/10 p-6 backdrop-blur-xl shadow-2xl\">
            <p class=\"text-xs uppercase tracking-[0.35em] text-slate-300\">Culture</p>
            <h2 class=\"mt-4 text-4xl font-black\">Authentic</h2>
            <p class=\"mt-3 text-slate-200\">Local stories, heritage rituals and people-first narratives throughout the platform.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class=\"bg-slate-950 py-20 px-6 text-white\" id=\"values\">
    <div class=\"mx-auto max-w-6xl\">
      <div class=\"text-center\">
        <p class=\"text-sm uppercase tracking-[0.35em] text-emerald-400\">Our purpose</p>
        <h2 class=\"mt-4 text-4xl font-black\">Why Tembera Urwanda exists</h2>
        <p class=\"mt-4 max-w-2xl mx-auto text-slate-300\">We create a compelling luxury tourism experience for Rwanda with clear storytelling, immersive photography, and seamless access to each region’s finest attractions.</p>
      </div>

      <div class=\"mt-16 grid gap-6 md:grid-cols-3\">
        <article class=\"rounded-[32px] border border-white/10 bg-white/5 p-8 shadow-2xl\">
          <h3 class=\"text-xl font-bold text-emerald-300\">Showcase Rwanda</h3>
          <p class=\"mt-4 text-slate-200\">Highlight premium destinations, cultural experiences, and modern hospitality with a polished visual language.</p>
        </article>
        <article class=\"rounded-[32px] border border-white/10 bg-white/5 p-8 shadow-2xl\">
          <h3 class=\"text-xl font-bold text-yellow-300\">Inspire travel</h3>
          <p class=\"mt-4 text-slate-200\">Turn curiosity into high-value trips through beautiful storytelling, destination insights, and local imagery.</p>
        </article>
        <article class=\"rounded-[32px] border border-white/10 bg-white/5 p-8 shadow-2xl\">
          <h3 class=\"text-xl font-bold text-sky-300\">Build trust</h3>
          <p class=\"mt-4 text-slate-200\">Provide a professional platform for partners, guests and decision makers to explore Rwanda’s tourism potential.</p>
        </article>
      </div>
    </div>
  </section>

  <section class=\"py-20 px-6 text-slate-900\">
    <div class=\"mx-auto max-w-6xl grid gap-12 lg:grid-cols-[0.65fr_0.35fr]\">
      <div class=\"space-y-10 rounded-[32px] border border-slate-200 bg-white p-10 shadow-2xl\">
        <div class=\"space-y-4\">
          <p class=\"text-sm uppercase tracking-[0.35em] text-emerald-500\">Our story</p>
          <h2 class=\"text-4xl font-black\">A modern tourism platform with deep local roots</h2>
        </div>
        <p class=\"text-slate-600 leading-8\">Tembera Urwanda brings together Rwanda’s strength in innovation, sustainability and hospitality. The platform is designed to reflect the country’s dynamic cities, rainforest escapes, volcano treks and lakeside luxury while giving travelers an intuitive path to explore and book.</p>
        <p class=\"text-slate-600 leading-8\">Every section is built to tell a richer story—whether through curated photo galleries, destination summaries, or intelligent trip guidance. The goal is to make Rwanda feel both aspirational and accessible without losing the authenticity of local culture.</p>
      </div>

      <div class=\"grid gap-6\">
        <div class=\"rounded-[32px] overflow-hidden shadow-2xl\">
          <img :src=\"storyImageA\" alt=\"Rwanda heritage\" class=\"h-80 w-full object-cover\" />
        </div>
        <div class=\"rounded-[32px] overflow-hidden shadow-2xl\">
          <img :src=\"storyImageB\" alt=\"Rwanda landscapes\" class=\"h-80 w-full object-cover\" />
        </div>
      </div>
    </div>
  </section>

  <section class=\"bg-slate-950 py-20 px-6 text-white\">
    <div class=\"mx-auto max-w-6xl\">
      <div class=\"grid gap-6 lg:grid-cols-3\">
        <div class=\"rounded-[32px] bg-white/5 p-8 shadow-2xl\">
          <p class=\"text-sm uppercase tracking-[0.35em] text-emerald-300\">What we deliver</p>
          <h3 class=\"mt-4 text-3xl font-black\">Complete tourism storytelling</h3>
          <p class=\"mt-4 text-slate-300\">Visual direction, destination copy, immersive imagery, and premium interaction design for every traveler.</p>
        </div>
        <div class=\"rounded-[32px] bg-white/5 p-8 shadow-2xl\">
          <h3 class=\"text-2xl font-bold text-white\">Destination photography</h3>
          <p class=\"mt-4 text-slate-300\">A curated suite of visuals for Kigali, national parks, tea hills, waterfalls, and cultural moments.</p>
        </div>
        <div class=\"rounded-[32px] bg-white/5 p-8 shadow-2xl\">
          <h3 class=\"text-2xl font-bold text-white\">Premium user journeys</h3>
          <p class=\"mt-4 text-slate-300\">From browsing destinations to planning itineraries and viewing partner opportunities, every experience feels deliberate.</p>
        </div>
      </div>
    </div>
  </section>

  <section class=\"py-20 px-6 text-slate-900\">
    <div class=\"mx-auto max-w-6xl text-center\">
      <p class=\"text-sm uppercase tracking-[0.35em] text-emerald-500\">Photo showcase</p>
      <h2 class=\"mt-4 text-4xl font-black\">Visual moments from Rwanda</h2>
      <p class=\"mt-4 max-w-3xl mx-auto text-slate-600\">A gallery of inviting landscapes, city life and cultural connection helps guests imagine the next premium trip.</p>
    </div>

    <div class=\"mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4\">
      <div class=\"overflow-hidden rounded-[28px] shadow-2xl\">
        <img :src=\"galleryA\" alt=\"Rwanda city scene\" class=\"h-72 w-full object-cover\" />
      </div>
      <div class=\"overflow-hidden rounded-[28px] shadow-2xl\">
        <img :src=\"galleryB\" alt=\"Rwanda nature\" class=\"h-72 w-full object-cover\" />
      </div>
      <div class=\"overflow-hidden rounded-[28px] shadow-2xl\">
        <img :src=\"galleryC\" alt=\"Rwanda culture\" class=\"h-72 w-full object-cover\" />
      </div>
      <div class=\"overflow-hidden rounded-[28px] shadow-2xl\">
        <img :src=\"galleryD\" alt=\"Rwanda tourism\" class=\"h-72 w-full object-cover\" />
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
"""

dest_content = """<template>
  <section class=\"relative overflow-hidden\">
    <img :src=\"heroImage\" alt=\"Rwanda destinations background\" class=\"absolute inset-0 h-full w-full object-cover opacity-60\" />
    <div class=\"absolute inset-0 bg-gradient-to-br from-slate-950/90 via-emerald-950/40 to-slate-950/90\"></div>

    <div class=\"relative mx-auto max-w-7xl px-4 py-24 text-white\">
      <div class=\"grid gap-12 lg:grid-cols-[1.2fr_0.8fr] lg:items-center\">
        <div>
          <p class=\"text-sm uppercase tracking-[0.35em] text-emerald-300\">Destinations</p>
          <h1 class=\"mt-4 text-5xl font-black tracking-tight sm:text-6xl\">Discover Rwanda’s premium destinations with bold imagery.</h1>
          <p class=\"mt-6 max-w-3xl text-slate-200/80\">From Kigali’s polished city scene to volcano treks, safari plains and lakeside retreats, explore curated travel stories with real photos and immersive details.</p>

          <div class=\"mt-10 flex flex-wrap gap-3\">
            <button @click=\"setProvince('All Provinces')\" :class=\"filterClass('All Provinces')\">All</button>
            <button @click=\"setProvince('Kigali')\" :class=\"filterClass('Kigali')\">Kigali</button>
            <button @click=\"setProvince('Northern Province')\" :class=\"filterClass('Northern Province')\">North</button>
            <button @click=\"setProvince('Southern Province')\" :class=\"filterClass('Southern Province')\">South</button>
            <button @click=\"setProvince('Eastern Province')\" :class=\"filterClass('Eastern Province')\">East</button>
            <button @click=\"setProvince('Western Province')\" :class=\"filterClass('Western Province')\">West</button>
          </div>
        </div>

        <div class=\"rounded-[32px] border border-white/10 bg-white/10 p-6 backdrop-blur-xl shadow-2xl\">
          <div class=\"space-y-6\">
            <div>
              <p class=\"text-xs uppercase tracking-[0.35em] text-slate-300\">Featured mood</p>
              <h2 class=\"mt-3 text-3xl font-black text-white\">Iconic Rwanda moments</h2>
            </div>
            <div class=\"grid gap-4 sm:grid-cols-2\">
              <div class=\"rounded-3xl bg-slate-950/60 p-5\">
                <p class=\"text-sm uppercase tracking-[0.25em] text-slate-400\">Best for</p>
                <p class=\"mt-3 text-2xl font-bold text-white\">Culture & city</p>
              </div>
              <div class=\"rounded-3xl bg-slate-950/60 p-5\">
                <p class=\"text-sm uppercase tracking-[0.25em] text-slate-400\">Must see</p>
                <p class=\"mt-3 text-2xl font-bold text-white\">Volcanoes & lakes</p>
              </div>
            </div>
            <div class=\"rounded-3xl bg-slate-950/70 p-5\">
              <p class=\"text-sm uppercase tracking-[0.25em] text-slate-400\">Why choose Rwanda</p>
              <p class=\"mt-3 text-slate-200\">Compact, safe and deeply scenic—Rwanda combines luxury safari, mountain adventure and refined urban living in one remarkable country.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class=\"page-shell py-20 text-slate-900\">
    <div class=\"mx-auto max-w-7xl px-4 md:px-8\">
      <div class=\"grid gap-10 lg:grid-cols-[1.1fr_0.9fr]\">
        <div>
          <h2 class=\"text-4xl font-black text-slate-900\">Plan your next stay with elegant destination previews</h2>
          <p class=\"mt-4 max-w-2xl text-slate-600\">Each province is presented with destination highlights, travel style guidance and striking photography to help you choose the perfect Rwanda itinerary.</p>
        </div>

        <div class=\"grid gap-4 sm:grid-cols-2\">
          <div class=\"rounded-[32px] bg-white p-6 shadow-lg\">
            <p class=\"text-xs uppercase tracking-[0.35em] text-emerald-600\">Popular</p>
            <h3 class=\"mt-3 text-xl font-black text-slate-900\">Kigali Urban Escape</h3>
            <p class=\"mt-3 text-slate-600\">Restaurants, museums, nightlife and modern Rwandan design.</p>
          </div>
          <div class=\"rounded-[32px] bg-white p-6 shadow-lg\">
            <p class=\"text-xs uppercase tracking-[0.35em] text-sky-500\">Adventure</p>
            <h3 class=\"mt-3 text-xl font-black text-slate-900\">Volcano trails</h3>
            <p class=\"mt-3 text-slate-600\">Luxury lodges, hiking, gorilla treks and mountain lodges.</p>
          </div>
        </div>
      </div>

      <div class=\"mt-12 grid gap-6 md:grid-cols-2 xl:grid-cols-3\">
        <article v-for=\"destination in filteredDestinations\" :key=\"destination.id\" class=\"group overflow-hidden rounded-[32px] border border-slate-200 bg-white shadow-xl transition hover:-translate-y-1 hover:shadow-2xl\">
          <img :src=\"destination.image\" :alt=\"destination.name\" class=\"h-72 w-full object-cover transition duration-500 group-hover:scale-105\" />
          <div class=\"p-6\">
            <div class=\"flex flex-wrap items-center justify-between gap-4\">
              <div>
                <h3 class=\"text-2xl font-bold text-slate-900\">{{ destination.name }}</h3>
                <p class=\"mt-2 text-sm text-slate-500\">{{ destination.province }}</p>
              </div>
              <span class=\"rounded-full bg-slate-100 px-3 py-1 text-xs uppercase tracking-[0.2em] text-slate-600\">{{ destination.category }}</span>
            </div>
            <p class=\"mt-5 text-sm leading-7 text-slate-600\">{{ destination.description }}</p>
            <div class=\"mt-6 flex flex-wrap gap-2\">
              <span v-for=\"tag in destination.tags\" :key=\"tag\" class=\"rounded-full bg-slate-100 px-3 py-1 text-xs uppercase tracking-[0.2em] text-slate-600\">{{ tag }}</span>
            </div>
          </div>
        </article>
      </div>

      <div class=\"mt-16 grid gap-6 lg:grid-cols-3\">
        <article class=\"rounded-[32px] border border-slate-200 bg-white p-8 shadow-2xl\">
          <p class=\"text-sm uppercase tracking-[0.35em] text-emerald-600\">Style</p>
          <h3 class=\"mt-4 text-2xl font-black text-slate-900\">Luxury stays</h3>
          <p class=\"mt-4 text-slate-600\">Premium lodges, curated suites, waterfront villas, and modern boutique hotels for discerning travelers.</p>
        </article>
        <article class=\"rounded-[32px] border border-slate-200 bg-white p-8 shadow-2xl\">
          <p class=\"text-sm uppercase tracking-[0.35em] text-yellow-500\">Highlight</p>
          <h3 class=\"mt-4 text-2xl font-black text-slate-900\">Adventure routing</h3>
          <p class=\"mt-4 text-slate-600\">Combine city culture with safari, mountains, lakes and community experiences in one smart itinerary.</p>
        </article>
        <article class=\"rounded-[32px] border border-slate-200 bg-white p-8 shadow-2xl\">
          <p class=\"text-sm uppercase tracking-[0.35em] text-sky-500\">Essentials</p>
          <h3 class=\"mt-4 text-2xl font-black text-slate-900\">Local stories</h3>
          <p class=\"mt-4 text-slate-600\">Travel with meaningful local interactions, cultural guides, museum visits and unforgettable performances.</p>
        </article>
      </div>

      <div class=\"mt-16 grid gap-10 lg:grid-cols-[0.75fr_0.25fr]\">
        <div class=\"rounded-[32px] border border-slate-200 bg-slate-950 p-8 text-white shadow-2xl\">
          <p class=\"text-sm uppercase tracking-[0.35em] text-slate-400\">Destination films</p>
          <h3 class=\"mt-4 text-3xl font-black\">See the country through film</h3>
          <p class=\"mt-4 text-slate-300\">Watch a trio of curated destination clips that capture Rwanda’s landscapes, city pulse and waterfall serenity.</p>
          <div class=\"mt-8 grid gap-4 sm:grid-cols-2\">
            <video v-for=\"(source, index) in videoSources\" :key=\"index\" controls muted loop playsinline class=\"h-40 w-full rounded-3xl border border-slate-800 bg-slate-900 object-cover\">
              <source :src=\"source\" type=\"video/mp4\" />
            </video>
          </div>
        </div>

        <div class=\"space-y-6\">
          <div class=\"rounded-[32px] border border-slate-200 bg-white p-8 shadow-2xl\">
            <p class=\"text-sm uppercase tracking-[0.35em] text-emerald-600\">Why visit</p>
            <h3 class=\"mt-4 text-2xl font-black text-slate-900\">Compact yet varied</h3>
            <p class=\"mt-4 text-slate-600\">Rwanda is easy to explore and offers mountains, savanna, lakes and vibrant city life within a short journey.</p>
          </div>
          <div class=\"rounded-[32px] border border-slate-200 bg-white p-8 shadow-2xl\">
            <p class=\"text-sm uppercase tracking-[0.35em] text-slate-500\">Tip</p>
            <h3 class=\"mt-4 text-2xl font-black text-slate-900\">Book premium experiences</h3>
            <p class=\"mt-4 text-slate-600\">Choose curated tours, luxury transport and private guides to make every trip truly memorable.</p>
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
"""

Path('src/components/views/about.vue').write_text(about_content, encoding='utf-8')
Path('src/components/views/Destinations.vue').write_text(dest_content, encoding='utf-8')
