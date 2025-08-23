<template>
	<v-row>
		<!-- Media player -->
		<video :src="correctAnswer[1]" @timeupdate="updateTime"></video>
		<MediaButton class="px-14 ml-3" />
	</v-row>
	<v-row>
		<!-- Quiz buttons -->
		<v-col cols="12" md="8">
			<v-row dense justify="space-between">
				<v-col
					v-for="(country, index) in quizCountries"
					:key="index"
					cols="12"
					md="4"
					class="d-flex justify-center">
					<v-btn
						block
						:color="getButtonColor(country)"
						class="rounded-lg px-12 wrap-text"
						:disabled="answered"
						@click="submitQuizAnswer(country)">
						{{ country }}
					</v-btn>
				</v-col>
			</v-row>
		</v-col>
	</v-row>
	<v-row>
		<!-- Feedback -->
		<v-col cols="12">
			<v-alert
				v-if="answered"
				:type="isCorrect ? 'success' : 'error'"
				class="mt-4"
				border="start"
				variant="tonal">
				{{
					isCorrect
						? "✅ Correct! That is " + correctAnswer[0]
						: "❌ Incorrect. The answer was " + correctAnswer[0]
				}}
			</v-alert>
		</v-col>
	</v-row>
</template>

<script setup>
	import { ref, onMounted } from "vue";
	import MediaButton from "./MediaControl.vue";

	const countries = ref([]);
	const quizCountries = ref([]);
	const correctAnswer = ref([]); // [country, media]
	const answered = ref(false);
	const isCorrect = ref(false);
	const submittedAnswer = ref("");

	onMounted(async () => {
		const res = await fetch("/api/countries");
		const data = await res.json();
		countries.value = data.map((row) => row[0]);
		let ind = 0;
		// pick 3 random unique countries
		const quizCountriesArray = new Set();
		while (quizCountriesArray.size < 3) {
			ind = Math.floor(Math.random() * data.length);
			quizCountriesArray.add(data[ind][0]);
		}

		// set correct answer (last picked from loop)
		correctAnswer.value = [data[ind][0], data[ind][2]];
		quizCountries.value = [...quizCountriesArray].sort();
	});

	function submitQuizAnswer(country) {
		submittedAnswer.value = country;
		answered.value = true;
		isCorrect.value = country === correctAnswer.value[0];
	}

	function getButtonColor(country) {
		if (!answered.value) return "grey-darken-4";

		if (country === correctAnswer.value[0]) return "success"; // highlight correct
		if (country === submittedAnswer.value) return "error"; // highlight wrong guess
		return "grey"; // fade others
	}
</script>

<style scoped>
	video {
		display: none;
	}

	#MediaControl {
		margin-left: 4%;
	}


</style>
