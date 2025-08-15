import { createApp } from 'vue'
import App from './App.vue'
import '/earth-globe.png';
import '@mdi/font/css/materialdesignicons.css'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import { VApp, VAppBar, VMain, VCard, VCardTitle, VAutocomplete, VImg, VCardText, VFooter, VBtn, VIcon, VRow, VCol, VSelect } from 'vuetify/components'
const vuetify = createVuetify({
  components: {
    VApp,
    VAppBar,
    VMain,
    VCard,
    VBtn,
    VIcon,
    VRow,
    VCol,
    VSelect,
    VCardTitle,
    VAutocomplete,
    VImg,
    VCardText,
    VFooter
  }
})

createApp(App).use(vuetify).mount('#app')
