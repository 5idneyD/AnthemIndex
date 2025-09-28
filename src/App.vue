<template>
	<v-app class="bg-neutral">
		<!-- Header -->
		<v-app-bar flat color="primary" class="px-6 py-4 border-thick">
			<v-col cols="8" lg="7">
				<v-card-title>
					<a href="/" class="text-black text-center">Anthem Index 🌍</a>
				</v-card-title>
			</v-col>
			<v-col cols="0" lg="1" class="hidden-md-and-down"></v-col>
			<v-col cols="4" lg="4">
				<v-autocomplete
					v-model="selectedCountry"
					:items="countries"
					item-title="name"
					item-value="name"
					label="Select a country"
					hide-details
					variant="outlined"
					class="neo-input"
					@update:modelValue="selectCountry" />
			</v-col>
		</v-app-bar>
		<!-- Main Content -->
		<v-main class="px-6 py-10">
			<v-container fluid>
				<v-row class="gap-6" align="stretch">
					<!-- Left column: Info + Media -->
					<v-col cols="12" md="6">
						<div class="neo-card px-8 mt-14 py-6 flex flex-col overflow-auto">
							<v-row v-if="message" justify="center" class="py-6">
								<v-col cols="7" sm="6" class="text-center">
									<v-card-title class="">{{ message }}</v-card-title>
									<video :src="selectedSource" @timeupdate="updateTime" class="d-none"></video>
									<span v-if="selectedSource">
										<MediaButton class="w-25 ml-25 mt-4 px-14" />
										<v-switch
											inset
											color="dark"
											class="ml-4 text-caption"
											
											@change="switchAnthemType"
											:label="vocalSourceURL && sourceURL ? selectedAnthemType: ''"
											:disabled="!vocalSourceURL || !sourceURL">
										</v-switch>
									</span>
									<div v-else></div>
								</v-col>
								<v-col cols="5" sm="4" class="text-center">
									<img
										v-if="flagLink"
										:src="flagLink"
										alt="flag"
										class="flag-img mt-6 mb-auto"
										width="110px"
										height="70px" />
									<div v-else class="loading">
										<div class="spinner"></div>
									</div>
								</v-col>
							</v-row>
							<div v-else-if="!fetchedData" class="text-center">
								<h2 class="text-xl font-bold mb-4">Welcome to Anthem Index!</h2>
								<v-img
									src="https://cdn.pixabay.com/photo/2016/02/04/13/40/the-earth-1179205_1280.png"
									alt="Earth Globe"
									max-width="180"
									class="mx-auto my-14" />
								<v-card-title>Play our Quiz:</v-card-title>
								<v-card-text class="text-grey py-8 px-16">
									<Quiz />
								</v-card-text>
							</div>
							<div v-else class="loading"><div class="spinner"></div></div>
							<!-- Song details -->
							<div v-if="title" class="mt-8">
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
						<div class="neo-card h-50 px-8 mt-14 py-6 flex flex-col flex-1 overflow-auto">
							<div v-if="lyrics" id="lyrics" class="text-pre-wrap text-center pt-8" v-html="lyrics"></div>
							<div v-else-if="!fetchedData">
								<h2 class="font-bold mb-4">Explore Our Rich Collection of Songs</h2>
								<p>
									Learn the lyrics and listen to the tunes of national anthems from all over the
									world!
								</p>
								<br />
								<p>
									Select any country from our dropdown menu at the top or try the random country
									suggested below!
								</p>
							</div>
							<div v-else class="loading min-h-[200px]"><div class="spinner"></div></div>
						</div>
						<div class="neo-card mt-6 px-12 py-8" style="min-height: 150px">
							<h3 class="font-bold mb-8">Why don't you try this one:</h3>
							<a :href="'/' + randomCountry" class="text-primary mt-4">
								<img :src="randomCountryFlag" alt="flag" />
								<span class="font-bold ml-8 mt-6">{{ randomCountry }}</span>
							</a>
						</div>
					</v-col>
				</v-row>
			</v-container>
		</v-main>
		<!-- Footer -->
		<v-footer class="bg-primary border-thick">
			<v-container class="text-center text-black">
				<p>
					Sponsored by
					<a href="https://www.novariance.com" class="text-black underline">No Variance.com</a>
				</p>
			</v-container>
		</v-footer>
	</v-app>
</template>
<script setup>
	import { ref, onMounted } from "vue";
	import MediaButton from "./MediaControl.vue";
	import Quiz from "./Quiz.vue";
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
	const countries = ref([]);
	const selectedCountry = ref("");
	const randomCountry = ref("");
	const randomCountryFlag = ref("");

	const fetchedData = ref(false);

	onMounted(async () => {
		const fetchedCountry = window.location.pathname.split("/")[1];
		if (fetchedCountry) {
			fetchedData.value = true;
			const res = await fetch("/api/" + fetchedCountry);
			const data = await res.json();
			message.value = data.country ? data.country : none;
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
				'\n\n<hr style="border: 1px solid white; margin: 1rem auto; width: 60%;">\n',
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

	onMounted(async () => {
		const res = await fetch("/api/countries");
		const data = await res.json();
		countries.value = data.map((row) => row[0]);
		let ind = [Math.floor(Math.random() * data.length)];
		randomCountry.value = data[ind][0];
		randomCountryFlag.value = data[ind][1];
	});

	function selectCountry() {
		window.location.href = `/${selectedCountry.value}`;
	}

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
	.bg-neutral {
		background-color: #8bd48d;
	}
	.border-thick {
		border: 3px solid black !important;
	}
	.neo-card {
		/* /background: #ffffff; */
		background-color: #389b64;
		color: #e9f0e9;
		border: 3px solid black;
		box-shadow: 6px 6px 0px #000;
		border-radius: 0;
		min-height: 50vh;
		max-height: 90vh;
	}
	.neo-input .v-field__input {
		border: 3px solid black;
		box-shadow: 4px 4px 0px #000;
		background-color: #fff !important;
	}
	.neo-divider {
		border: 2px solid black;
		margin: 1rem auto;
		width: 60%;
	}
	.spinner {
		border: 6px solid rgba(0, 0, 0, 0.1);
		border-top: 6px solid #000;
		border-radius: 50%;
		width: 48px;
		height: 48px;
		animation: spin 1s linear infinite;
	}

	a {
		white-space: nowrap;
		overflow: visible;
	}

	@keyframes spin {
		to {
			transform: rotate(360deg);
		}
	}
</style>
