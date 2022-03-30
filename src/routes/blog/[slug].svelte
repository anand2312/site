<script context="module">
  export async function load({ fetch, params }) {
    const response = await fetch(`/blog/${params.slug}.json`);
    const data = await response.json();

    return {
      status: response.status,
      props: {
        html: data.html,
        metadata: data.data
      }
    };
  }
</script>

<script>
  import { DateTime } from 'luxon';
  import Head from '$lib/components/Head.svelte';
  import Navbar from '$lib/components/Navbar.svelte';
  import Tag from '$lib/components/Tag.svelte';

  export let html;
  export let metadata;

  let date = DateTime.fromSQL(metadata.date);
</script>

<main>
  <Head title={metadata.title} />
  <Navbar />
  <div class="mx-7 my-5">
    <h1 class="font-bold font-display text-pink-500 text-2xl underline decoration-1 md:text-3xl">
      {metadata.title}
    </h1>
    <p class="font-light font-display text-pink-50 my-2 mx-2 text-sm md:text-lg">
      Written on: {date.toLocaleString(DateTime.DATE_HUGE)}
    </p>
    <span class="flex flex-row mx-2 mb-4">
      <p class="font-display text-pink-50 text-sm md:text-lg">Tags:</p>
      {#each metadata.tags as tag}
        <Tag name={tag} />
      {/each}
    </span>
    <hr />
  </div>
  <div class="mx-7 my-5">
    {@html html}
  </div>
</main>

<style lang="postcss">
  div :global(.content) {
    @apply font-bold font-display text-pink-50 text-lg md:text-xl my-3;
  }
  div :global(.heading) {
    @apply font-bold font-display text-pink-500 my-6;
  }
  div :global(h1) {
    @apply text-xl md:text-2xl;
  }
  div :global(h2) {
    @apply text-lg md:text-xl;
  }
</style>
