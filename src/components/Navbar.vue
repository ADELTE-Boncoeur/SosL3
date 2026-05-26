<script setup>
import logo from '../assets/sos-logo.jpg'
</script>

<template>
<nav class="fixed top-0 left-0 w-full z-50 bg-white/95 backdrop-blur-sm border-b border-slate-200 text-slate-900">
  <div class="max-w-6xl mx-auto flex justify-between items-center px-6 py-4">
    <div class="flex items-center gap-3">
      <img :src="logo" class="w-11 h-11 rounded-full border border-slate-300 shadow-sm" />
      <h1 class="text-xl md:text-2xl font-bold">SOS Schoolaa</h1>
    </div>

    <div class="hidden md:flex gap-6 text-sm font-medium">
      <a href="#home" class="hover:text-sky-600 transition">Home</a>
      <a href="#about" class="hover:text-sky-600 transition">About</a>
      <a href="#gallery" class="hover:text-sky-600 transition">Gallery</a>
      <a href="#teachers" class="hover:text-sky-600 transition">Teachers</a>
      <a href="#contact" class="hover:text-sky-600 transition">Contact</a>
    </div>
  </div>
</nav>
</template>