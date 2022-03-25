<script context="module">
  export function load({ error, status }) {
    return {
      props: {
        title: `${status}: ${error.message}`
      }
    };
  }
</script>

<script>
  import Navbar from '$lib/components/Navbar.svelte';

  export let title;
</script>

<main>
  <Navbar />
  <center class="flex flex-row justify-center content-center">
    <h1 class="font-bold py-56 font-display text-pink-50 text-2xl md:text-4xl m-2 p-1">{title}</h1>
    <img
      src="favicon-1.webp"
      class="py-40 md:py-0 w-1/3 h-1/3 md:w-2/4 md:h-2/3"
      alt="sad cat as you've reached an error page"
      type="image/webp"
    />
  </center>
</main>
