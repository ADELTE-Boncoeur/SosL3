<script setup>
//import Home from './components/Home.vue';
import Navbar from './components/Navbar.vue';
import Footer from './components/views/footer.vue';
import { RouterView } from 'vue-router';
</script>
<template>
  <Navbar />
  <router-view /> 
  <Footer />
  <!-- <Home /> -->
</template>