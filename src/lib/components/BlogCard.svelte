<script lang="ts">
  import { DateTime } from 'luxon';
  import Tag from '$lib/components/Tag.svelte';

  export let title: string;
  export let date: DateTime;
  export let tags: string[];
  export let slug: string;
</script>

<main>
  <div class="border-2 border-solid rounded-lg border-lgreen-50 m-3 p-3 font-display">
    <a href="/blog/{slug}" class="my-2 mx-1 text-pink-500 hover:text-gold-100 font-bold text-xl"
      >{title}</a
    >
    <p class="m-1 text-pink-50 text-lg"><i>on {date.toLocaleString(DateTime.DATE_MED)}</i></p>
    <span class="flex-row flex">
      {#each tags as tag}
        <Tag name={tag} />
      {/each}
    </span>
  </div>
</main>
