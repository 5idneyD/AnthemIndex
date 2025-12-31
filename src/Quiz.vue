<template>
	<v-row>
		<!-- Media player -->
		<video :src="correctAnswer[1]" @timeupdate="updateTime"></video>
        <v-col cols="12">
            <MediaButton class="px-14" />
            <v-btn @click="newQuiz" class="ml-2 my-2" id="refresh">
			    <v-icon color="#000602">mdi-refresh</v-icon>
		    </v-btn>
        </v-col>
		
	</v-row>
	<v-row>
		<!-- Quiz buttons -->
		<v-col cols="12">
			<v-row dense justify="space-between">
				<v-col
					v-for="(country, index) in quizCountries"
					:key="index"
					cols="12"
					md=""
					class="d-flex justify-center">
					<v-btn
						block
						:color="getButtonColor(country)"
						class="rounded-lg px-12  mt-2 w-75 text-truncate"
						:disabled="answered"
						@click="submitQuizAnswer(country)">
						{{ country }}
					</v-btn>
				</v-col>
			</v-row>
		</v-col>
	</v-row>
	<!-- <v-row> 
		Feedback
		<v-col cols="12">
			<v-alert
				v-if="answered"
				:type="isCorrect ? 'success' : 'error'"
				class="mt-4 pl-3"
				border="start"
				>{{
					isCorrect
						? "Correct!"
						: "Incorrect."
				}}
			</v-alert>
		</v-col>
	</v-row> -->
</template>

<script setup>
	import '@/assets/colours.css'
	import { ref, onMounted } from "vue";
	import MediaButton from "./MediaControl.vue";

	const countries = ref([]);
	let data = ref();
	const quizCountries = ref([]);
	const correctAnswer = ref([]); // [country, media]
	const answered = ref(false);
	const isCorrect = ref(false);
	const submittedAnswer = ref("");

	onMounted(async () => {
		const res = await fetch("/api/countries");
		data = await res.json();
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
		if (!answered.value) return null;

		if (country === correctAnswer.value[0]) return "success"; // highlight correct
		if (country === submittedAnswer.value) return "error"; // highlight wrong guess
		return "blue-grey-darken-4"; // fade others
	}

	function newQuiz() {
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

		answered.value = false;
	}
</script>

<style scoped>
	video {
		display: none;
	}

	#MediaControl {
		margin-left: 4%;
	}

	#refresh {
		color: white;
	}

	.v-btn {
    background-color: var(--buttonColor);
    color: var(--buttonTextColor);
	}
</style>
