<script setup>
function playPause(){
  let video = document.querySelector('video');
  let button = document.querySelector('#mediaControl');
  if (video.paused) {
    video.play();
    button.textContent = 'II';
  } else {
    video.pause();
    button.textContent = '▶';
  }
}
</script>

<template>
  <v-btn class="bg-grey-darken-4" id="mediaControl" @click="playPause">▶</v-btn>
</template>

