<template>
  <footer class="relative bg-gradient-to-br from-slate-950 via-emerald-950/50 to-slate-950 text-white px-4 md:px-8 py-16 mt-10 border-t border-emerald-900/30">

    <div class="absolute inset-0 pointer-events-none overflow-hidden">
      <div class="absolute top-20 right-10 w-72 h-72 bg-emerald-500/5 rounded-full blur-3xl opacity-10"></div>
      <div class="absolute bottom-20 left-10 w-96 h-96 bg-cyan-500/5 rounded-full blur-3xl opacity-10"></div>
    </div>

    <div class="relative z-10 max-w-7xl mx-auto">

      <div class="grid gap-8 md:gap-12 lg:grid-cols-[1.2fr_1fr_1fr_1.2fr] mb-12">

        <!-- Brand -->
        <div class="fade-in-up">
          <h3 class="text-2xl font-black bg-gradient-to-r from-emerald-300 to-cyan-300 bg-clip-text text-transparent mb-4 tracking-tight">
            TEMBERA URWANDA
          </h3>

          <p class="text-sm text-emerald-100/80 leading-relaxed">
            Rwanda's premier digital tourism ecosystem.
          </p>
        </div>

        <!-- Quick Links -->
        <div class="fade-in-up" style="animation-delay:0.1s">
          <h3 class="text-lg font-black uppercase tracking-[0.2em] text-emerald-300 mb-6">
            Quick Links
          </h3>

          <ul class="space-y-3 text-sm">
            <li><RouterLink to="/">Home</RouterLink></li>
            <li><RouterLink to="/about">About</RouterLink></li>
            <li><RouterLink to="/gallery">Gallery</RouterLink></li>
            <li><RouterLink to="/destinations">Destinations</RouterLink></li>
          </ul>
        </div>

        <!-- Explore -->
        <div class="fade-in-up" style="animation-delay:0.2s">
          <h3 class="text-lg font-black uppercase tracking-[0.2em] text-cyan-300 mb-6">
            Explore
          </h3>

          <ul class="space-y-3 text-sm">
            <li><RouterLink to="/destinations/kigali-city">Kigali</RouterLink></li>
            <li><RouterLink to="/destinations/eastern-province">Eastern</RouterLink></li>
            <li><RouterLink to="/destinations/northern-province">Northern</RouterLink></li>
            <li><RouterLink to="/destinations/western-province">Western</RouterLink></li>
            <li><RouterLink to="/destinations/southern-province">Southern</RouterLink></li>
          </ul>
        </div>

        <!-- Contact -->
        <div class="fade-in-up" style="animation-delay:0.3s">
          <h3 class="text-lg font-black uppercase tracking-[0.2em] text-yellow-300 mb-6">
            Contact
          </h3>

          <p class="text-sm">Kigali, Rwanda</p>
          <p class="text-sm">+250 722 635 461</p>
        </div>

      </div>
    </div>

  </footer>
</template>

<script setup>
// nothing required
</script>

<style scoped>
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-in-up {
  animation: fadeInUp 0.6s ease-out forwards;
}
</style>