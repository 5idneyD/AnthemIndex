<template>
	<v-btn id="mediaControl" @click="togglePlay">
		<v-icon color="light">
			{{ isPlaying ? "mdi-pause" : "mdi-play" }}
		</v-icon>
	</v-btn>
</template>

<script setup>
	import { ref } from "vue";
	import '@/assets/colours.css'
	const isPlaying = ref(false);

	function togglePlay() {
		let video = document.querySelector("video");
		if (video.paused) {
			video.play();
			isPlaying.value = true;
		} else {
			video.pause();
			isPlaying.value = false;
		}
	}
</script>

<style scoped>
.v-btn {
	background-color: var(--buttonColour);
}

i.mdi {
color: var(--buttonColour) !important;
}
</style>
