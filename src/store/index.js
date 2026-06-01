import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

const favoritesKey = 'tembera-favorites'
const recentKey = 'tembera-recently'
const bookingKey = 'tembera-bookings'
const preferenceKey = 'tembera-preferences'

function loadJson(key, fallback) {
  try {
    return JSON.parse(localStorage.getItem(key) || JSON.stringify(fallback))
  } catch {
    return fallback
  }
}

export const useTourismStore = defineStore('tourism', () => {
  const favorites = ref(loadJson(favoritesKey, []))
  const recentlyViewed = ref(loadJson(recentKey, []))
  const bookings = ref(loadJson(bookingKey, []))
  const preferences = ref(loadJson(preferenceKey, { language: 'en', theme: 'luxury' }))
  const searchQuery = ref('')
  const activeProvince = ref('All Provinces')

  const destinations = ref([
    {
      id: 'kigali',
      name: 'Kigali City',
      province: 'Kigali',
      category: 'City',
      rating: 4.9,
      price: '$$ - $$$',
      visitors: 19300,
      description: 'A modern innovation hub with museums, nightlife, and urban luxury experiences.',
      image: new URL('../assets/images/background1.jpg', import.meta.url).href,
      tags: ['Nightlife', 'Culture', 'City']
    },
    {
      id: 'eastern',
      name: 'Eastern Province',
      province: 'Eastern Province',
      category: 'Safari',
      rating: 4.8,
      price: '$$ - $$$',
      visitors: 14250,
      description: 'Wildlife safaris, conservation reserves and wide plains rich in open country.',
      image: new URL('../assets/images/background2.jpg', import.meta.url).href,
      tags: ['Wildlife', 'Safari', 'Adventure']
    },
    {
      id: 'northern',
      name: 'Northern Province',
      province: 'Northern Province',
      category: 'Mountains',
      rating: 4.9,
      price: '$$$',
      visitors: 16320,
      description: 'Mountain escapes, volcano treks, and gorilla trails for premium adventure travelers.',
      image: new URL('../assets/images/background.jpg', import.meta.url).href,
      tags: ['Trekking', 'Volcanoes', 'Nature']
    },
    {
      id: 'southern',
      name: 'Southern Province',
      province: 'Southern Province',
      category: 'Culture',
      rating: 4.7,
      price: '$$ - $$$',
      visitors: 9800,
      description: 'Cultural villages, coffee landscapes, museums and immersive heritage trips.',
      image: new URL('../assets/images/background.jpg', import.meta.url).href,
      tags: ['Culture', 'Heritage', 'Nature']
    },
    {
      id: 'western',
      name: 'Western Province',
      province: 'Western Province',
      category: 'Adventure',
      rating: 4.9,
      price: '$$$',
      visitors: 17500,
      description: 'Lake Kivu, Nyungwe rainforest and volcano parks for luxury adventure stays.',
      image: new URL('../assets/images/background1.jpg', import.meta.url).href,
      tags: ['Lakes', 'Forest', 'Adventure']
    }
  ])

  const hotels = ref([
    {
      id: 'royal-plaza',
      name: 'Royal Kigali Plaza',
      destination: 'Kigali City',
      stars: 5,
      rating: 4.9,
      price: 320,
      rooms: ['Deluxe Suite', 'Garden View', 'Sky Terrace'],
      amenities: ['Spa', 'Pool', 'Gym', 'Airport transfer'],
      image: new URL('../assets/images/background2.jpg', import.meta.url).href,
      available: true
    },
    {
      id: 'akagera-lodge',
      name: 'Akagera Safari Lodge',
      destination: 'Eastern Province',
      stars: 4,
      rating: 4.8,
      price: 240,
      rooms: ['Safari Tent', 'Family Cottage', 'Executive Room'],
      amenities: ['Safari drives', 'Wildlife meals', 'Pool'],
      image: new URL('../assets/images/background.jpg', import.meta.url).href,
      available: true
    },
    {
      id: 'volcano-view',
      name: 'Volcano View Retreat',
      destination: 'Western Province',
      stars: 5,
      rating: 4.9,
      price: 390,
      rooms: ['Presidential Suite', 'Lake View', 'Forest Suite'],
      amenities: ['Private guide', 'Yoga deck', 'Infinity pool'],
      image: new URL('../assets/images/background1.jpg', import.meta.url).href,
      available: false
    }
  ])

  const restaurants = ref([
    {
      id: 'kigali-rooftop',
      name: 'Kigali Rooftop Kitchen',
      cuisine: 'Rwandan Fusion',
      rating: 4.8,
      priceRange: '$$ - $$$',
      description: 'Fine dining with skyline views and farm-to-table cuisine.',
      image: new URL('../assets/images/background.jpg', import.meta.url).href
    },
    {
      id: 'lake-kivu-bistro',
      name: 'Lake Kivu Bistro',
      cuisine: 'Seafood & African',
      rating: 4.7,
      priceRange: '$$ - $$$',
      description: 'Relaxed waterfront dining with local seafood specialties.',
      image: new URL('../assets/images/background2.jpg', import.meta.url).href
    }
  ])

  const events = ref([
    {
      id: 'culture-festival',
      title: 'Rwanda Culture Festival',
      province: 'Southern Province',
      category: 'Cultural Events',
      date: '2026-09-15',
      countdown: '45 days',
      description: 'A celebration of traditional music, dance and art from across the country.',
      attendees: 3520
    },
    {
      id: 'travel-summit',
      title: 'East Africa Tourism Summit',
      province: 'Kigali',
      category: 'Conference',
      date: '2026-08-10',
      countdown: '20 days',
      description: 'A business travel event for tourism operators, analysts and travel media.',
      attendees: 820
    }
  ])

  const news = ref([
    {
      id: 'rwanda-growth',
      title: 'Rwanda tourism reaches new growth milestones',
      category: 'Industry News',
      summary: 'Visitor spending and international arrivals are on track for a record year.',
      date: '2026-05-18'
    },
    {
      id: 'new-luxury-lodges',
      title: 'New luxury lodges open near Nyungwe',
      category: 'Lodging',
      summary: 'High-end eco resorts add premium stay options for adventure travelers.',
      date: '2026-04-27'
    }
  ])

  const itineraries = ref([
    {
      id: 'gorilla-expedition',
      title: '7-Day Gorilla Expedition',
      province: 'Northern Province',
      duration: '7 days',
      cost: '$2,150'
    },
    {
      id: 'lake-kivu-retreat',
      title: 'Lake Kivu Luxury Retreat',
      province: 'Western Province',
      duration: '5 days',
      cost: '$1,480'
    }
  ])

  const compareList = ref(loadJson('tembera-compare', []))
  const travelPlans = ref(loadJson('tembera-plans', []))
  const languages = ref(['English', 'French', 'Kinyarwanda', 'Swahili'])
  const searchSuggestions = ref(['Gorilla trekking', 'Luxury lodge', 'Rwanda safari', 'City tour', 'Lake cruise'])

  const community = ref([
    {
      id: 'trailstory',
      author: 'Amina',
      title: 'Gorillas, coffee and a perfect night in Musanze',
      excerpt: 'I planned a 5-day route with the AI assistant and discovered moments I did not expect.',
      reactions: 84
    },
    {
      id: 'kigalivibe',
      author: 'James',
      title: 'Kigali city nightlife and sustainable dining',
      excerpt: 'From markets to rooftop bars, the city felt modern and welcoming.',
      reactions: 61
    }
  ])

  const weather = ref([
    { province: 'Kigali', temp: '24°C', condition: 'Sunny', wind: '12 km/h', recommendation: 'Perfect city tours today' },
    { province: 'Eastern Province', temp: '26°C', condition: 'Partly cloudy', wind: '8 km/h', recommendation: 'Great for safaris' },
    { province: 'Northern Province', temp: '18°C', condition: 'Cool mist', wind: '10 km/h', recommendation: 'Best hiking conditions' },
    { province: 'Western Province', temp: '22°C', condition: 'Rain showers', wind: '14 km/h', recommendation: 'Lake cruises remain calm' }
  ])

  function persist() {
    localStorage.setItem(favoritesKey, JSON.stringify(favorites.value))
    localStorage.setItem(recentKey, JSON.stringify(recentlyViewed.value))
    localStorage.setItem(bookingKey, JSON.stringify(bookings.value))
    localStorage.setItem(preferenceKey, JSON.stringify(preferences.value))
    localStorage.setItem('tembera-compare', JSON.stringify(compareList.value))
    localStorage.setItem('tembera-plans', JSON.stringify(travelPlans.value))
  }

  function toggleFavorite(itemId) {
    if (favorites.value.includes(itemId)) {
      favorites.value = favorites.value.filter((id) => id !== itemId)
    } else {
      favorites.value.push(itemId)
    }
    persist()
  }

  function addToCompare(itemId) {
    if (!compareList.value.includes(itemId)) {
      compareList.value.push(itemId)
      persist()
    }
  }

  function removeFromCompare(itemId) {
    compareList.value = compareList.value.filter((id) => id !== itemId)
    persist()
  }

  function saveTravelPlan(plan) {
    travelPlans.value.unshift({ id: `plan-${Date.now()}`, ...plan })
    if (travelPlans.value.length > 8) travelPlans.value.pop()
    persist()
  }

  function setLanguage(language) {
    preferences.value.language = language
    persist()
  }

  function getSearchSuggestions(query) {
    return searchSuggestions.value.filter((item) => item.toLowerCase().includes(query.toLowerCase()))
  }

  function addRecentlyViewed(item) {
    const existing = recentlyViewed.value.find((entry) => entry.id === item.id)
    if (!existing) {
      recentlyViewed.value.unshift({ ...item, visitedAt: new Date().toISOString() })
      if (recentlyViewed.value.length > 6) {
        recentlyViewed.value.pop()
      }
      persist()
    }
  }

  function createBooking(details) {
    bookings.value.unshift({ id: `bk-${Date.now()}`, ...details, status: 'Confirmed', createdAt: new Date().toISOString() })
    persist()
  }

  function updatePreferences(updates) {
    preferences.value = { ...preferences.value, ...updates }
    persist()
  }

  const filteredDestinations = computed(() => {
    const query = searchQuery.value.toLowerCase().trim()
    return destinations.value.filter((item) => {
      const matchesQuery = !query || item.name.toLowerCase().includes(query) || item.description.toLowerCase().includes(query)
      const matchesProvince = activeProvince.value === 'All Provinces' || item.province === activeProvince.value
      return matchesQuery && matchesProvince
    })
  })

  const analytics = computed(() => ({
    totalAttractions: 238,
    totalVisitors: 432000,
    totalBookings: bookings.value.length,
    monthlyGrowth: [12, 18, 22, 26, 30, 40],
    provinceRankings: [
      { province: 'Kigali', score: 98 },
      { province: 'Western Province', score: 92 },
      { province: 'Northern Province', score: 89 },
      { province: 'Eastern Province', score: 85 },
      { province: 'Southern Province', score: 78 }
    ]
  }))

  return {
    favorites,
    recentlyViewed,
    bookings,
    preferences,
    searchQuery,
    activeProvince,
    destinations,
    hotels,
    restaurants,
    events,
    news,
    community,
    weather,
    filteredDestinations,
    analytics,
    itineraries,
    compareList,
    travelPlans,
    languages,
    searchSuggestions,
    getSearchSuggestions,
    toggleFavorite,
    addToCompare,
    removeFromCompare,
    saveTravelPlan,
    setLanguage,
    addRecentlyViewed,
    createBooking,
    updatePreferences,
    persist
  }
})
