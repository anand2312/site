<script lang="ts">
  export let title: string;
  export let date: string;
  export let tags: string[];

  let slug = `${date}-${title}`;
</script>

<main>
  <div class="border-2 border-solid rounded-lg border-lgreen-50 m-2 p-3 font-display">
    <a href="/blog/{slug}" class="my-2 mx-1 text-pink-500 hover:text-gold-100 font-bold text-xl"
      >{title}</a
    >
    <p class="m-1 text-pink-50 text-lg">{date}</p>
    <!--TODO: render tags-->
  </div>
</main>
