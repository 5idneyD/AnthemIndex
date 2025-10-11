<template>
	<v-app class="bg-neutral">
		<!-- Header -->
		<v-app-bar flat class="px-6 py-4 border-thick" id="header">
			<v-col cols="8" lg="7">
				<v-card-title>
					<a href="/" class="text-center">Anthem Index 🌍</a>
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
				<Home v-if="Window.location.href.endsWith('/') || Window.location.href.endsWith('/null')" />
				<Country v-else />
			</v-container>
		</v-main>
		<!-- Footer -->
		<v-footer class="border-thick" id="footer">
			<v-container class="text-center">
				<p>
					Sponsored by
					<a href="https://www.novariance.com" class="underline">No Variance.com</a>
				</p>
			</v-container>
		</v-footer>
	</v-app>
</template>
<script setup>
	import Home from "./Home.vue";
	import Country from "./Country.vue";
	import { ref, onMounted } from "vue";

	const Window = ref(window);
	const countries = ref([]);
	const selectedCountry = ref("");

	function selectCountry() {
		if (selectedCountry.value !== null) {
		window.location.href = `/${selectedCountry.value}`;
		}
	}

	onMounted(async () => {
		const res = await fetch("/api/countries");
		const data = await res.json();
		countries.value = data.map((row) => row[0]);
		const pathCountry = window.location.pathname.split("/")[1];
		if (pathCountry && countries.value.includes(pathCountry)) {
			selectedCountry.value = pathCountry;
		} else {
			selectedCountry.value = "";
		}
	});
</script>
<style scoped>
	@import "./assets/styles.css";
</style>
