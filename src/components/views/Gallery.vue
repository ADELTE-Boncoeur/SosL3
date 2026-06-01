<template>
  <div class="archive-wall" @mousemove="handleMouseMove">
    <!-- Fluid Spotlight -->
    <div 
      class="spotlight"
      :style="{ transform: `translate3d(${cursorX}px, ${cursorY}px, 0)` }"
      :class="{ 'active': isHovering }"
    ></div>

    <main class="scroll-container">
      
      <!-- CINEMATIC VIDEO HEADQUARTERS -->
      <section class="video-engine">
        <div class="hero-vid-frame" @mouseenter="isHovering = true" @mouseleave="isHovering = false">
          <video autoplay muted loop playsinline class="bg-vid">
            <source :src="rwandaVid" type="video/mp4">
          </video>
          <div class="vid-overlay">
            <h1 class="glitch-text">RWANDA</h1>
            <p>PROJECT MAB // ARCHIVE 2026</p>
          </div>
        </div>

        <div class="side-channels">
          <div class="channel-card" v-for="(v, i) in channels" :key="i">
            <video autoplay muted loop playsinline @mouseenter="isHovering = true" @mouseleave="isHovering = false">
              <source :src="v.src" type="video/mp4">
            </video>
            <div class="chan-label">CH_{{ i + 1 }} // {{ v.name }}</div>
          </div>
        </div>
      </section>

      <!-- THE INFINITE GRID -->
      <section class="photo-matrix">
        <div 
          v-for="(img, idx) in allPhotos" 
          :key="idx" 
          class="matrix-item"
          :class="getLayoutClass(idx)"
          @mouseenter="isHovering = true" 
          @mouseleave="isHovering = false"
        >
          <div class="matrix-inner">
            <img :src="img.path" :alt="img.title" loading="lazy" />
            
            <!-- Glassmorphism Hover Reveal -->
            <div class="glass-info">
              <div class="glass-content">
                <span class="serial">#00{{ idx + 1 }}</span>
                <h3>{{ img.title }}</h3>
                <div class="line"></div>
                <p>MAB_ASSET_L3</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- VISION BREAKOUT (MARQUEE) -->
      <section class="vision-strip">
        <div class="strip-track">
          <img :src="visionImg" alt="Vision 1" />
          <img :src="vision1Img" alt="Vision 2" />
          <img :src="bgImg" alt="BG" />
          <img :src="visionImg" alt="Vision 1" />
          <!-- Duplicated for loop -->
          <img :src="visionImg" alt="Vision 1" />
          <img :src="vision1Img" alt="Vision 2" />
          <img :src="bgImg" alt="BG" />
          <img :src="visionImg" alt="Vision 1" />
        </div>
      </section>

    </main>

    <footer class="system-footer">
      <span>MADE BY ADELTE // STAGE 2026</span>
      <span>KIGALI_SECTOR_01</span>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';

/* ASSET MAPPING - VIDEOS */
import rwandaVid from '../../assets/images/rwanda.mp4';
import urugaryVid from '../../assets/images/urugary.mp4';
import waterfallVid from '../../assets/images/waterfall.mp4';
import sunsetVid from '../../assets/images/sunset.mp4';

/* ASSET MAPPING - PHOTOS */
import kigaliImg from '../../assets/images/kigali.jpg';
import teaImg from '../../assets/images/tea plantation.jpg';
import visitImg from '../../assets/images/visit rwanda.jpg';
import northImg from '../../assets/images/north.jpg';
import southImg from '../../assets/images/south.jpg';
import easternImg from '../../assets/images/eastern.jpg';
import eastern1Img from '../../assets/images/eastern1.jpg';
import eastern2Img from '../../assets/images/eastern2.jpg';
import east3Img from '../../assets/images/east3.jpg';
import westImg from '../../assets/images/west.jpg';
import musanzeImg from '../../assets/images/musanze.jpg';
import rwandansImg from '../../assets/images/rwandans.jpg';
import rwandanMImg from '../../assets/images/rwandanM.jpg';
import rwandan1Img from '../../assets/images/rwandan1.jpg';
import rwNImg from '../../assets/images/rwN.jpg';
import presidentImg from '../../assets/images/president.jpg';
import presidentWomanImg from '../../assets/images/prwsident_woman.jpg';
import historyImg from '../../assets/images/ourhistory.jpg';
import history1Img from '../../assets/images/ourhistory1.jpg';
import history2Img from '../../assets/images/ourhistory2.jpg';
import visionImg from '../../assets/images/vision.jpg';
import vision1Img from '../../assets/images/vision1.jpg';
import bgImg from '../../assets/images/background.jpg';
import bg2Img from '../../assets/images/background2.jpg';

const cursorX = ref(0);
const cursorY = ref(0);
const isHovering = ref(false);

const channels = [
  { src: urugaryVid, name: 'URUGARY_NATURE' },
  { src: waterfallVid, name: 'WATERFALL_FX' },
  { src: sunsetVid, name: 'DUSK_HORIZON' }
];

