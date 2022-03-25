<script context="module">
  export async function load({ params, fetch, session, stuff }) {
    const url = 'https://site-backend-api.an23.workers.dev/pinned';
    const response = await fetch(url);
    const data = parseResponse(await response.json());

    return {
      status: response.status,
      props: {
        repos: data
      }
    };
  }

  function parseResponse(res) {
    let data = res['data'];
    let out = new Array();

    for (const repo of data) {
      out.push({
        url: repo.url,
        name: repo.nameWithOwner,
        description: repo.description,
        langColor: repo.primaryLanguage.color,
        langName: repo.primaryLanguage.name,
        stars: repo.stargazerCount
      });
    }
    return out;
  }
</script>

<script lang="ts">
  import Head from '$lib/components/Head.svelte';
  import Navbar from '$lib/components/Navbar.svelte';
  import Project from '$lib/components/Project.svelte';

  interface Repo {
    url: string;
    name: string;
    description: string;
    langColor: string;
    langName: string;
    stars: number;
  }

  export let repos: Array<Repo>;
</script>

<main>
  <Head favicon="favicon-3.webp" title="Projects" />
  <Navbar />
  <center>
    <p class="font-bold font-display text-pink-50 text-lg md:text-2xl mx-3 my-4 p-1">
      Here are some of the projects I've worked on; these are the repositories that are pinned on my
      GitHub profile.
    </p>
  </center>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-2 m-3">
    {#each repos as repo}
      <Project {...repo} />
    {/each}
  </div>
  <center>
    <p class="m-3 font-bold font-display text-pink-50 text-lg md:text-2xl p-1">
      ...and more on <a href="https://anand2312.tech/r/" class="text-lgreen-100 hover:text-pink-500"
        >GitHub.</a
      >
    </p>
  </center>
</main>
