<template>
  <section class="page-shell py-12 text-slate-800">
    <div class="mx-auto grid max-w-6xl gap-8 px-4 md:grid-cols-[0.9fr_1.1fr] md:px-8">
      <article class="page-card p-8">
        <p class="text-sm uppercase tracking-[0.35em] text-emerald-600">Contact</p>
        <h1 class="mt-4 text-4xl font-black text-emerald-800">Reach us easily</h1>
        <p class="mt-4 text-slate-600">Whether you need route help, travel inspiration, or booking support, we are here to answer your questions.</p>

        <div class="mt-6 space-y-4">
          <div class="rounded-2xl bg-emerald-50 p-4">📞 +250 722 635 461</div>
          <div class="rounded-2xl bg-amber-50 p-4">✉️ info@rwandatravel.example</div>
          <div class="rounded-2xl bg-sky-50 p-4">📍 Kigali, Rwanda</div>
        </div>
      </article>

      <article class="page-card p-8">
        <h2 class="text-2xl font-bold text-emerald-800">Send a quick message</h2>
        <form class="mt-6 space-y-4">
          <input class="w-full rounded-2xl border border-emerald-100 bg-emerald-50 px-4 py-3 outline-none ring-0" type="text" placeholder="Your name" />
          <input class="w-full rounded-2xl border border-emerald-100 bg-emerald-50 px-4 py-3 outline-none ring-0" type="email" placeholder="Your email" />
          <textarea class="min-h-32 w-full rounded-2xl border border-emerald-100 bg-emerald-50 px-4 py-3 outline-none ring-0" placeholder="Tell us how we can help"></textarea>
          <button class="rounded-full bg-emerald-700 px-5 py-3 text-sm font-bold text-white shadow-lg transition hover:bg-emerald-800">Send message</button>
        </form>
      </article>
    </div>
  </section>
</template>