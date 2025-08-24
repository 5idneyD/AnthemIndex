import { createApp } from 'vue'
import App from './App.vue'
import '/earth-globe.png';
import '@mdi/font/css/materialdesignicons.css'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import { VProgressCircular, VAlert, VApp, VAppBar, VMain, VCard, VCardTitle, VAutocomplete, VImg, VCardText, VFooter, VBtn, VIcon, VRow, VCol, VSelect } from 'vuetify/components'
const vuetify = createVuetify({
  components: {
    VProgressCircular,
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
    VFooter,
    VAlert
  },
    theme: {
    defaultTheme: 'greenTheme',
    themes: {
      greenTheme: {
        dark: false,
        colors: {
          primary: '#CFFFE2',
          accent: '#A2D5C6',
          dark: '#000000',
          light: '#F6F6F6'
        }
      }
    }
  }
})

createApp(App).use(vuetify).mount('#app')
