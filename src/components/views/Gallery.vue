<template>
  <section class="page-shell py-12 text-slate-800">
    <div class="mx-auto max-w-7xl px-4 md:px-8">
      <article class="page-card p-8 md:p-10">
        <p class="text-sm uppercase tracking-[0.35em] text-emerald-600">Gallery</p>
        <h1 class="mt-4 text-4xl font-black text-emerald-800 md:text-5xl">A simple visual journey through Rwanda</h1>
        <p class="mt-4 max-w-3xl text-slate-600">Browse a few highlights from the country’s hills, city scenes, and scenic landscapes.</p>

        <div class="mt-8 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
          <article class="overflow-hidden rounded-3xl border border-emerald-100 bg-white shadow-lg">
            <img src="/src/assets/images/background1.jpg" alt="Rwanda landscape" class="h-56 w-full object-cover" />
            <div class="p-4"><h2 class="text-xl font-bold text-emerald-800">Mountain views</h2><p class="mt-2 text-sm text-slate-600">Fresh air, green hills, and unforgettable scenery.</p></div>
          </article>
          <article class="overflow-hidden rounded-3xl border border-emerald-100 bg-white shadow-lg">
            <img src="/src/assets/images/background2.jpg" alt="Rwanda city route" class="h-56 w-full object-cover" />
            <div class="p-4"><h2 class="text-xl font-bold text-emerald-800">City energy</h2><p class="mt-2 text-sm text-slate-600">Modern streets, markets, and vibrant travel experiences.</p></div>
          </article>
          <article class="overflow-hidden rounded-3xl border border-emerald-100 bg-white shadow-lg md:col-span-2 xl:col-span-1">
            <img src="/src/assets/images/background.jpg" alt="Rwanda travel view" class="h-56 w-full object-cover" />
            <div class="p-4"><h2 class="text-xl font-bold text-emerald-800">Travel inspiration</h2><p class="mt-2 text-sm text-slate-600">A simple reminder of why Rwanda is a beautiful destination.</p></div>
          </article>
        </div>
      </article>
    </div>
  </section>
</template>