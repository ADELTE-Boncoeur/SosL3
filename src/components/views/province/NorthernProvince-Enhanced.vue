<template>
  <!-- ======================== NORTHERN PROVINCE HERO ======================== -->
  <section class="relative min-h-screen overflow-hidden text-white flex items-center">
    <video 
      autoplay 
      muted 
      loop 
      playsinline 
      class="absolute inset-0 h-full w-full object-cover opacity-50"
    >
      <source src="@/assets/images/Uruguay Feel Nature (1 min) - Instituto Nacional de Carnes (720p, h264).mp4" type="video/mp4" />
    </video>

    <!-- Epic overlay -->
    <div class="absolute inset-0 bg-gradient-to-b from-slate-950/40 via-slate-950/50 to-slate-950/70"></div>

    <div class="relative z-10 mx-auto max-w-7xl px-4 py-20 lg:px-10 w-full">
      <div class="max-w-3xl fade-in-up">
        <p class="text-sm uppercase tracking-[0.35em] text-red-300 font-bold">Mountain Adventure</p>
        <h1 class="mt-6 text-6xl md:text-8xl font-black leading-tight tracking-tight">
          <span class="bg-gradient-to-r from-red-300 via-orange-300 to-yellow-300 bg-clip-text text-transparent drop-shadow-2xl">
            Northern Province
          </span>
        </h1>
        <p class="mt-8 max-w-2xl text-xl text-white/90">Experience Rwanda's most epic landscapes. Trek through misty volcanic highlands, encounter endangered mountain gorillas, and explore pristine rainforests from luxury mountain lodges.</p>
        
        <div class="mt-10 flex flex-wrap gap-4">
          <button class="rounded-full bg-gradient-to-r from-red-500 to-orange-500 px-8 py-4 font-black text-white shadow-2xl hover:scale-110 transition-transform">
            Plan Your Trek
          </button>
          <button class="rounded-full border-2 border-white/40 bg-white/10 px-8 py-4 font-black text-white backdrop-blur-sm hover:bg-white/20">
            View Gallery
          </button>
        </div>
      </div>
    </div>

    <!-- Scroll indicator -->
    <div class="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
      <div class="flex h-12 w-7 justify-center rounded-full border-2 border-white/60 bg-white/10 backdrop-blur-md">
        <div class="mt-3 h-2 w-1 rounded-full bg-white"></div>
      </div>
    </div>
  </section>

  <!-- ======================== IMMERSIVE EXPERIENCE SECTION ======================== -->
  <section class="relative bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 py-24 px-4 text-white overflow-hidden">
    <div class="absolute inset-0 pointer-events-none">
      <div class="absolute top-20 right-10 w-72 h-72 bg-red-500/10 rounded-full blur-3xl opacity-20"></div>
      <div class="absolute bottom-20 left-10 w-96 h-96 bg-orange-500/10 rounded-full blur-3xl opacity-20"></div>
    </div>

    <div class="relative z-10 mx-auto max-w-7xl">
      <!-- Section intro -->
      <div class="text-center mb-16 fade-in-up" data-scroll-reveal>
        <p class="text-sm uppercase tracking-[0.35em] text-red-400 font-bold">Epic Experiences</p>
        <h2 class="mt-4 text-5xl md:text-6xl font-black">Mountain Gorilla Encounters</h2>
        <p class="mt-6 max-w-2xl mx-auto text-lg text-white/70">Trek into the misty rainforest to encounter the magnificent mountain gorillas in their natural habitat. A transformative experience with expert guides in Rwanda's volcanic highlands.</p>
      </div>

      <!-- Feature cards grid -->
      <div class="grid gap-6 md:grid-cols-2 xl:grid-cols-3 mb-12">
        <article class="group rounded-[32px] border border-white/15 bg-white/5 p-8 shadow-2xl hover:-translate-y-2 transition-all duration-500 backdrop-blur-sm card-hover-glow">
          <div class="text-4xl mb-4">🦍</div>
          <h3 class="text-2xl font-black text-white">Gorilla Trekking</h3>
          <p class="mt-3 text-white/80">Expert-guided treks to encounter endangered mountain gorillas in their pristine rainforest home.</p>
          <div class="mt-4 flex gap-2">
            <span class="rounded-full bg-red-500/20 px-3 py-1 text-xs font-bold text-red-200">Wildlife</span>
            <span class="rounded-full bg-orange-500/20 px-3 py-1 text-xs font-bold text-orange-200">Adventure</span>
          </div>
        </article>

        <article class="group rounded-[32px] border border-white/15 bg-white/5 p-8 shadow-2xl hover:-translate-y-2 transition-all duration-500 backdrop-blur-sm card-hover-glow">
          <div class="text-4xl mb-4">⛰️</div>
          <h3 class="text-2xl font-black text-white">Volcano Exploration</h3>
          <p class="mt-3 text-white/80">Hike across volcanic terrain, crater lakes, and ancient lava fields in dramatic mountain landscapes.</p>
          <div class="mt-4 flex gap-2">
            <span class="rounded-full bg-yellow-500/20 px-3 py-1 text-xs font-bold text-yellow-200">Hiking</span>
            <span class="rounded-full bg-red-500/20 px-3 py-1 text-xs font-bold text-red-200">Nature</span>
          </div>
        </article>

        <article class="group rounded-[32px] border border-white/15 bg-white/5 p-8 shadow-2xl hover:-translate-y-2 transition-all duration-500 backdrop-blur-sm card-hover-glow">
          <div class="text-4xl mb-4">🏨</div>
          <h3 class="text-2xl font-black text-white">Luxury Lodges</h3>
          <p class="mt-3 text-white/80">Premium mountain accommodations with breathtaking views, spa services, and gourmet dining experiences.</p>
          <div class="mt-4 flex gap-2">
            <span class="rounded-full bg-orange-500/20 px-3 py-1 text-xs font-bold text-orange-200">Luxury</span>
            <span class="rounded-full bg-amber-500/20 px-3 py-1 text-xs font-bold text-amber-200">Comfort</span>
          </div>
        </article>
      </div>

      <!-- Large featured image section -->
      <div class="rounded-[40px] border border-white/15 overflow-hidden shadow-2xl mb-12 fade-in-up" data-scroll-reveal>
        <img 
          src="@/assets/images/background.jpg" 
          alt="Northern Province mountain landscape" 
          class="w-full h-96 md:h-[500px] object-cover group-hover:scale-105 transition-transform duration-700"
        />
      </div>

      <!-- Destination highlights -->
      <div class="grid gap-6 lg:grid-cols-[1fr_1.2fr_1fr] items-stretch">
        <!-- Left info -->
        <article class="rounded-[32px] border border-white/15 bg-gradient-to-br from-red-900/40 to-red-950/60 p-8 backdrop-blur-sm flex flex-col justify-center fade-in-up" data-scroll-reveal style="animation-delay: 0.2s">
          <p class="text-xs uppercase tracking-[0.35em] text-red-300 font-bold">Exploration</p>
          <h3 class="mt-4 text-3xl font-black text-white">Hidden Treasures</h3>
          <p class="mt-4 text-white/80">Discover remote trails, hidden waterfalls, and pristine viewpoints that reveal Rwanda's most dramatic landscapes.</p>
        </article>

        <!-- Center media -->
        <div class="grid gap-4 grid-cols-2 fade-in-up" data-scroll-reveal style="animation-delay: 0.3s">
          <video 
            controls 
            muted 
            loop 
            playsinline 
            class="rounded-2xl border border-white/15 bg-slate-900 object-cover h-full shadow-xl"
          >
            <source src="@/assets/images/Uruguay Feel Nature (1 min) - Instituto Nacional de Carnes (720p, h264).mp4" type="video/mp4" />
          </video>
          <video 
            controls 
            muted 
            loop 
            playsinline 
            class="rounded-2xl border border-white/15 bg-slate-900 object-cover h-full shadow-xl"
          >
            <source src="@/assets/images/Sunset drone flight deep in Amazon Jungle, Bolivia - Joshua Turner (1080p, h264).mp4" type="video/mp4" />
          </video>
        </div>

        <!-- Right info -->
        <article class="rounded-[32px] border border-white/15 bg-gradient-to-br from-orange-900/40 to-orange-950/60 p-8 backdrop-blur-sm flex flex-col justify-center fade-in-up" data-scroll-reveal style="animation-delay: 0.4s">
          <p class="text-xs uppercase tracking-[0.35em] text-orange-300 font-bold">Best Time</p>
          <h3 class="mt-4 text-3xl font-black text-white">Seasonal Perfection</h3>
          <p class="mt-4 text-white/80">Visit during dry seasons (June-September or December-February) for optimal conditions and unforgettable adventures.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- ======================== PRACTICAL INFORMATION ======================== -->
  <section class="page-shell py-20 px-4 text-slate-900">
    <div class="mx-auto max-w-7xl">
      <div class="text-center mb-12 fade-in-up" data-scroll-reveal>
        <h2 class="text-4xl md:text-5xl font-black">Plan Your Northern Adventure</h2>
        <p class="mt-4 text-lg text-slate-600 max-w-2xl mx-auto">Everything you need to know for an unforgettable visit to Rwanda's most spectacular province.</p>
      </div>

      <div class="grid gap-6 md:grid-cols-3 mb-12">
        <article class="rounded-[24px] border border-emerald-200 bg-white p-8 shadow-lg hover:shadow-xl transition-all duration-300">
          <p class="text-sm uppercase tracking-[0.35em] text-red-600 font-bold">Elevation</p>
          <h3 class="mt-3 text-3xl font-black text-slate-900">2,000m+</h3>
          <p class="mt-3 text-slate-600">High altitude mountains with cool temperatures and unique ecosystems.</p>
        </article>

        <article class="rounded-[24px] border border-emerald-200 bg-white p-8 shadow-lg hover:shadow-xl transition-all duration-300">
          <p class="text-sm uppercase tracking-[0.35em] text-orange-600 font-bold">Duration</p>
          <h3 class="mt-3 text-3xl font-black text-slate-900">3-7 Days</h3>
          <p class="mt-3 text-slate-600">Recommended minimum for comprehensive highland exploration.</p>
        </article>

        <article class="rounded-[24px] border border-emerald-200 bg-white p-8 shadow-lg hover:shadow-xl transition-all duration-300">
          <p class="text-sm uppercase tracking-[0.35em] text-yellow-600 font-bold">Best Season</p>
          <h3 class="mt-3 text-3xl font-black text-slate-900">Jun-Sep</h3>
          <p class="mt-3 text-slate-600">Dry season offers clearest skies and best wildlife viewing.</p>
        </article>
      </div>

      <!-- Highlights grid -->
      <div class="grid gap-6 md:grid-cols-2">
        <article class="rounded-[24px] border border-slate-200 bg-white p-8 shadow-lg">
          <h3 class="text-2xl font-bold text-slate-900 mb-4">What to Experience</h3>
          <ul class="space-y-3 text-slate-600">
            <li class="flex gap-3">
              <span class="text-red-500 font-black">✓</span> Mountain gorilla trekking
            </li>
            <li class="flex gap-3">
              <span class="text-orange-500 font-black">✓</span> Volcanic crater lake hiking
            </li>
            <li class="flex gap-3">
              <span class="text-yellow-500 font-black">✓</span> Golden monkey encounters
            </li>
            <li class="flex gap-3">
              <span class="text-red-500 font-black">✓</span> Premium mountain lodges
            </li>
          </ul>
        </article>

        <article class="rounded-[24px] border border-slate-200 bg-white p-8 shadow-lg">
          <h3 class="text-2xl font-bold text-slate-900 mb-4">Key Information</h3>
          <ul class="space-y-3 text-slate-600">
            <li><strong>Main Town:</strong> Ruhengeri</li>
            <li><strong>Main Attraction:</strong> Volcanoes National Park</li>
            <li><strong>Distance from Kigali:</strong> 120 km (2-3 hours)</li>
            <li><strong>Permit Required:</strong> Yes, gorilla trekking permit</li>
          </ul>
        </article>
      </div>
    </div>
  </section>

  <style scoped>
    @keyframes fadeInUp {
      from {
        opacity: 0;
        transform: translateY(30px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .fade-in-up {
      animation: fadeInUp 0.8s ease-out forwards;
    }
  </style>
</template>

<script setup>
// Northern Province component
</script>
