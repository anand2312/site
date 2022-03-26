<script>
  import Head from '$lib/components/Head.svelte';
  import Navbar from '$lib/components/Navbar.svelte';
</script>

<main>
  <Head favicon="favicon-1.webp" title="Index" />
  <Navbar />
  <center>
    <h1 class="font-bold font-display text-pink-500 text-2xl md:text-3xl my-6">Welcome!</h1>
    <p class="font-bold font-display text-pink-50 text-xl md:text-2xl m-2 p-1">
      My name is Anand. This is my basic attempt building a website :)
    </p>
    <p class="font-bold font-display text-pink-50 text-lg md:text-2xl m-2 p-1">
      If you want to know more about me (for whatever reason), <a
        href="/about"
        class="text-lgreen-100 hover:text-pink-500">go here.</a
      >
    </p>
    <!--
    <p class="font-bold font-display text-pink-50 text-lg md:text-2xl m-2 p-1">
      I spend an ungodly amount of time watching cute kitty videos. If you want to see a few of the
      ones I like, <a href="/cute" class="text-lgreen-100 hover:text-pink-500">go here.</a>
    </p>
    -->
  </center>
</main>
