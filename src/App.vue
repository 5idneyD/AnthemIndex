<template>
	<v-card class="bg-grey-darken-4 d-flex align-center justify-space-between">
		<v-card-title class="text-white">Anthem Index 🌍</v-card-title>
		<v-autocomplete
			v-model="selectedCountry"
			:items="countries"
			item-title="name"
			item-value="name"
			label="Select a country"
			@update:modelValue="selectCountry"
			outlined
			dense
			hide-details
			style="max-width: 200px" />
	</v-card>

	<v-card class="bg-grey-lighten-5" border="lg">
		<v-row justify="center" align="end" class="py-6">
			<v-col cols="5" sm="6" class="text-center">
				<v-card-title class="text-wrap">{{ message }}</v-card-title>
				<video :src="sourceURL" @timeupdate="updateTime"></video>
				<MediaButton class="w-50 ml-25"/>
			</v-col>
			<v-col cols="7" sm="6" class="text-center">
				<img v-if="sourceURL" :src="flagLink" alt="flag" class="flag-img mt-auto mb-auto" />
				<div v-else class="loading">
					<div class="spinner"></div>
				</div>
			</v-col>
		</v-row>
	</v-card>

	<v-card class="bg-grey-lighten-5 px-4 py-6">
		<div id="lyrics" class="text-pre-wrap">
			<p>{{ lyrics }}</p>
		</div>
	</v-card>

	<v-card class="bg-grey-lighten-5" border="lg">
		<v-card-title>Title</v-card-title>
		<v-card-text>The title of the song is {{ title }}.</v-card-text>
		<v-card-title>Composition</v-card-title>
		<v-card-text>The song was written by {{ lyricist }} and composed by {{ composer }}</v-card-text>
		<v-card-title>Date</v-card-title>
		<v-card-text>Research suggests the song originated in {{ year }}</v-card-text>
	</v-card>

	<v-footer class="bg-grey-darken-4 text-white">
		<v-row justify="center">
			<v-col cols="12" sm="6" class="text-center">
				<p>Sponsored by <a href="https://www.novariance.com" class="text-grey">No Variance.com</a></p>
			</v-col>
		</v-row>
	</v-footer>	
</template>

<script setup>
	import { ref, onMounted } from "vue";
	import MediaButton from "./MediaControl.vue";
	const message = ref("Loading...");
	const sourceURL = ref("");
	const flagLink = ref("");
	const lyrics = ref("");
	const lyricist = ref("...");
	const composer = ref("...");
	const year = ref("...");
	const title = ref("...");
	const countries = ref([]);
	const selectedCountry = ref("");

	onMounted(async () => {
		const res = await fetch("/api/" + window.location.pathname.split("/")[1]);
		const data = await res.json();
		message.value = data.country;
		sourceURL.value = data.source;
		flagLink.value = data.flag_link.replace("40px", "130px");
		lyrics.value = data.lyrics;
		lyricist.value = data.lyricist;
		composer.value = data.composer;
		year.value = data.year;
		title.value = data.anthem_name;
	});

	onMounted(async () => {
		const res = await fetch("/api/countries");
		const data = await res.json();
		countries.value = data.map((row) => row[0]);
	});

	function selectCountry() {
		window.location.href = `/${selectedCountry.value}`;
	}
</script>

<style scoped>

* {
	    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}
	/* Flag */
	.flag-img {
		max-width: 200px;
		margin-bottom: 1rem;
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
		to {
			transform: rotate(360deg);
		}
	}

	/* Lyrics */
	#lyrics {
		text-align: center;
		margin-top: 1rem;
	}

	/* Responsive for mobile */
	@media (max-width: 900px) {
		main {
			flex-direction: column;
		}
		section {
			order: -1;
		}
	}

	video {
		display: none;
	}

	.notes-card {
		height: fit-content;
	}
</style>
