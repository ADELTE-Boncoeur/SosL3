<template>
  <section class="page-shell py-12 text-slate-800">
    <div class="mx-auto max-w-7xl px-4 md:px-8">
      <article class="page-card p-8 md:p-10">
        <p class="text-sm uppercase tracking-[0.35em] text-emerald-600">Destinations</p>
        <h1 class="mt-4 text-4xl font-black text-emerald-800 md:text-5xl">Choose your next Rwanda stop</h1>
        <p class="mt-4 max-w-3xl text-slate-600">A simple overview of Kigali and Rwanda’s major provinces, ready for your trip plan.</p>

        <div class="mt-8 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
          <RouterLink to="/destinations/kigali-city" class="rounded-3xl border border-emerald-100 bg-emerald-50 p-5 shadow-md transition hover:-translate-y-1 hover:bg-emerald-100"> <h2 class="text-xl font-bold text-emerald-800">Kigali City</h2><p class="mt-2 text-sm text-slate-600">Modern capital, museums, markets, and city experiences.</p></RouterLink>
          <RouterLink to="/destinations/eastern-province" class="rounded-3xl border border-emerald-100 bg-amber-50 p-5 shadow-md transition hover:-translate-y-1 hover:bg-amber-100"> <h2 class="text-xl font-bold text-amber-800">Eastern Province</h2><p class="mt-2 text-sm text-slate-600">Wide plains, wildlife, and open-country travel.</p></RouterLink>
          <RouterLink to="/destinations/northern-province" class="rounded-3xl border border-emerald-100 bg-sky-50 p-5 shadow-md transition hover:-translate-y-1 hover:bg-sky-100"> <h2 class="text-xl font-bold text-sky-800">Northern Province</h2><p class="mt-2 text-sm text-slate-600">Cool hills, mountain views, and peaceful nature.</p></RouterLink>
          <RouterLink to="/destinations/southern-province" class="rounded-3xl border border-emerald-100 bg-violet-50 p-5 shadow-md transition hover:-translate-y-1 hover:bg-violet-100"> <h2 class="text-xl font-bold text-violet-800">Southern Province</h2><p class="mt-2 text-sm text-slate-600">Culture, traditions, and green village landscapes.</p></RouterLink>
          <RouterLink to="/destinations/western-province" class="rounded-3xl border border-emerald-100 bg-rose-50 p-5 shadow-md transition hover:-translate-y-1 hover:bg-rose-100"> <h2 class="text-xl font-bold text-rose-800">Western Province</h2><p class="mt-2 text-sm text-slate-600">Volcanoes, forests, and thrilling mountain adventures.</p></RouterLink>
        </div>
      </article>
    </div>
  </section>
</template>