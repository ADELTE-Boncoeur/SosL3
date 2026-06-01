<template>
  <div class="relative min-h-screen bg-[#050505] text-white font-sans overflow-x-hidden selection:bg-[#FAD201] selection:text-black">
    
    <!-- ================= STATIC IMIGONGO TEXTURE ================= -->
    <div class="fixed inset-0 pointer-events-none z-0 opacity-[0.08]">
      <div class="w-full h-full" :style="{ backgroundImage: `url(${assets.imigongo})`, backgroundSize: '150px' }"></div>
    </div>

    <!-- ================= 1. HERO ================= -->
    <section class="relative h-screen w-full flex items-center justify-center z-10 bg-black overflow-hidden">
      <TransitionGroup name="fade-zoom">
        <video v-for="(slide, index) in heroSlides" 
          :key="slide.word" v-show="activeSlideIndex === index" 
          autoplay muted loop playsinline
          class="absolute inset-0 h-full w-full object-cover brightness-[0.4] grayscale">
          <source :src="slide.video" type="video/mp4" />
        </video>
      </TransitionGroup>

      <div class="relative z-30 text-center">
        <h1 class="text-7xl md:text-[11vw] font-black tracking-tighter uppercase leading-[0.8] mb-6">
          TEMBERA<br/>
          <Transition name="word-morph" mode="out-in">
            <span :key="activeSlideIndex" 
                  class="text-outline block transition-all duration-1000"
                  :style="{ textShadow: `0 0 50px ${heroSlides[activeSlideIndex].color}` }">
              {{ heroSlides[activeSlideIndex].word }}
            </span>
          </Transition>
        </h1>
        <div class="flex items-center justify-center gap-6">
           <div class="h-[3px] w-20 bg-[#FAD201]"></div>
           <p class="text-white tracking-[1.5em] text-[10px] font-black uppercase">Land of Thousand Hills</p>
           <div class="h-[3px] w-20 bg-[#FAD201]"></div>
        </div>
      </div>
    </section>

    <!-- ================= 2. THE VISIONARY CORE ================= -->
    <section class="relative z-10 py-44 px-6 bg-white text-black overflow-hidden border-t-[20px] border-black">
      <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-24 items-center">
        <div class="relative flex justify-center items-center group/portal">
          <div @mouseenter="isHovered = true" @mouseleave="isHovered = false"
            class="imigongo-portal w-[550px] h-[550px] overflow-hidden relative shadow-[0_0_0_15px_black] bg-black">
            <Transition name="image-swap" mode="out-in">
              <div v-if="!isHovered" key="stateA" class="w-full h-full relative">
                <img :src="assets.vision" class="w-full h-full object-cover grayscale brightness-75" />
              </div>
              <div v-else key="stateB" class="w-full h-full relative">
                <img :src="assets.president" class="w-full h-full object-cover" />
              </div>
            </Transition>
          </div>
          <img :src="assets.patternCircle" class="absolute -z-10 w-[650px] h-[650px] opacity-10 animate-spin-slow" />
        </div>
        <div class="space-y-10">
          <div class="inline-block px-8 py-3 bg-black text-white font-black text-sm tracking-[0.5em] uppercase">The Visionary Core</div>
          <h2 class="text-8xl font-black tracking-tighter leading-[0.8] uppercase">State<br/><span class="text-zinc-300">Resilience</span></h2>
          <p class="text-2xl text-zinc-600 font-bold border-l-[10px] border-black pl-8">Architecting a global hub of innovation.</p>
        </div>
      </div>
    </section>

    <!-- ================= 3. IMPACT METRICS ================= -->
    <section class="py-20 bg-[#0a0a0a] border-y border-white/10">
      <div class="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-8">
        <div v-for="stat in stats" :key="stat.label" class="text-center">
          <div class="text-5xl font-black text-[#FAD201] mb-2">{{ stat.value }}</div>
          <div class="text-xs uppercase tracking-widest text-zinc-500">{{ stat.label }}</div>
        </div>
      </div>
    </section>

    <!-- ================= 4. PARTNERSHIP ECOSYSTEM ================= -->
    <section class="py-32 bg-white">
      <div class="max-w-7xl mx-auto px-6">
        <h2 class="text-5xl font-black text-black uppercase mb-20 tracking-tighter">Partnership <br/><span class="text-zinc-400">Ecosystem</span></h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-12 items-center opacity-60 grayscale hover:grayscale-0 transition-all">
          <div class="text-2xl font-black text-black border-2 border-black p-8 text-center">BK GROUP</div>
          <div class="text-2xl font-black text-black border-2 border-black p-8 text-center">RWANDAIR</div>
          <div class="text-2xl font-black text-black border-2 border-black p-8 text-center">MINICT</div>
          <div class="text-2xl font-black text-black border-2 border-black p-8 text-center">RDB</div>
        </div>
      </div>
    </section>

    <!-- ================= 5. THE SOVEREIGN PATH ================= -->
    <section class="relative z-10 py-44 px-6 bg-[#030303] text-white overflow-hidden border-b-[20px] border-black">
      <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-24 items-center">
        <div class="space-y-10 order-2 lg:order-1">
          <div class="inline-block px-8 py-3 bg-[#00A3E0] text-white font-black text-sm tracking-[0.5em] uppercase">The Sovereign Path</div>
          <h2 class="text-8xl font-black tracking-tighter leading-[0.8] uppercase">Our<br/><span class="text-[#FAD201]">History</span></h2>
          <p class="text-2xl text-zinc-400 font-bold border-l-[10px] border-[#2D6A4F] pl-8">Tracing the journey of a thousand hills.</p>
          <div class="flex gap-4 pt-4 opacity-50">
            <img :src="assets.ourhistory1" class="w-24 h-16 object-cover border border-white/10" />
            <img :src="assets.ourhistory2" class="w-24 h-16 object-cover border border-white/10" />
          </div>
        </div>
        <div class="relative flex justify-center items-center group/history order-1 lg:order-2">
          <div @mouseenter="isHistoryHovered = true" @mouseleave="isHistoryHovered = false"
            class="imigongo-portal w-[550px] h-[550px] overflow-hidden relative shadow-[0_0_0_15px_#00A3E0] bg-black">
            <Transition name="image-swap" mode="out-in">
              <div v-if="!isHistoryHovered" key="histA" class="w-full h-full relative">
                <img :src="assets.ourhistory" class="w-full h-full object-cover grayscale brightness-50" />
                <div class="absolute inset-0 flex flex-col opacity-60 mix-blend-color">
                  <div class="flex-1 bg-[#00A3E0]"></div>
                  <div class="h-1/3 bg-[#FAD201]"></div>
                  <div class="h-1/3 bg-[#2D6A4F]"></div>
                </div>
              </div>
              <div v-else key="histB" class="w-full h-full relative">
                <img :src="assets.ourhistory1" class="w-full h-full object-cover grayscale-0" />
              </div>
            </Transition>
          </div>
        </div>
      </div>
    </section>

    <!-- ================= 6. THE LIVING EARTH ================= -->
    <section class="relative z-10 py-44 px-6 bg-[#0a0a0a] text-white border-b-[20px] border-black">
      <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-24 items-center">
        <div class="imigongo-portal w-[550px] h-[550px] overflow-hidden relative shadow-[0_0_0_15px_#2D6A4F] bg-zinc-900">
           <img :src="assets.teaPlantation" class="w-full h-full object-cover grayscale" />
           <video autoplay muted loop playsinline class="absolute inset-0 w-full h-full object-cover mix-blend-overlay opacity-50">
              <source :src="assets.waterfallVideo" type="video/mp4" />
           </video>
        </div>
        <div class="space-y-10">
          <div class="inline-block px-8 py-3 bg-[#2D6A4F] text-white font-black text-sm tracking-[0.5em] uppercase">The Living Earth</div>
          <h2 class="text-8xl font-black tracking-tighter leading-[0.8] uppercase">Deep<br/><span class="text-zinc-400">Nature</span></h2>
          <p class="text-2xl text-zinc-600 font-bold border-l-[10px] border-[#2D6A4F] pl-8">Protected horizons, untamed and pure.</p>
        </div>
      </div>
    </section>

    <!-- ================= 7. THE CULTURAL PULSE ================= -->
    <section class="relative z-10 py-44 px-6 bg-[#0a0a0a] text-white">
      <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-24 items-center">
        <div class="space-y-10">
          <div class="inline-block px-8 py-3 bg-[#FAD201] text-black font-black text-sm tracking-[0.5em] uppercase">The Cultural Pulse</div>
          <h2 class="text-8xl font-black tracking-tighter leading-[0.8] uppercase">Human<br/><span class="text-[#FAD201]">Vibrancy</span></h2>
          <p class="text-2xl text-zinc-400 font-bold border-l-[10px] border-[#FAD201] pl-8">The heartbeat of Rwandan tradition.</p>
        </div>
        <div class="imigongo-portal w-[550px] h-[550px] overflow-hidden relative shadow-[0_0_0_15px_#FAD201] bg-black">
          <img :src="assets.rwandans" class="w-full h-full object-cover grayscale-0" />
        </div>
      </div>
    </section>

    <!-- ================= FOOTER: WHAT MAKES US DIFFERENT & SUBSCRIBE ================= -->
    <footer class="bg-black pt-24 pb-12 border-t-[20px] border-[#00A3E0]">
      <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-2 gap-20">
        
        <!-- Dropdown Accordion -->
        <div class="space-y-4">
          <h3 class="text-3xl font-black uppercase mb-8">What Makes Us Different</h3>
          <div v-for="(item, index) in differences" :key="index" class="border border-white/10">
            <button @click="activeDiff = activeDiff === index ? null : index" 
                    class="w-full p-6 flex justify-between items-center bg-white/5 hover:bg-white/10 transition-all">
              <span class="font-bold text-lg">{{ item.title }}</span>
              <span class="text-[#FAD201] text-2xl">{{ activeDiff === index ? '−' : '+' }}</span>
            </button>
            <div v-if="activeDiff === index" class="p-6 bg-[#0a0a0a] border-t border-white/5 text-zinc-400 leading-relaxed">
              {{ item.desc }}
            </div>
          </div>
        </div>

        <!-- Subscribe Form -->
        <div class="bg-[#2D6A4F] p-12 relative overflow-hidden">
          <h3 class="text-4xl font-black uppercase mb-6">Stay Connected</h3>
          <p class="mb-8 opacity-80">Join the movement of the thousand hills. Get updates on our digital evolution.</p>
          <form class="space-y-4" @submit.prevent>
            <input type="email" placeholder="YOUR EMAIL ADDRESS" 
                   class="w-full p-4 bg-black/30 border-2 border-white/20 outline-none focus:border-[#FAD201] transition-all placeholder:text-white/30" />
            <button class="w-full bg-[#FAD201] text-black font-black py-4 uppercase hover:bg-white transition-all">Subscribe</button>
          </form>
          <!-- Rwandan flag accent bars -->
          <div class="absolute bottom-0 left-0 w-full h-3 flex">
            <div class="flex-1 bg-[#00A3E0]"></div>
            <div class="flex-1 bg-[#FAD201]"></div>
            <div class="flex-1 bg-[#2D6A4F]"></div>
          </div>
        </div>
      </div>
      <div class="text-center mt-20 text-zinc-600 text-sm uppercase tracking-[0.2em]">© 2026 Tembera Rwanda. All Rights Reserved.</div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const assets = {
  president: new URL('@/assets/images/president.jpg', import.meta.url).href,
  vision: new URL('@/assets/images/vision.jpg', import.meta.url).href,
  teaPlantation: new URL('@/assets/images/tea plantation.jpg', import.meta.url).href,
  rwandans: new URL('@/assets/images/rwandans.jpg', import.meta.url).href,
  ourhistory: new URL('@/assets/images/ourhistory.jpg', import.meta.url).href,
  ourhistory1: new URL('@/assets/images/ourhistory1.jpg', import.meta.url).href,
  ourhistory2: new URL('@/assets/images/ourhistory2.jpg', import.meta.url).href,
  imigongo: new URL('@/assets/images/image_8832a6.png', import.meta.url).href,
  patternCircle: new URL('@/assets/images/image_414999.png', import.meta.url).href,
  rwandaVideo: new URL('@/assets/images/rwanda.mp4', import.meta.url).href,
  waterfallVideo: new URL('@/assets/images/waterfall.mp4', import.meta.url).href,
  urugaryVideo: new URL('@/assets/images/urugary.mp4', import.meta.url).href,
  sunsetVideo: new URL('@/assets/images/sunset.mp4', import.meta.url).href
}

