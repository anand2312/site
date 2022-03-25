<script>
	let isMenuHidden = true;

	function toggleMenu() {
		isMenuHidden = !isMenuHidden;
	}
</script>

<main>
	<nav class="flex m-3 bg-pink-500">
		<h1 class="basis-3/5 font-bold text-3xl sm:text-5xl font-display py-2 m-5 sm:m-8">
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
		<div
			class="right-0 transform ease-in-out duration-300 absolute w-1/2 -translate-x-5 h-full bg-pink-500 {isMenuHidden
				? 'hidden'
				: ''} md:hidden"
		>
			<aside>
				<ul class="m-4">
					<li>
						<button on:click={toggleMenu}>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								id="Isolation_Mode"
								data-name="Isolation Mode"
								viewBox="0 0 24 24"
								width="30"
								height="30"
								class="w-4 h-4 text-dblue-500"
							>
								<path
									d="M8.127,24l9.507-9.52a3.507,3.507,0,0,0,0-4.948L8.116,0,6,2.121l9.518,9.531a.5.5,0,0,1,0,.707L6.01,21.879Z"
								/>
							</svg>
						</button>
					</li>
					<li>
						<a
							href="/about"
							class="block font-display text-2xl px-2 py-4 text-pink-50 hover:text-gold-100 transition duration-300"
							>ABOUT ME</a
						>
					</li>
					<li>
						<a
							href="/projects"
							class="block font-display text-2xl px-2 py-4 text-pink-50 hover:text-gold-100 transition duration-300"
							>PROJECTS</a
						>
					</li>
					<li>
						<a
							href="/blog"
							class="block font-display text-2xl px-2 py-4 text-pink-50 hover:text-gold-100 transition duration-300"
							>BLOG</a
						>
					</li>
				</ul>
			</aside>
		</div>
	</nav>
</main>
