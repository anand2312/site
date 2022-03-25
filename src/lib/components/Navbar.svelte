<script>
	import MobileNav from '$lib/components/MobileNav.svelte';

	let isMenuHidden = true;

	function toggleMenu() {
		isMenuHidden = !isMenuHidden;
	}
</script>

<main>
	<nav class="flex m-3 bg-pink-500">
		<h1 class="basis-3/5 font-bold text-3xl sm:text-5xl font-display m-5 sm:m-8">
			<a class="text-dblue-500 hover:text-pink-50" href="/">anand2312</a>
		</h1>
		<!--Large screen nav-->
		<div class="hidden md:flex justify-evenly content-center">
			<a
				class="text-center font-display p-2.5 m-6 font-extralight text-xl sm:text-3xl text-pink-50 hover:text-gold-100"
				href="/about">ABOUT ME</a
			>
			<a
				class="text-center font-display p-2.5 m-6 font-extralight text-xl sm:text-3xl text-pink-50 hover:text-gold-100"
				href="/projects">PROJECTS</a
			>
			<a
				class="text-center font-display p-2.5 m-6 font-extralight text-xl sm:text-3xl text-pink-50 hover:text-gold-100"
				href="/blog">BLOG</a
			>
		</div>
		<!--Mobile button-->
		<!--Credit: https://www.section.io/engineering-education/creating-a-responsive-navigation-bar-using-tailwind-css-and-javascript/-->
		<div class="basis-1/5 ml-9 md:hidden flex items-center">
			<button class="outline-none" on:click={toggleMenu}>
				<svg
					class="w-8 h-8 text-dblue-500"
					x-show="!showMenu"
					fill="none"
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path d="M4 6h16M4 12h16M4 18h16" />
				</svg>
			</button>
		</div>
		<!--Mobile nav-->
		<MobileNav hidden={isMenuHidden} />
	</nav>
</main>
