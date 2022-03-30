<script>
  // @ts-nocheck
  let favicons = ['/images/favicon-1.webp', '/images/favicon-2.webp', '/images/favicon-3.webp'];
  let random = Math.floor(Math.random() * favicons.length);

  export let favicon = favicons[random];
  export let title;
</script>

<main>
  <meta charset="utf8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="author" value="Anand" />
  <meta property="og:title" content="anand2312 {title ? '•' + title : ''}" />
  <meta property="og:description" content="Personal site and blog." />
  <meta property="og:site_name" content="anand2312" />
  <meta property="og:image" content={favicon} />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="icon" href={favicon} type="image/webp" />
  <link
    href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@100;600&display=swap"
    rel="stylesheet"
  />

  <title>anand2312 • {title}</title>
</main>
