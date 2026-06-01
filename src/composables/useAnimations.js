import { onMounted, ref } from 'vue'

export const useScrollReveal = (threshold = 0.1) => {
  const elements = ref([])
  
  onMounted(() => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate-reveal')
          observer.unobserve(entry.target)
        }
      })
    }, { threshold })
    
    document.querySelectorAll('[data-scroll-reveal]').forEach(el => {
      observer.observe(el)
    })
  })
}

export const useParallax = (strength = 0.5) => {
  const offset = ref(0)
  
  onMounted(() => {
    const handleScroll = () => {
      offset.value = window.scrollY * strength
    }
    
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  })
  
  return { offset }
}

export const useCounterAnimation = (endValue, duration = 2000) => {
  const count = ref(0)
  
  onMounted(() => {
    let startTime = null
    
    const animate = (currentTime) => {
      if (!startTime) startTime = currentTime
      const elapsed = currentTime - startTime
      const progress = Math.min(elapsed / duration, 1)
      
      count.value = Math.floor(endValue * progress)
      
      if (progress < 1) {
        requestAnimationFrame(animate)
      }
    }
    
    requestAnimationFrame(animate)
  })
  
  return { count }
}

export const useLazyLoad = () => {
  onMounted(() => {
    const images = document.querySelectorAll('img[data-lazy]')
    
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target
          img.src = img.dataset.lazy
          img.classList.remove('opacity-0')
          img.classList.add('opacity-100', 'transition', 'duration-500')
          observer.unobserve(img)
        }
      })
    })
    
    images.forEach(img => observer.observe(img))
  })
}
