<template>
  <section class="relative min-h-screen overflow-hidden text-white">

    <!-- ================= BACKGROUND IMAGE ================= -->
    <div class="absolute inset-0 bg-[url('src/assets/images/background2.jpg')] bg-cover bg-center scale-110"></div>

    <!-- ================= RWANDA COLOR GRADIENT OVERLAY ================= -->
    <div class="absolute inset-0 bg-gradient-to-r from-green-900/90 via-yellow-600/30 to-blue-900/90"></div>

    <!-- ================= HERO ================= -->
    <div class="relative z-10 flex flex-col items-center justify-center min-h-screen text-center px-6">

      <p class="uppercase tracking-[0.4em] text-white/70 text-sm">
        Discover Rwanda
      </p>

      <h1 class="text-5xl md:text-7xl font-extrabold mt-4 leading-tight">
        TEMBERA RWANDA
      </h1>

      <p class="mt-6 max-w-2xl text-lg text-white/90">
        Explore breathtaking landscapes, rich culture, wildlife, and unforgettable experiences across Rwanda.
      </p>

      <div class="mt-10 flex gap-4">
        <button class="px-8 py-3 bg-green-500 hover:bg-green-600 rounded-full font-bold transition">
          Explore Now
        </button>

        <button class="px-8 py-3 border border-white/40 hover:bg-white/10 rounded-full transition">
          View Destinations
        </button>
      </div>

    </div>

    <!-- ================= SCROLL INDICATOR ================= -->
    <div class="absolute bottom-6 left-1/2 -translate-x-1/2 animate-bounce">
      <div class="w-6 h-10 border-2 border-white rounded-full flex justify-center">
        <div class="w-1 h-2 bg-white mt-2 rounded-full"></div>
      </div>
    </div>

  </section>

  <!-- ================= STATS SECTION ================= -->
  <section class="bg-black text-white py-20 px-6">

    <div class="max-w-6xl mx-auto grid md:grid-cols-4 gap-6 text-center">

      <div class="p-6 rounded-2xl bg-white/10 border border-white/10">
        <h2 class="text-3xl font-bold text-green-400">50+</h2>
        <p class="text-white/70 mt-2">Destinations</p>
      </div>

      <div class="p-6 rounded-2xl bg-white/10 border border-white/10">
        <h2 class="text-3xl font-bold text-yellow-400">100K+</h2>
        <p class="text-white/70 mt-2">Tourists Guided</p>
      </div>

      <div class="p-6 rounded-2xl bg-white/10 border border-white/10">
        <h2 class="text-3xl font-bold text-blue-400">20+</h2>
        <p class="text-white/70 mt-2">Cultural Sites</p>
      </div>

      <div class="p-6 rounded-2xl bg-white/10 border border-white/10">
        <h2 class="text-3xl font-bold text-emerald-400">24/7</h2>
        <p class="text-white/70 mt-2">Support</p>
      </div>

    </div>

  </section>

  <!-- ================= ABOUT SECTION ================= -->
  <section class="bg-[linear-gradient(180deg,#020617_0%,#052e16_45%,#111827_100%)] py-24 px-6 text-white">
    <div class="mx-auto max-w-6xl text-center">
      <p class="text-sm uppercase tracking-[0.35em] text-emerald-300">Why Rwanda</p>
      <h2 class="mt-3 text-4xl font-bold md:text-5xl">A premium travel experience, beautifully presented</h2>
      <p class="mx-auto mt-4 max-w-3xl text-white/75">From serene landscapes to lively city culture, Rwanda offers a rare mix of elegance, nature, and adventure for every traveler.</p>
    </div>

    <div class="mx-auto mt-16 grid max-w-6xl gap-6 md:grid-cols-3">
      <article class="rounded-3xl border border-white/10 bg-white/8 p-6 shadow-2xl shadow-black/20 transition hover:-translate-y-1">
        <h3 class="text-xl font-bold text-emerald-300">Nature</h3>
        <p class="mt-3 text-white/75">Volcanoes, lakes, and rolling hills that make Rwanda feel cinematic and unforgettable.</p>
      </article>
      <article class="rounded-3xl border border-white/10 bg-white/8 p-6 shadow-2xl shadow-black/20 transition hover:-translate-y-1">
        <h3 class="text-xl font-bold text-yellow-300">Culture</h3>
        <p class="mt-3 text-white/75">Warm hospitality, traditions, and local stories that bring every journey to life.</p>
      </article>
      <article class="rounded-3xl border border-white/10 bg-white/8 p-6 shadow-2xl shadow-black/20 transition hover:-translate-y-1">
        <h3 class="text-xl font-bold text-sky-300">Adventure</h3>
        <p class="mt-3 text-white/75">Unforgettable nature trails, safaris, and scenic routes crafted for curious explorers.</p>
      </article>
    </div>
  </section>

  <!-- ================= CTA SECTION ================= -->
  <section class="py-24 text-center bg-black text-white">

    <h2 class="text-4xl font-bold">
      Ready to Experience Rwanda?
    </h2>

    <p class="mt-4 text-white/70">
      Start your journey today and explore the land of a thousand hills.
    </p>

    <button class="mt-8 px-10 py-3 bg-green-500 hover:bg-green-600 rounded-full font-bold transition">
      Start Exploring
    </button>

  </section>

</template>