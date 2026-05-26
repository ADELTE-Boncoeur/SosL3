<script setup>
import a from '../assets/apply.jpg'
import b from '../assets/graduate.jpg'
import c from '../assets/new.jpg'
</script>

<template>
<section id="gallery" class="py-20 bg-white text-slate-900">
  <div class="max-w-6xl mx-auto px-6 text-center">
    <h2 class="text-4xl font-bold mb-10">Gallery</h2>
    <div class="grid gap-6 md:grid-cols-3">
      <img :src="a" class="card w-full h-64 object-cover rounded-3xl" />
      <img :src="b" class="card w-full h-64 object-cover rounded-3xl" />
      <img :src="c" class="card w-full h-64 object-cover rounded-3xl" />
    </div>
  </div>
</section>
</template>