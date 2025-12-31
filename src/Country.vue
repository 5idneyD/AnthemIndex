<template>
	<v-row class="gap-6" align="stretch">
		<!-- Left column: Info + Media -->
		<v-col cols="12" md="6">
			<div class="neo-card px-8 mt-14 py-6 flex flex-col overflow-auto">
				<v-row justify="center" class="py-6">
					<v-col cols="7" sm="6" class="text-center">
						<v-card-title class="">{{ message }}</v-card-title>
						<img
							v-if="flagLink"
							:src="flagLink"
							alt="flag"
							class="flag-img mt-6 mb-auto"
							width="110px"
							height="70px" />
						<div v-else></div>
					</v-col>
					<v-col cols="5" sm="6" class="text-center align-center">
						<video :src="selectedSource" @timeupdate="updateTime" class="d-none"></video>

						<span v-if="selectedSource">
							<MediaButton class="mt-4 px-10" />

							<!-- Centered switch -->
							<div class="d-flex justify-center mt-3">
								<v-switch
									id="anthem-type-switch"
									inset
									@change="switchAnthemType"
									:disabled="!vocalSourceURL || !sourceURL" />
							</div>

							<p v-text="vocalSourceURL && sourceURL ? selectedAnthemType : ''"></p>
						</span>

						<div v-else class="loading">
							<div class="spinner"></div>
						</div>
					</v-col>
				</v-row>
				<!-- Song details -->
				<div class="mt-8">
					<h3 class="font-bold mb-2">Title</h3>
					<p>{{ title }}</p>
					<h3 class="font-bold mt-4 mb-2">Composition</h3>
					<p>{{ lyricist }} & {{ composer }}</p>
					<h3 class="font-bold mt-4 mb-2">Date</h3>
					<p>{{ year }}</p>
					<h3 class="font-bold mt-4 mb-2">Info</h3>
					<p class="text-pre-wrap">{{ short_fact }}</p>
				</div>
			</div>
		</v-col>
		<!-- Right column: Lyrics + Suggestion -->
		<v-col cols="12" md="6" class="d-flex flex-column gap-6">
			<div class="neo-card h-50 px-8 py-6 flex flex-col flex-1 overflow-auto">
				<div v-if="lyrics" id="lyrics" class="text-pre-wrap text-center pt-8" v-html="lyrics"></div>
				<div v-else class="loading min-h-[200px]"><div class="spinner"></div></div>
			</div>
			<RandomCountry />
		</v-col>
	</v-row>
</template>
<script setup>
	import "@/assets/colours.css";
	import RandomCountry from "./RandomCountry.vue";
	import MediaButton from "./MediaControl.vue";
	import { ref, onMounted } from "vue";

	const message = ref("");
	const sourceURL = ref("");
	const vocalSourceURL = ref("");
	const selectedAnthemType = ref("Vocal"); // not true/false
	const selectedSource = ref("");
	const flagLink = ref("");
	const lyrics = ref("");
	const lyricist = ref("");
	const composer = ref("");
	const year = ref("");
	const short_fact = ref("");
	const title = ref("");

	const fetchedData = ref(false);

	onMounted(async () => {
		const fetchedCountry = window.location.pathname.split("/")[1];
		if (fetchedCountry) {
			fetchedData.value = true;
			const res = await fetch("/api/" + fetchedCountry);
			const data = await res.json();
			message.value = data.country ? data.country : null;
			sourceURL.value = data.source && data.source !== "" ? data.source : null;
			vocalSourceURL.value =
				data.vocal_media && data.vocal_media !== "" ? window.location.origin + "/" + data.vocal_media : null;
			selectedSource.value =
				data.vocal_media && data.vocal_media !== ""
					? window.location.origin + "/" + data.vocal_media
					: data.source;
			flagLink.value = data.flag_link ? data.flag_link.replace("40px", "130px") : null;
			lyrics.value = data.lyrics.replace(
				/\n\n\n/g,
				'\n\n<hr style="border: 1px solid #aff8c4; margin: 1rem auto; width: 60%;">\n',
			);
			lyricist.value = data.lyricist;
			composer.value = data.composer;
			year.value = data.year;
			title.value = data.anthem_name ? data.anthem_name : null;
			short_fact.value = data.short_fact
				.replace(". ", ". \n\n")
				.replace(/\[.*?\]/g, "")
				.replace(".\n", ".\n\n");
		} else {
		}
	});

	function switchAnthemType() {
		if (selectedAnthemType.value === "Vocal") {
			selectedSource.value = sourceURL.value;
			selectedAnthemType.value = "Non-Vocal";
		} else if (selectedAnthemType.value === "Non-Vocal") {
			selectedSource.value = vocalSourceURL.value;
			selectedAnthemType.value = "Vocal";
		} else {
			// default (first switch)
			selectedSource.value = vocalSourceURL.value;
			selectedAnthemType.value = "Vocal";
		}
	}
</script>

<style scoped>
	@import "./assets/styles.css";
	.v-btn {
		background-color: var(--buttonColor);
	}
</style>
