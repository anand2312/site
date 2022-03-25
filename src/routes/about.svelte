<script>
	import Head from '$lib/components/Head.svelte';
	import Navbar from '$lib/components/Navbar.svelte';

	let today = new Date();
	let bday = new Date(2002, 11, 23);
	// @ts-ignore
	let diff = today - bday;
	let years = Math.floor(diff / (1000 * 60 * 60 * 24 * 365));
</script>

<main>
	<Head favicon="favicon-2.webp" title="About" />
	<Navbar />

	<center>
		<h1 class="font-bold font-display text-pink-500 text-2xl md:text-3xl my-6">About Me</h1>
		<p class="font-bold font-display text-pink-50 text-xl md:text-2xl m-2 p-1">
			My name is Anand, I'm a {years} year old programmer. I am a Computer Science Engineering student
			at NIT Allahabad.
		</p>
		<p class="font-bold font-display text-pink-50 text-lg md:text-2xl m-2 p-1">
			Currently I'm mostly interested in <em>databases</em> and <em>concurrency</em>.
		</p>
		<p class="font-bold font-display text-pink-50 text-lg md:text-2xl m-2 p-1">
			I also try to learn some <em>DevOps</em> and
			<em><a href="https://rust-lang.org" class="text-lgreen-100 hover:text-pink-500">Rust</a></em>,
			but I'm not very good at those 😅.
		</p>
		<p class="font-bold font-display text-pink-50 text-lg md:text-2xl m-2 p-1">
			You can find me hanging out in the <a
				href="https://discord.gg/python"
				class="text-lgreen-100 hover:text-pink-500">Python Discord server</a
			>
			in the <em>databases</em> or <em>web development</em> channels. My username is
			<em>anand#8837</em>.
		</p>
		<br />

		<p class="font-bold font-display text-pink-50 text-lg md:text-2xl m-2 p-1">
			If you want to see some of my projects, <a
				href="/projects"
				class="text-lgreen-100 hover:text-pink-500">go here.</a
			>
			<br /><br />
			I'll <i>try</i> to blog <a href="/blog" class="text-lgreen-100 hover:text-pink-500">here.</a>
		</p>

		<h2 class="font-bold font-display text-pink-500 text-xl md:text-2xl my-1">Contact</h2>
		<ul class="font-bold font-display text-pink-50">
			<li>
				<a href="https://anand2312.tech/r/" class="text-lgreen-100 hover:text-pink-500">GitHub</a>
			</li>
			<li>
				<a
					href="https://discord.com/users/271586885346918400"
					class="text-lgreen-100 hover:text-pink-500">Discord - anand#8837</a
				>
			</li>
			<li>Gitter</li>
		</ul>
	</center>
</main>

<style>
	em {
		color: #8cbcb9;
	}
</style>
