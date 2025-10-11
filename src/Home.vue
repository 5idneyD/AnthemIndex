<template>
	<v-row class="gap-6" align="stretch">
		<!-- Left column: Info + Media -->
		<v-col cols="12" md="6">
			<div class="neo-card px-8 mt-14 py-6 flex flex-col overflow-auto">
				<div class="text-center">
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
			</div>
		</v-col>
		<!-- Right column: Lyrics + Suggestion -->
		<v-col cols="12" md="6" class="d-flex flex-column gap-6">
			<div class="neo-card h-50 px-8 py-6 flex flex-col flex-1 overflow-auto">
				<div>
					<h2 class="font-bold mb-4">Explore Our Rich Collection of Songs</h2>
					<p>Learn the lyrics and listen to the tunes of national anthems from all over the world!</p>
					<br />
					<p>
						Select any country from our dropdown menu at the top or try the random country suggested below!
					</p>
				</div>
			</div>
			<RandomCountry />
		</v-col>
	</v-row>
</template>
<script setup>
    import RandomCountry from './RandomCountry.vue';
	import Quiz from "./Quiz.vue";
</script>

<style scoped>
@import "./assets/styles.css";
</style>
