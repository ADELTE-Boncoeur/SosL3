<template>
  <div class="relative min-h-screen bg-[#050505] text-white font-sans overflow-x-hidden selection:bg-[#FAD201] selection:text-black">
    
    <!-- ================= LANGUAGE TRANSLATOR ================= -->
    <div class="fixed top-6 right-6 z-50">
      <div class="flex gap-2 bg-black/80 backdrop-blur-md border border-white/10 rounded-full p-1">
        <button
          v-for="lang in languages"
          :key="lang.code"
          @click="switchLanguage(lang.code)"
          :class="[
            'px-5 py-2 text-sm font-bold rounded-full transition-all',
            currentLang === lang.code 
              ? 'bg-[#FAD201] text-black' 
              : 'hover:bg-white/10'
          ]"
        >
          {{ lang.label }}
        </button>
      </div>
    </div>

    <!-- ================= STATIC IMIGONGO TEXTURE ================= -->
    <div class="fixed inset-0 pointer-events-none z-0 opacity-[0.08]">
      <div class="w-full h-full" :style="{ backgroundImage: `url(${assets.imigongo})`, backgroundSize: '150px' }"></div>
    </div>

    <!-- ================= 1. HERO ================= -->
    <section class="relative h-screen w-full flex items-center justify-center z-10 bg-black overflow-hidden">
      <TransitionGroup name="fade-zoom">
        <video v-for="(slide, index) in heroSlides" 
          :key="slide.wordKey" v-show="activeSlideIndex === index" 
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
              {{ t(heroSlides[activeSlideIndex].wordKey) }}
            </span>
          </Transition>
        </h1>
        <div class="flex items-center justify-center gap-6">
          <div class="h-[3px] w-20 bg-[#FAD201]"></div>
          <p class="text-white tracking-[1.5em] text-[10px] font-black uppercase">{{ t('landOfThousandHills') }}</p>
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
          <div class="inline-block px-8 py-3 bg-black text-white font-black text-sm tracking-[0.5em] uppercase">
            {{ t('theVisionaryCore') }}
          </div>
          <h2 class="text-8xl font-black tracking-tighter leading-[0.8] uppercase">
            {{ t('stateResilience') }}<br/>
            <span class="text-zinc-300">{{ t('resilience') }}</span>
          </h2>
          <p class="text-2xl text-zinc-600 font-bold border-l-[10px] border-black pl-8">
            {{ t('architectingGlobalHub') }}
          </p>
        </div>
      </div>
    </section>

    <!-- ================= 3. IMPACT METRICS ================= -->
    <section class="py-20 bg-[#0a0a0a] border-y border-white/10">
      <div class="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-8">
        <div v-for="stat in stats" :key="stat.label" class="text-center">
          <div class="text-5xl font-black text-[#FAD201] mb-2">{{ stat.value }}</div>
          <div class="text-xs uppercase tracking-widest text-zinc-500">{{ t(stat.labelKey) }}</div>
        </div>
      </div>
    </section>

    <!-- ================= 4. PARTNERSHIP ECOSYSTEM ================= -->
    <section class="py-32 bg-white">
      <div class="max-w-7xl mx-auto px-6">
        <h2 class="text-5xl font-black text-black uppercase mb-20 tracking-tighter">
          {{ t('partnershipEcosystem') }}
        </h2>
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
          <div class="inline-block px-8 py-3 bg-[#00A3E0] text-white font-black text-sm tracking-[0.5em] uppercase">
            {{ t('theSovereignPath') }}
          </div>
          <h2 class="text-8xl font-black tracking-tighter leading-[0.8] uppercase">
            {{ t('ourHistory') }}<br/>
            <span class="text-[#FAD201]">{{ t('history') }}</span>
          </h2>
          <p class="text-2xl text-zinc-400 font-bold border-l-[10px] border-[#2D6A4F] pl-8">
            {{ t('tracingJourney') }}
          </p>
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
          <div class="inline-block px-8 py-3 bg-[#2D6A4F] text-white font-black text-sm tracking-[0.5em] uppercase">
            {{ t('theLivingEarth') }}
          </div>
          <h2 class="text-8xl font-black tracking-tighter leading-[0.8] uppercase">
            {{ t('deepNature') }}<br/>
            <span class="text-zinc-400">{{ t('nature') }}</span>
          </h2>
          <p class="text-2xl text-zinc-600 font-bold border-l-[10px] border-[#2D6A4F] pl-8">
            {{ t('protectedHorizons') }}
          </p>
        </div>
      </div>
    </section>

    <!-- ================= 7. THE CULTURAL PULSE ================= -->
    <section class="relative z-10 py-44 px-6 bg-[#0a0a0a] text-white">
      <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-24 items-center">
        <div class="space-y-10">
          <div class="inline-block px-8 py-3 bg-[#FAD201] text-black font-black text-sm tracking-[0.5em] uppercase">
            {{ t('theCulturalPulse') }}
          </div>
          <h2 class="text-8xl font-black tracking-tighter leading-[0.8] uppercase">
            {{ t('humanVibrancy') }}<br/>
            <span class="text-[#FAD201]">{{ t('vibrancy') }}</span>
          </h2>
          <p class="text-2xl text-zinc-400 font-bold border-l-[10px] border-[#FAD201] pl-8">
            {{ t('heartbeatTradition') }}
          </p>
        </div>
        <div class="imigongo-portal w-[550px] h-[550px] overflow-hidden relative shadow-[0_0_0_15px_#FAD201] bg-black">
          <img :src="assets.rwandans" class="w-full h-full object-cover grayscale-0" />
        </div>
      </div>
    </section>

    <!-- ================= FOOTER ================= -->
    <footer class="bg-black pt-24 pb-12 border-t-[20px] border-[#00A3E0]">
      <div class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-2 gap-20">
        <div class="space-y-4">
          <h3 class="text-3xl font-black uppercase mb-8">{{ t('whatMakesUsDifferent') }}</h3>
          <div v-for="(item, index) in differences" :key="index" class="border border-white/10">
            <button @click="activeDiff = activeDiff === index ? null : index" 
                    class="w-full p-6 flex justify-between items-center bg-white/5 hover:bg-white/10 transition-all">
              <span class="font-bold text-lg">{{ t(item.titleKey) }}</span>
              <span class="text-[#FAD201] text-2xl">{{ activeDiff === index ? '−' : '+' }}</span>
            </button>
            <div v-if="activeDiff === index" class="p-6 bg-[#0a0a0a] border-t border-white/5 text-zinc-400 leading-relaxed">
              {{ t(item.descKey) }}
            </div>
          </div>
        </div>

        <div class="bg-[#2D6A4F] p-12 relative overflow-hidden">
          <h3 class="text-4xl font-black uppercase mb-6">{{ t('stayConnected') }}</h3>
          <p class="mb-8 opacity-80">{{ t('joinMovement') }}</p>
          <form class="space-y-4" @submit.prevent>
            <input type="email" :placeholder="t('yourEmailAddress')" 
                   class="w-full p-4 bg-black/30 border-2 border-white/20 outline-none focus:border-[#FAD201] transition-all placeholder:text-white/30" />
            <button class="w-full bg-[#FAD201] text-black font-black py-4 uppercase hover:bg-white transition-all">
              {{ t('subscribe') }}
            </button>
          </form>
          <div class="absolute bottom-0 left-0 w-full h-3 flex">
            <div class="flex-1 bg-[#00A3E0]"></div>
            <div class="flex-1 bg-[#FAD201]"></div>
            <div class="flex-1 bg-[#2D6A4F]"></div>
          </div>
        </div>
      </div>
      <div class="text-center mt-20 text-zinc-600 text-sm uppercase tracking-[0.2em]">
        © 2026 Tembera Rwanda. {{ t('allRightsReserved') }}
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const currentLang = ref('en')

