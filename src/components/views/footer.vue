<template>
  <footer class="bg-green-800 text-white px-8 py-10 mt-10">
    <!-- This is about footer -->
    <div class="flex flex-wrap justify-between gap-8">
      <div>
        <h3 class="text-yellow-300 font-bold text-lg mb-3">TEMBERA URWANDA</h3> 
        <p class="text-sm text-green-200">Discover the beauty of the land of a Thousand hills</p>
      </div>

      <!-- Quick links -->
       <div>
        <h3 class="text-yellow-300 font-bold text-lg mb-3">Quick links</h3>
        <ul class="space-y-2 text-sm">
          <li><RouterLink to="/home" class="hover:text-yellow-300">Home</RouterLink></li>
          <li><RouterLink to="/about" class="hover:text-yellow-300">About Us</RouterLink></li>
          <li><RouterLink to="/contact" class="hover:text-yellow-300">Contact</RouterLink></li>
        </ul>
      </div>

      <!-- This is destinations -->
     <div>
        <h3 class="text-yellow-300 font-bold text-lg mb-3">Destinations</h3>
        <ul class="space-y-2 text-sm">
          <li><RouterLink to="/" class="hover:text-yellow-300">Kigali city</RouterLink></li>
          <li><RouterLink to="/" class="hover:text-yellow-300">Eastern</RouterLink></li>
          <li><RouterLink to="/" class="hover:text-yellow-300">North</RouterLink></li>
          <li><RouterLink to="/" class="hover:text-yellow-300">Western</RouterLink></li>
          <li><RouterLink to="/" class="hover:text-yellow-300">South</RouterLink></li>
        </ul>
      </div> 
     <div>
        <h3 class="text-yellow-300 font-bold text-lg mb-3">Follow Us</h3>
        <ul class="space-y-2 text-green-300">
            <li>mloaze778@gmail.mab</li>
            <li>+250 788 123 456</li>
            <li>Rwanda, Kigali</li>
        </ul>
    </div>
    </div>
    <!-- Social media links-->
     <div class="mt-8 border-t border-green-700 pt-4 text-center text-sm text-green-300">
       <p class="text-center">©2026 Tembera Urwanda. All rights reserved.</p>
    </div>
  </footer>
</template>
