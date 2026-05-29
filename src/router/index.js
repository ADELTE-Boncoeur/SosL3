import { createRouter, createWebHistory } from 'vue-router'

import Home from "../components/Home.vue"
import About from "../components/views/about.vue"
import Gallery from "../components/views/Gallery.vue"
import Destinations from "../components/views/Destinations.vue"
import Maps from "../components/views/Maps.vue"
import Contact from "../components/views/Contact.vue"
import Login from "../components/views/Login.vue"
import SignUp from "../components/views/SignUp.vue"
import KigaliCity from "../components/views/province/KigaliCity.vue"
import SouthernProvince from "../components/views/province/SouthernProvince.vue"
import WesternProvince from "../components/views/province/WesternProvince.vue"
import NorthernProvince from "../components/views/province/NorthernProvince.vue"
import EasternProvince from "../components/views/province/EasternProvince.vue"

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/gallery',
    name: 'Gallery',
    component: Gallery
  },
  {
    path: '/destinations',
    name: 'Destinations',
    component: Destinations
  },
  {
    path: '/destinations/kigali-city',
    name: 'KigaliCity',
    component: KigaliCity
  },
  {
    path: '/destinations/southern-province',
    name: 'SouthernProvince',
    component: SouthernProvince
  },
  {
    path: '/destinations/western-province',
    name: 'WesternProvince',
    component: WesternProvince
  },
  {
    path: '/destinations/northern-province',
    name: 'NorthernProvince',
    component: NorthernProvince
  },
  {
    path: '/destinations/eastern-province',
    name: 'EasternProvince',
    component: EasternProvince
  },
  {
    path: '/maps',
    name: 'Maps',
    component: Maps
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

/* ================= ADDITION (DO NOT REMOVE ANYTHING ABOVE) ================= */

// Scroll to top on route change
router.afterEach(() => {
  window.scrollTo(0, 0)
})

export default router