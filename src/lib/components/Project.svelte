<script lang="ts">
  export let url: string;
  export let name: string;
  export let description: string;
  export let langColor: string;
  export let langName: string;
  export let stars: number;
</script>

<main>
  <div class="border-2 border-solid rounded-lg border-lgreen-50 m-2 p-3 font-display">
    <a href={url} class="my-2 mx-1 text-pink-500 hover:text-gold-100 font-bold text-xl">{name}</a>
    <p class="m-1 text-pink-50 text-lg">{description}</p>
    <div class="flex">
      <span class="dot" style="background-color: {langColor};" />
      <p class="m-0.5 py-3 text-pink-50 text-lg">{langName}</p>
      <img src="star.svg" class="star" alt="Star" />
      <p class="m-0.5 py-3 text-pink-50 text-lg">{stars}</p>
    </div>
  </div>
</main>

<style>
  .dot {
    margin-top: 1em;
    margin-bottom: 1em;
    margin-right: 1em;
    margin-left: 0%;
    height: 1.5em;
    width: 1.5em;
    border-radius: 50%;
  }

  .star {
    margin: 1em;
    height: 1.5em;
    width: 1.5em;
  }
</style>