const languages = [
  { code: 'en', label: 'EN' },
  { code: 'rw', label: 'RW' },
  { code: 'fr', label: 'FR' }
]

const translations = {
  en: {
    landOfThousandHills: "Land of Thousand Hills",
    theVisionaryCore: "The Visionary Core",
    stateResilience: "State",
    resilience: "Resilience",
    architectingGlobalHub: "Architecting a global hub of innovation.",
    partnershipEcosystem: "Partnership Ecosystem",
    theSovereignPath: "The Sovereign Path",
    ourHistory: "Our",
    history: "History",
    tracingJourney: "Tracing the journey of a thousand hills.",
    theLivingEarth: "The Living Earth",
    deepNature: "Deep",
    nature: "Nature",
    protectedHorizons: "Protected horizons, untamed and pure.",
    theCulturalPulse: "The Cultural Pulse",
    humanVibrancy: "Human",
    vibrancy: "Vibrancy",
    heartbeatTradition: "The heartbeat of Rwandan tradition.",
    whatMakesUsDifferent: "What Makes Us Different",
    stayConnected: "Stay Connected",
    joinMovement: "Join the movement of the thousand hills. Get updates on our digital evolution.",
    yourEmailAddress: "YOUR EMAIL ADDRESS",
    subscribe: "Subscribe",
    allRightsReserved: "All Rights Reserved.",

    // Stats
    connectivity: "Connectivity",
    annualGrowth: "Annual Growth",
    transparency: "Transparency",
    businessSetup: "Business Setup",

    // Differences
    digitalResilience: "Digital Resilience",
    digitalResilienceDesc: "Our infrastructure is built for high-uptime, high-capacity traffic across the entire region.",
    culturalIntegration: "Cultural Integration",
    culturalIntegrationDesc: "Every line of code respects the heritage of Imigongo and traditional patterns, merging tech with soul.",
    transparencyFirst: "Transparency First",
    transparencyFirstDesc: "We leverage secure blockchain and efficient admin dashboards to ensure 0% corruption in transactions."
  },

  rw: {
    landOfThousandHills: "Igihugu cy'Imisozi Igihumbi",
    theVisionaryCore: "Ingufu y'Ikirenga",
    stateResilience: "Leta",
    resilience: "Kwihangana",
    architectingGlobalHub: "Gushinga ikiyiko cy'isi y'ubuhanga.",
    partnershipEcosystem: "Ubufatanye n'Abandi",
    theSovereignPath: "Inzira y'Ubwigenge",
    ourHistory: "Amateka",
    history: "Yacu",
    tracingJourney: "Kuronda urugendo rw'imisozi igihumbi.",
    theLivingEarth: "Isi Ibona",
    deepNature: "Kirekire",
    nature: "Kamere",
    protectedHorizons: "Imirenge irindwa, itaribo n'umwanda.",
    theCulturalPulse: "Umutima w'Umuco",
    humanVibrancy: "Abantu",
    vibrancy: "Bafite ubuzima",
    heartbeatTradition: "Umutima w'umuco nyarwanda.",
    whatMakesUsDifferent: "Ibyatwandukanya",
    stayConnected: "Umenye Ibya Tembera",
    joinMovement: "Iyemeza urugendo rw'imisozi igihumbi. Habwa amakuru y'iterambere ry'ikoranabuhanga.",
    yourEmailAddress: "IMEYILI YAWE",
    subscribe: "Iyandikisha",
    allRightsReserved: "Uburenganzira bwose burarindwa.",

    connectivity: "Ukwihuza",
    annualGrowth: "Iterambere buri mwaka",
    transparency: "Ubutabera",
    businessSetup: "Gushinga ibikorwa mu masaha 24",

    digitalResilience: "Kwihangana mu Ikoranabuhanga",
    digitalResilienceDesc: "Ibikorwa byacu byubakwa kugira ngo bikore neza igihe kirekire.",
    culturalIntegration: "Guhuza Umuco",
    culturalIntegrationDesc: "Buri kode yubaha umuco w'Imigongo n'imihango gakondo.",
    transparencyFirst: "Ubutabera Ubwa Mbere",
    transparencyFirstDesc: "Dukoresha blockchain kugira ngo habemo ubwiyunge nta ruswa."
  },

  fr: {
    landOfThousandHills: "Pays des Mille Collines",
    theVisionaryCore: "Le Cœur Visionnaire",
    stateResilience: "État",
    resilience: "Résilience",
    architectingGlobalHub: "Construire un hub mondial d'innovation.",
    partnershipEcosystem: "Écosystème de Partenariats",
    theSovereignPath: "La Voie Souveraine",
    ourHistory: "Notre",
    history: "Histoire",
    tracingJourney: "Retracer le parcours des mille collines.",
    theLivingEarth: "La Terre Vivante",
    deepNature: "Nature",
    nature: "Profonde",
    protectedHorizons: "Horizons protégés, sauvages et purs.",
    theCulturalPulse: "Le Pouls Culturel",
    humanVibrancy: "Vibrance",
    vibrancy: "Humaine",
    heartbeatTradition: "Le battement du cœur de la tradition rwandaise.",
    whatMakesUsDifferent: "Ce qui nous distingue",
    stayConnected: "Restez Connecté",
    joinMovement: "Rejoignez le mouvement des mille collines. Recevez les mises à jour.",
    yourEmailAddress: "VOTRE ADRESSE EMAIL",
    subscribe: "S'abonner",
    allRightsReserved: "Tous droits réservés.",

    connectivity: "Connectivité",
    annualGrowth: "Croissance Annuelle",
    transparency: "Transparence",
    businessSetup: "Création d'Entreprise",

    digitalResilience: "Résilience Numérique",
    digitalResilienceDesc: "Notre infrastructure est conçue pour une haute disponibilité.",
    culturalIntegration: "Intégration Culturelle",
    culturalIntegrationDesc: "Chaque ligne de code respecte l'héritage de l'Imigongo.",
    transparencyFirst: "Transparence d'Abord",
    transparencyFirstDesc: "Nous utilisons la blockchain pour garantir zéro corruption."
  }
}

const t = (key) => translations[currentLang.value][key] || key

const switchLanguage = (lang) => {
  currentLang.value = lang
  document.documentElement.lang = lang
}

// Assets
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
  { wordKey: 'URWANDA', video: assets.rwandaVideo, color: '#00A3E0' },
  { wordKey: 'HERITAGE', video: assets.sunsetVideo, color: '#FAD201' },
  { wordKey: 'FUTURE', video: assets.urugaryVideo, color: '#2D6A4F' }
]

const stats = [
  { value: '95%', labelKey: 'connectivity' },
  { value: '8%', labelKey: 'annualGrowth' },
  { value: '1st', labelKey: 'transparency' },
  { value: '24h', labelKey: 'businessSetup' }
]

const differences = [
  { 
    titleKey: 'digitalResilience', 
    descKey: 'digitalResilienceDesc' 
  },
  { 
    titleKey: 'culturalIntegration', 
    descKey: 'culturalIntegrationDesc' 
  },
  { 
    titleKey: 'transparencyFirst', 
    descKey: 'transparencyFirstDesc' 
  }
]

onMounted(() => {
  setInterval(() => {
    activeSlideIndex.value = (activeSlideIndex.value + 1) % heroSlides.length
  }, 6000)
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