const activeSlideIndex = ref(0)
const isHovered = ref(false)
const isHistoryHovered = ref(false)
const activeDiff = ref(null)

const heroSlides = [
  { word: 'URWANDA', video: assets.rwandaVideo, color: '#00A3E0' },
  { word: 'HERITAGE', video: assets.sunsetVideo, color: '#FAD201' },
  { word: 'FUTURE', video: assets.urugaryVideo, color: '#2D6A4F' }
]

const stats = [
  { value: '95%', label: 'Connectivity' },
  { value: '8%', label: 'Annual Growth' },
  { value: '1st', label: 'Transparency' },
  { value: '24h', label: 'Business Setup' }
]

const differences = [
  { title: "Digital Resilience", desc: "Our infrastructure is built for high-uptime, high-capacity traffic across the entire region." },
  { title: "Cultural Integration", desc: "Every line of code respects the heritage of Imigongo and traditional patterns, merging tech with soul." },
  { title: "Transparency First", desc: "We leverage secure blockchain and efficient admin dashboards to ensure 0% corruption in transactions." }
]

onMounted(() => {
  setInterval(() => { activeSlideIndex.value = (activeSlideIndex.value + 1) % heroSlides.length }, 6000)
})
</script>

<style scoped>
.text-outline { -webkit-text-stroke: 2px white; color: transparent; }
.imigongo-portal {
  clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
  transition: all 1s cubic-bezier(0.16, 1, 0.3, 1);
}
.imigongo-portal:hover { clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%); }
.word-morph-enter-active, .word-morph-leave-active { transition: all 0.8s ease; }
.word-morph-enter-from { opacity: 0; transform: translateY(20px); filter: blur(10px); }
.fade-zoom-enter-active { animation: zoom 6s forwards; }
@keyframes zoom { from { opacity: 0; transform: scale(1.1); } to { opacity: 1; transform: scale(1); } }
.animate-spin-slow { animation: spin 45s linear infinite; }
@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
</style>