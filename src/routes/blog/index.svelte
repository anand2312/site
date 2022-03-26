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
  import BlogCard from '$lib/components/BlogCard.svelte';
  export let posts;
</script>

<main>
  <div class="grid grid-cols-1">
    {#each posts as post}
      <BlogCard title={post.title} date={post.date} tags={post.tags} />
    {/each}
  </div>
</main>
