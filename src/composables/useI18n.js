import { ref } from 'vue'

const availableLocales = [
  { code: 'en', label: 'English' },
  { code: 'rw', label: 'Kinyarwanda' }
]

const savedLocale = typeof localStorage !== 'undefined'
  ? localStorage.getItem('app-locale') || 'en'
  : 'en'

const locale = ref(
  availableLocales.some(lang => lang.code === savedLocale)
    ? savedLocale
    : 'en'
)

const messages = {
  en: {
    logoTitle: 'Rwanda Travel',
    logoTagline: 'Discover simple, beautiful journeys',
    home: 'Home',
    about: 'About',
    gallery: 'Gallery',
    contact: 'Contact Us',
    destinations: 'Destinations',
    kgl: 'Kigali City',
    southern: 'Southern',
    western: 'Western',
    northern: 'Northern',
    eastern: 'Eastern'
  },
  rw: {
    logoTitle: 'Rwanda Travel',
    logoTagline: 'Tembera mu buryo bworoshye, bwiza',
    home: 'Ahabanza',
    about: 'Ibyerekeye',
    gallery: 'Inzu y\'amafoto',
    contact: 'Vuga Natwe',
    destinations: 'Aho gusura',
    kgl: 'Umujyi wa Kigali',
    southern: 'Amajyepfo',
    western: 'Uburengerazuba',
    northern: 'Amajyaruguru',
    eastern: 'Iburasirazuba'
  }
}

const setLocale = (newLocale) => {
  if (!availableLocales.some(lang => lang.code === newLocale)) return
  locale.value = newLocale
  if (typeof localStorage !== 'undefined') {
    localStorage.setItem('app-locale', newLocale)
  }
}

const t = (key) => {
  return messages[locale.value]?.[key] ?? key
}

export function useI18n() {
  return {
    locale,
    availableLocales,
    t,
    setLocale
  }
}
