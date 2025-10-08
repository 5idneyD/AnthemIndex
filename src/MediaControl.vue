<template>
	<v-btn class="bg-blue-grey-darken-4" id="mediaControl" @click="togglePlay">
		<v-icon color="light">
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
