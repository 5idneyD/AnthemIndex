<template>
  <div class="app-container">
    <header>
      <h1 class="title">{{ message }}</h1>
    </header>

    <main>
      <!-- LEFT COLUMN: Notes -->
      <aside class="sidebar">
        <h2>Title</h2>
        <p>The title of the song is {{ title }}.</p>
        <h2>Composition</h2>
        <p>The song was written by {{ lyricist }} and composed by {{ composer }}</p>
        <h2>Date</h2>
        <p>Research suggests the song originated in {{ year }}</p>
      </aside>

      <!-- CENTER COLUMN: Main Content -->
      <section class="content">
        <img :src="flagLink" alt="flag" class="flag-img">

        <iframe
          v-if="sourceURL"
          :src="sourceURL"
          frameborder="0"
          class="content-frame"
          loading="lazy"
          allowfullscreen
        ></iframe>

        <div v-else class="loading">
          <div class="spinner"></div>
          {Loading anthem…}
        </div>

        <div v-if="lyrics" class="lyrics">
          <h2>Lyrics:</h2>
          <p>{{ lyrics }}</p>
        </div>
      </section>

      <!-- RIGHT COLUMN: Placeholder -->
      <aside class="sidebar">
        <h2>Select Another Country</h2>
    <select id="country" v-model="selectedCountry" @change="selectCountry">
      <option value="">Select...</option>
      <option v-for="country in countries" :key="country" :value="country" >
        {{ country[0] }}
      </option>
    </select>
      </aside>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const message = ref('Loading...')
const sourceURL = ref('')
const flagLink = ref('')
const lyrics = ref('')
const lyricist = ref('...')
const composer = ref('...')
const year = ref('...')
const title = ref('...')
const countries = ref([])
const selectedCountry = ref('')

onMounted(async () => {
  const res = await fetch('/api/' + window.location.pathname.split('/')[1])
  const data = await res.json()
  message.value = data.country
  sourceURL.value = data.source
  flagLink.value = data.flag_link.replace('40px', '160px')
  lyrics.value = data.lyrics
  lyricist.value = data.lyricist
  composer.value = data.composer
  year.value = data.year
  title.value = data.anthem_name
})

onMounted(async () => {
  const res = await fetch('/api/countries')
  countries.value = await res.json()
})

function selectCountry(){
  window.location.href = `/${selectedCountry.value[0]}`
}
</script>

<style scoped>
/* Container */
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(135deg, #42b883 0%, #35495e 100%);
  color: #dae6e3;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  padding: 2rem 1rem;
  box-sizing: border-box;
}

/* Header */
header {
  text-align: center;
  margin-bottom: 2rem;
}

.title {
  font-size: 2.8rem;
  font-weight: 900;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

/* Main layout - three columns */
main {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 2rem;
  flex: 1;
}

/* Sidebar */
.sidebar {
  background: rgba(255, 255, 255, 0.08);
  border-radius: 10px;
  padding: 1rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  height: fit-content;
  margin-left: 5vw;
}

.sidebar h2 {
  margin-bottom: 0.5rem;
  font-size: 1.25rem;
}

.sidebar textarea::placeholder {
  color: #cfd8dc;
}

.placeholder-text {
  font-size: 0.95rem;
  color: #e0f2f1;
}

/* Center content */
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Flag */
.flag-img {
  max-width: 200px;
  margin-bottom: 1rem;
}

/* Anthem iframe */
.content-frame {
  margin-top: 1rem;
  max-height: 3rem;
  border-radius: 40px;
  border: none;
  box-shadow:
    0 8px 24px rgba(21, 101, 77, 0.6),
    0 0 20px rgba(66, 184, 131, 0.35) inset;
  background: #f5f7fa;
  transition: box-shadow 0.3s ease;
}

.content-frame:hover,
.content-frame:focus {
  box-shadow:
    0 12px 36px rgba(21, 101, 77, 0.8),
    0 0 28px rgba(66, 184, 131, 0.5) inset;
}

/* Loading state */
.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  font-size: 1.25rem;
  font-weight: 600;
}

.spinner {
  border: 6px solid rgba(66, 184, 131, 0.3);
  border-top: 6px solid #dae6e3;
  border-radius: 50%;
  width: 48px;
  height: 48px;
  animation: spin 1.1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Lyrics */
.lyrics {
  white-space: pre-wrap;
  text-align: center;
  margin-top: 1rem;
}

/* Responsive for mobile */
@media (max-width: 900px) {
  main {
    grid-template-columns: 1fr;
  }
  .sidebar {
    order: 1;
  }
  .content {
    order: 0;
  }
}
</style>
