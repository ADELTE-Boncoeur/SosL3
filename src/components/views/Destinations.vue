<template>
  <ul class="flex gap-6 text-white font-semibold">
    <li class="relative group cursor-pointer">
      Destination ▼
      <ul class="absolute hidden group-hover:block mt-3 bg-white text-slate-700 rounded-2xl shadow-xl w-56 overflow-hidden">
        <li class="px-5 py-4 hover:bg-emerald-50">
          Kigali
        </li>
        <li class="px-5 py-4 hover:bg-emerald-50">
          Eastern Province
        </li>
        <li class="px-5 py-4 hover:bg-emerald-50">
          Northern Province
        </li>
        <li class="px-5 py-4 hover:bg-emerald-50">
          Southern Province
        </li>
        <li class="px-5 py-4 hover:bg-emerald-50">
          Western Province
        </li>
      </ul>
    </li>
  </ul>
</template>