const allPhotos = [
  { path: kigaliImg, title: 'KIGALI_URBAN' },
  { path: teaImg, title: 'TEA_PLANTATION' },
  { path: northImg, title: 'VOLCANO_NORTH' },
  { path: southImg, title: 'SOUTHERN_PROVINCE' },
  { path: westImg, title: 'KIVU_SHORES' },
  { path: easternImg, title: 'AKAGERA_EAST' },
  { path: eastern1Img, title: 'SAVANNA_LIFE' },
  { path: eastern2Img, title: 'WILD_RESERVE' },
  { path: east3Img, title: 'LAKE_MUHAZI' },
  { path: musanzeImg, title: 'MUSANZE_CAVES' },
  { path: visitImg, title: 'VISIT_RWANDA' },
  { path: rwandansImg, title: 'CULTURAL_HERITAGE' },
  { path: rwandanMImg, title: 'LOCAL_CRAFT' },
  { path: rwandan1Img, title: 'PEOPLE_01' },
  { path: rwNImg, title: 'NATURAL_FLORA' },
  { path: presidentImg, title: 'GOVERNANCE_ST' },
  { path: presidentWomanImg, title: 'LEADERSHIP_V' },
  { path: historyImg, title: 'HISTORICAL_ROOTS' },
  { path: history1Img, title: 'MEMORY_01' },
  { path: history2Img, title: 'TRUTH_ARC' },
  { path: bg2Img, title: 'MIST_VALLEY' },
  { path: bgImg, title: 'LANDSCAPE_RAW' }
];

const handleMouseMove = (e) => {
  cursorX.value = e.clientX;
  cursorY.value = e.clientY;
};

const getLayoutClass = (i) => {
  const types = ['span-v', 'span-h', 'standard', 'span-v', 'standard'];
  return types[i % 5];
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;700&family=Unbounded:wght@900&display=swap');

.archive-wall {
  background: #050505;
  color: #fff;
  min-height: 100vh;
  cursor: none;
  font-family: 'Space Grotesk', sans-serif;
  overflow-x: hidden;
}

/* SPOTLIGHT */
.spotlight {
  position: fixed;
  top: -100px; left: -100px;
  width: 200px; height: 200px;
  background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
  pointer-events: none; z-index: 9999;
  will-change: transform;
}
.spotlight.active {
  background: radial-gradient(circle, rgba(0, 112, 60, 0.2) 0%, transparent 70%);
  width: 400px; height: 400px;
  margin-left: -100px; margin-top: -100px;
}

/* VIDEO ENGINE */
.video-engine {
  display: flex; height: 80vh; gap: 10px; padding: 20px 10px 10px;
}
.hero-vid-frame { flex: 2; position: relative; overflow: hidden; border-radius: 4px; }
.bg-vid { width: 100%; height: 100%; object-fit: cover; filter: brightness(0.7); }
.vid-overlay {
  position: absolute; bottom: 40px; left: 40px;
}
.vid-overlay h1 { font-family: 'Unbounded', sans-serif; font-size: 6vw; margin: 0; }

.side-channels { flex: 0.8; display: flex; flex-direction: column; gap: 10px; }
.channel-card { flex: 1; position: relative; overflow: hidden; border-radius: 4px; }
.channel-card video { width: 100%; height: 100%; object-fit: cover; filter: grayscale(1); }
.channel-card:hover video { filter: grayscale(0); }
.chan-label { position: absolute; top: 10px; left: 10px; font-size: 8px; font-weight: 700; background: #000; padding: 4px 8px; }

/* MATRIX GRID */
.photo-matrix {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-auto-rows: 300px;
  grid-auto-flow: dense;
  gap: 10px; padding: 10px;
}

.matrix-item { position: relative; overflow: hidden; border-radius: 4px; background: #111; }
.span-v { grid-row: span 2; }
.span-h { grid-column: span 2; }

.matrix-inner { width: 100%; height: 100%; }
.matrix-inner img { 
  width: 100%; height: 100%; object-fit: cover; 
  filter: grayscale(1) contrast(1.1);
  transition: transform 1s cubic-bezier(0.19, 1, 0.22, 1);
}

/* GLASSMORPHISM HOVER REVEAL */
.glass-info {
  position: absolute; inset: 0;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(0px);
  display: flex; align-items: center; justify-content: center;
  opacity: 0; transition: all 0.5s ease;
}

.matrix-item:hover .glass-info { opacity: 1; backdrop-filter: blur(12px); }
.matrix-item:hover img { transform: scale(1.1); filter: grayscale(0); }

.glass-content { text-align: center; padding: 20px; }
.serial { font-size: 10px; color: #fadb14; font-weight: 700; }
.glass-content h3 { font-size: 1.2rem; margin: 10px 0; letter-spacing: 1px; }
.line { width: 40px; height: 1px; background: #fff; margin: 0 auto 10px; }
.glass-content p { font-size: 8px; opacity: 0.6; letter-spacing: 2px; }

/* STRIP ANIMATION (MARQUEE) */
.vision-strip { height: 30vh; margin: 100px 0; overflow: hidden; border-top: 1px solid #222; border-bottom: 1px solid #222; }
.strip-track { display: flex; width: max-content; height: 100%; animation: slide 40s linear infinite; }
.strip-track img { height: 100%; object-fit: cover; filter: brightness(0.5); padding-right: 10px; }

@keyframes slide { from { transform: translateX(0); } to { transform: translateX(-50%); } }

.system-footer {
  padding: 60px 40px; display: flex; justify-content: space-between;
  font-size: 10px; opacity: 0.4; letter-spacing: 2px;
}

@media (max-width: 768px) {
  .video-engine { flex-direction: column; height: auto; }
  .span-h { grid-column: span 1; }
}
</style>