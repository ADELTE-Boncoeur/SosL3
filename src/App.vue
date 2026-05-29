<script setup>
import Navbar from './components/Navbar.vue'
import Footer from './components/views/footer.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <Navbar />

  <!-- MAIN CONTENT AREA -->
  <router-view />

  <Footer />
</template>