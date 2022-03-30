<script context="module">
  export async function load({ fetch }) {
    const response = await fetch('/blog.json');
    const data = await response.json();

    return {
      status: response.status,
      props: {
        posts: data.posts
      }
    };
  }
</script>

<script>
  import { DateTime } from 'luxon';
  import Head from '$lib/components/Head.svelte';
  import Navbar from '$lib/components/Navbar.svelte';
  import BlogCard from '$lib/components/BlogCard.svelte';

  export let posts;
</script>

<main>
  <Head favicon="images/favicon-1.webp" title="Blog" />
  <Navbar />

  <div class="grid grid-cols-1">
    {#each posts as post}
      <BlogCard
        title={post.title}
        date={DateTime.fromSQL(post.date)}
        tags={post.tags}
        slug={post.slug}
      />
    {/each}
  </div>
</main>
