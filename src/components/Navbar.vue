<template>
  <nav class="sticky top-0 z-50 border-b border-emerald-800/20 bg-emerald-900/95 shadow-xl shadow-emerald-950/20 backdrop-blur">
    <div class="mx-auto flex w-full max-w-7xl flex-col items-center justify-center gap-4 px-4 py-3 md:flex-row md:px-6">
      <a href="#" class="flex items-center gap-3 rounded-full bg-white/10 px-3 py-2 md:mr-6">
        <img src="../assets/images/logos.png" alt="Tembera logo" class="h-12 w-12 rounded-full object-cover ring-2 ring-white/30" />
        <div>
          <h1 class="text-base font-black uppercase tracking-[0.25em] text-white md:text-lg">Rwanda Travel</h1>
          <p class="text-[11px] text-emerald-100">Discover simple, beautiful journeys</p>
        </div>
      </a>

  <ul class="flex flex-wrap items-center justify-center gap-4 text-sm font-bold uppercase tracking-widest text-white md:gap-8 lg:gap-12">

  <li>
    <RouterLink to="/" class="nav-link hover:text-yellow-300 hover:bg-green-600/50 px-3 py-2 rounded-lg transition">
      Home
    </RouterLink>
  </li>

  <li>
    <RouterLink to="/about" class="nav-link hover:text-yellow-300 hover:bg-green-600/50 px-3 py-2 rounded-lg transition">
      About
    </RouterLink>
  </li>

  <li class="relative group">
    <a href="#" class="hover:text-yellow-300 px-3 py-2 rounded-lg">
      Gallery <span>▾</span>
    </a>
    <ul class="invisible group-hover:visible opacity-0 group-hover:opacity-100 absolute bg-white text-green-900 rounded shadow w-48 top-full left-0 z-50 transition">
      <li><RouterLink to="/gallery" class="block px-4 py-2 hover:bg-green-200">Gallery Home</RouterLink></li>
      <li><a href="#" class="block px-4 py-2 hover:bg-green-200">Photos</a></li>
      <li><a href="#" class="block px-4 py-2 hover:bg-green-200">Videos</a></li>
    </ul>
  </li>

  <li class="relative group">
    <a href="#" class="hover:text-yellow-300 px-3 py-2 rounded-lg">
      Destinations <span>▾</span>
    </a>
    <ul class="invisible group-hover:visible opacity-0 group-hover:opacity-100 absolute bg-white text-green-900 rounded shadow w-52 top-full left-0 z-50 transition">
      <li><RouterLink to="/destinations/kigali-city" class="block px-4 py-2 hover:bg-green-200">Kigali</RouterLink></li>
      <li><RouterLink to="/destinations/southern-province" class="block px-4 py-2 hover:bg-green-200">South</RouterLink></li>
      <li><RouterLink to="/destinations/western-province" class="block px-4 py-2 hover:bg-green-200">West</RouterLink></li>
      <li><RouterLink to="/destinations/northern-province" class="block px-4 py-2 hover:bg-green-200">North</RouterLink></li>
      <li><RouterLink to="/destinations/eastern-province" class="block px-4 py-2 hover:bg-green-200">East</RouterLink></li>
    </ul>
  </li>

  <li>
    <RouterLink to="/maps" class="nav-link hover:text-yellow-300 hover:bg-green-600/50 px-3 py-2 rounded-lg transition">
      Maps
    </RouterLink>
  </li>

  <li>
    <RouterLink to="/contact" class="nav-link hover:text-yellow-300 hover:bg-green-600/50 px-3 py-2 rounded-lg transition">
      Contact
    </RouterLink>
  </li>

</ul>
</div>
  </nav>
</template>  
