<template>
  <section class="relative min-h-screen overflow-hidden text-white">
    <div class="absolute inset-0 bg-[url('@/assets/images/background2.jpg')] bg-cover bg-center opacity-80"></div>
    <div class="absolute inset-0 bg-gradient-to-br from-slate-950/80 via-slate-900/40 to-emerald-900/70"></div>

    <div class="relative z-10 flex min-h-screen flex-col justify-center px-6 py-16 lg:px-10">
      <div class="mb-8 inline-flex items-center gap-3 rounded-full border border-white/15 bg-white/10 px-4 py-2 text-xs uppercase tracking-[0.35em] text-white/80 backdrop-blur-xl shadow-xl">
        <span class="rounded-full bg-emerald-500/20 px-2 py-1">Enterprise</span>
        Rwanda Smart Tourism Ecosystem
      </div>

      <div class="grid gap-12 lg:grid-cols-[1.05fr_0.95fr]">
        <div class="space-y-6 text-center lg:text-left">
          <p class="text-sm uppercase tracking-[0.35em] text-emerald-300">About Tembera Urwanda</p>
          <h1 class="text-5xl md:text-7xl font-black tracking-tight">A next-generation luxury tourism platform for Rwanda.</h1>
          <p class="max-w-3xl text-lg text-white/75 md:text-xl">From AI-powered itineraries to analytics, smart booking, cultural guides and immersive destination dashboards — this site combines the feel of global travel leaders with Rwanda’s unique premium experiences.</p>

          <div class="mt-8 flex flex-wrap justify-center gap-4 lg:justify-start">
            <RouterLink to="/smart-search" class="inline-flex items-center justify-center rounded-full bg-gradient-to-r from-emerald-400 via-yellow-300 to-cyan-400 px-8 py-3 text-sm font-black text-slate-950 shadow-xl transition hover:scale-105">
              Explore AI search
            </RouterLink>
            <RouterLink to="/analytics" class="inline-flex items-center justify-center rounded-full border border-white/20 bg-white/10 px-8 py-3 text-sm font-black text-white transition hover:bg-white/20">
              View insights
            </RouterLink>
          </div>
        </div>

        <div class="rounded-[32px] border border-white/10 bg-white/10 p-6 backdrop-blur-xl shadow-2xl shadow-black/30">
          <div class="grid gap-4 sm:grid-cols-2">
            <div class="rounded-3xl bg-slate-950/40 p-5">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Premium visitors</p>
              <p class="mt-3 text-3xl font-black text-white">432K+</p>
            </div>
            <div class="rounded-3xl bg-slate-950/40 p-5">
              <p class="text-sm uppercase tracking-[0.25em] text-slate-300">Booking growth</p>
              <p class="mt-3 text-3xl font-black text-white">+18%</p>
            </div>
          </div>
          <div class="mt-6 rounded-3xl bg-slate-900/50 p-5">
            <h2 class="text-xl font-bold text-white">AI itinerary planner</h2>
            <p class="mt-3 text-slate-300">Generate a full travel plan with hotels, activities, restaurants, budgets and dates in seconds.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-slate-950 py-20 px-6 text-white">
    <div class="mx-auto max-w-6xl text-center">
      <p class="text-sm uppercase tracking-[0.35em] text-emerald-400">Platform features</p>
      <h2 class="mt-4 text-4xl font-black">Luxury travel features for every touring experience</h2>
      <p class="mt-4 max-w-3xl mx-auto text-white/70">Interactive dashboards, virtual tours, weather guides, community stories and smart analytics bring every traveler and operator together.</p>
    </div>

    <div class="mx-auto mt-16 grid gap-6 md:grid-cols-3">
      <article class="rounded-[32px] border border-white/10 bg-white/5 p-8 shadow-2xl transition hover:-translate-y-1">
        <h3 class="text-xl font-bold text-emerald-300">Smart analytics</h3>
        <p class="mt-3 text-white/70">Live visitor counters, province rankings, monthly growth charts and revenue projections.</p>
      </article>
      <article class="rounded-[32px] border border-white/10 bg-white/5 p-8 shadow-2xl transition hover:-translate-y-1">
        <h3 class="text-xl font-bold text-yellow-300">AI travel assistant</h3>
        <p class="mt-3 text-white/70">Personalized recommendations, trip planning, budgets and date suggestions for every type of traveler.</p>
      </article>
      <article class="rounded-[32px] border border-white/10 bg-white/5 p-8 shadow-2xl transition hover:-translate-y-1">
        <h3 class="text-xl font-bold text-sky-300">Community hub</h3>
        <p class="mt-3 text-white/70">Travel stories, reviews, user photos and tourism discussions to inspire every visit.</p>
      </article>
    </div>
  </section>

  <section class="py-20 px-6 text-slate-900">
    <div class="mx-auto max-w-6xl">
      <div class="grid gap-6 lg:grid-cols-[0.7fr_0.3fr]">
        <div class="rounded-[32px] border border-slate-200 bg-white p-8 shadow-2xl">
          <h2 class="text-3xl font-black text-slate-900">Why Tembera Urwanda?</h2>
          <p class="mt-4 text-slate-600">This platform brings Rwanda’s premium tourism ecosystem into a modern, enterprise-grade experience with every page, dashboard and booking workflow improved for international and local travelers alike.</p>
          <div class="mt-8 grid gap-4">
            <div class="rounded-3xl bg-slate-50 p-5">
              <p class="font-semibold text-slate-900">Luxury glassmorphism UI</p>
              <p class="mt-2 text-slate-600">Premium cards, gradients, particle style effects and advanced motion.</p>
            </div>
            <div class="rounded-3xl bg-slate-50 p-5">
              <p class="font-semibold text-slate-900">Real-time insights</p>
              <p class="mt-2 text-slate-600">Analytics, visitor trends and destination performance in one dashboard.</p>
            </div>
            <div class="rounded-3xl bg-slate-50 p-5">
              <p class="font-semibold text-slate-900">Travel intelligence</p>
              <p class="mt-2 text-slate-600">AI planning, predictive search and saved itineraries for premium trip design.</p>
            </div>
          </div>
        </div>

        <div class="rounded-[32px] border border-slate-200 bg-gradient-to-br from-emerald-500 to-cyan-500 p-8 text-white shadow-2xl">
          <h2 class="text-3xl font-black">Interactive tourism hub</h2>
          <p class="mt-4 text-white/80">Every traveler gets rich, content-led guidance with accessible tools for weather, safety, culture and events.</p>
          <div class="mt-8 grid gap-4">
            <div class="rounded-3xl bg-white/10 p-5">
              <p class="font-semibold">360° virtual tours</p>
              <p class="mt-2 text-sm text-white/75">Kigali, Akagera, Volcanoes, Nyungwe and Lake Kivu experiences.</p>
            </div>
            <div class="rounded-3xl bg-white/10 p-5">
              <p class="font-semibold">Accessibility and translation</p>
              <p class="mt-2 text-sm text-white/75">Keyboard navigation, high contrast, large text and multi-language support.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>