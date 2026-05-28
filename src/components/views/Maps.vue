<template>
  <div class="maps-container">
    <h1>Maps & Directions</h1>

    <div class="maps-content">
      <div class="map-section">
        <h2>Find Your Destination</h2>
        <div class="search-box">
          <input 
            v-model="searchLocation" 
            type="text" 
            placeholder="Enter location..."
            @keyup.enter="searchLocation"
          />
          <button @click="searchLocation">Search</button>
        </div>

        <div class="map-placeholder">
          <iframe 
            width="100%" 
            height="400" 
            frameborder="0" 
            style="border:0" 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.019!2d-122.419!3d37.775!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064e2d47e59:0x1234567890!2sDestination!5e0!3m2!1sen!2sus!4v1234567890123"
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
          </iframe>
        </div>
      </div>

      <div class="directions-section">
        <h2>Popular Routes</h2>
        <div class="routes-list">
          <div v-for="route in routes" :key="route.id" class="route-item">
            <div class="route-info">
              <h3>{{ route.from }} → {{ route.to }}</h3>
              <p>Distance: {{ route.distance }}</p>
              <p>Duration: {{ route.duration }}</p>
            </div>
            <button class="direction-btn">Get Directions</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

