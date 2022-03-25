<script type="ts">
	export let hidden: boolean;

	function toggleMenu() {
		hidden = !hidden;
	}
</script>

<main>
	<div
		class="right-0 transform ease-in-out duration-300 absolute w-1/2 -translate-x-5 h-full bg-pink-500 {hidden
			? 'hidden'
			: ''} md:hidden"
	>
		<aside>
			<ul class="m-3">
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
						class="block font-display text-lg px-2 py-4 text-pink-50 hover:text-gold-100 transition duration-300"
						>ABOUT ME</a
					>
				</li>
				<li>
					<a
						href="/projects"
						class="block font-display text-lg px-2 py-4 text-pink-50 hover:text-gold-100 transition duration-300"
						>PROJECTS</a
					>
				</li>
				<li>
					<a
						href="/blog"
						class="block font-display text-lg px-2 py-4 text-pink-50 hover:text-gold-100 transition duration-300"
						>BLOG</a
					>
				</li>
			</ul>
		</aside>
	</div>
</main>
