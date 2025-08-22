<template>
	<v-btn class="bg-primary" id="mediaControl" @click="togglePlay">
		<v-icon color="white">
			{{ isPlaying ? "mdi-pause" : "mdi-play" }}
		</v-icon>
	</v-btn>
</template>

<script setup>
	import { ref } from "vue";

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
