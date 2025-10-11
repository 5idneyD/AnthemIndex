<template>
	<div class="neo-card mt-6 px-12 py-8" style="min-height: 150px">
		<h3 class="font-bold mb-8">Why don't you try this one:</h3>
		<a :href="'/' + randomCountry" class="mt-2">
			<img :src="randomCountryFlag" alt="flag" />
			<span class="ml-8">{{ randomCountry }}</span>
		</a>
	</div>
</template>
<script setup>
	import { ref, onMounted } from "vue";
	const randomCountry = ref("");
	const randomCountryFlag = ref("");
	const countries = ref([]);

	onMounted(async () => {
		const res = await fetch("/api/countries");
		const data = await res.json();
		countries.value = data.map((row) => row[0]);
		let ind = [Math.floor(Math.random() * data.length)];
		randomCountry.value = data[ind][0];
		randomCountryFlag.value = data[ind][1];
	});
</script>

<style scoped>
span {
	color: var(--buttonColor);
}

a {
	text-decoration: none;
}
</style>
