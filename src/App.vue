<template>
	<!-- Header of the page -->
	<v-row class="bg-light align-center text-center w-75 my-4 mx-auto rounded-xl">
		<v-col cols="6" lg="5">
			<v-card-title>
				<a href="/" class="text-primary">Anthem Index 🌍</a>
			</v-card-title>
		</v-col>
		<v-col cols="0" lg="2" class="hidden-md-and-down"></v-col>
		<v-col cols="6" lg="4" class="px-4 py-2">
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
				class="bg-primary rounded-xl" />
		</v-col>
	</v-row>

	<!-- Welcome message or country name, flag and media button -->
	<div class="content w-75 mx-auto text-primary">
		<v-row>
			<v-col cols="4 mx-auto mt-8 bg-light rounded-xl" style="height: 65vh; overflow-y: auto">
				<v-row v-if="message" justify="center" align="end" class="py-6">
					<v-col cols="5" sm="6" class="text-center">
						<v-card-title class="text-wrap">{{ message }}</v-card-title>
						<video :src="sourceURL" @timeupdate="updateTime"></video>
						<MediaButton v-if="sourceURL" class="w-25 ml-25 px-14" />
						<div v-else></div>
					</v-col>
					<v-col cols="7" sm="6" class="text-center">
						<img
							v-if="flagLink"
							:src="flagLink"
							alt="flag"
							class="flag-img mt-auto mb-auto"
							width="130px"
							height="70px" />
						<div v-else class="loading">
							<div class="spinner"></div>
						</div>
					</v-col>
				</v-row>
				<v-row v-else justify="center" align="center" class="py-14">
					<v-col v-if="!fetchedData" cols="6" lg="7" class="text-center py-8">
						<v-card-title class="text-wrap">Welcome to Anthem Index!</v-card-title>
					</v-col>
					<div v-else class="loading">
						<div class="spinner"></div>
					</div>
					<v-col cols="0" lg="1" class="hidden-md-and-down"></v-col>
					<v-col cols="6" lg="4">
						<v-img
							src="https://cdn.pixabay.com/photo/2016/02/04/13/40/the-earth-1179205_1280.png"
							alt="Earth Globe"
							class="flag-img w-50 h-50"></v-img>
					</v-col>
				</v-row>
				<div class="py-6 px-6 bg-light w-100 text-primary">
					<v-card-title>Title</v-card-title>
					<v-card-text>The title of the song is {{ title }}.</v-card-text>
					<v-card-title>Composition</v-card-title>
					<v-card-text>The song was written by {{ lyricist }} and composed by {{ composer }}</v-card-text>
					<v-card-title>Date</v-card-title>
					<v-card-text>Research suggests the song originated in {{ year }}</v-card-text>
					<v-card-title>Info</v-card-title>
					<v-card-text class="text-pre-wrap">{{ short_fact }}</v-card-text>
				</div>
			</v-col>
			<v-col cols="7 mx-auto mt-8">
				<v-row class="bg-light rounded-xl text-center" style="height: 50vh; overflow-y: auto">
					<!-- Lyrics or welcome message or loading spinner -->
					<div
						v-if="lyrics"
						id="lyrics"
						class="text-pre-wrap text-center overflow-auto mx-auto px-8 py-6 text-primary"
						v-html="lyrics"></div>
					<span v-else-if="!fetchedData" span>
						<v-card-title>Explore Our Rich Collection of Songs</v-card-title>
						<v-card-text
							>Learn the lyrics and listen to the tunes of national anthems from all over the
							world!</v-card-text
						>
						<v-card-text
							>Select any country from our dropdown menu at the top or try the random country suggested
							below!</v-card-text
						>
					</span>
					<div v-else class="loading min-h-screen">
						<div class="spinner"></div>
					</div>
				</v-row>
				<v-row class="mt-8">
					<v-card style="height: 13vh" class="w-100 text-primary rounded-xl bg-light">
						<v-card-title>Why don't you try this one:</v-card-title>
						<v-card-text class="mt-4 ml-8">
							<a :href="`/${randomCountry}`" class="text-decoration-none text-primary">
								<v-row>
									<v-col cols="2">
										<img :src="randomCountryFlag" alt="" />
									</v-col>
									<v-col cols="10" class="align-text">{{ randomCountry }}</v-col>
								</v-row>
							</a>
						</v-card-text>
					</v-card>
				</v-row>
			</v-col>
		</v-row>
	</div>
		<v-row class="bg-light align-center text-center w-75 mt-8 mx-auto rounded-xl py-6 h-50 text-primary" >
			<v-col cols="12" class="text-center">
				<p>Sponsored by <a href="https://www.novariance.com" class="text-primary">No Variance.com</a></p>
			</v-col>
		</v-row>
</template>

<script setup>
	import { ref, onMounted } from "vue";
	import MediaButton from "./MediaControl.vue";
	const message = ref("");
	const sourceURL = ref("");
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
			sourceURL.value = data.source;
			flagLink.value = data.flag_link ? data.flag_link.replace("40px", "130px") : none;
			lyrics.value = data.lyrics.replace(
				/\n\n\n/g,
				'\n\n<hr style="border: 1px solid grey; margin: 1rem auto; width: 60%;">\n',
			);
			lyricist.value = data.lyricist;
			composer.value = data.composer;
			year.value = data.year;
			title.value = data.anthem_name ? data.anthem_name : none;
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
</script>

<style scoped>
	* {
		font-family: 'D-DIN Condensed', sans-serif;
		color: primary;
		border: 0px solid black !important;
	}
	/* Flag */
	.flag-img {
		max-width: 200px;
		margin-bottom: 1rem;
	}

	/* Loading state */
	.loading {
		display: flex;
		flex: 1;
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

	video {
		display: none;
	}

	a[href="/"] {
		text-decoration-color: primary;
	}
	.v-card {
		border: none;
	}

	/* .content .v-row .v-col  {
		border: 2px solid red;
	} */

	 html {
    overflow: scroll;
    overflow-x: hidden;
}
::-webkit-scrollbar {
    width: 0;  /* Remove scrollbar space */
    background: transparent;  /* Optional: just make scrollbar invisible */
}
/* Optional: show position indicator in red */
::-webkit-scrollbar-thumb {
    background: transparent
}
</style>
