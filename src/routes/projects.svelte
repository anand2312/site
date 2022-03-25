<script lang="ts">
	import Head from '$lib/components/Head.svelte';
	import Navbar from '$lib/components/Navbar.svelte';
	import Project from '$lib/components/Project.svelte';

	let repos = [
		{
			url: 'abc.com',
			name: 'annad2312/bru',
			description: 'hi bois',
			langColor: '#F4D35E',
			langName: 'Python',
			stars: 10
		},
		{
			url: 'def.com',
			name: 'annad2312/anoter',
			description: 'wow',
			langColor: '#F4D35E',
			langName: 'Python',
			stars: 12
		}
	];
</script>

<main>
	<Head favicon="favicon-3.webp" title="Projects" />
	<Navbar />
	<div class="grid grid-cols-1 md:grid-cols-2 gap-2 m-3">
		{#each repos as repo}
			<Project {...repo} />
		{/each}
	</div>
	<p class="m-3 font-bold font-display text-pink-50 text-lg md:text-2xl p-1">
		...and more on <a href="https://anand2312.tech/r/" class="text-lgreen-100 hover:text-pink-500"
			>GitHub.</a
		>
	</p>
</main>
