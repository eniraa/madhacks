<script lang="ts">
  import { response } from "../store";
  import type { BackendResponse } from "../store";
  let resp: BackendResponse = {};
  response.subscribe((value) => resp = value);

  function bytesToSize(bytes) {
    const sizes = ['bytes', 'KB', 'MB', 'GB', 'TB']
    if (bytes === 0) return 'n/a'
    const i = parseInt(String(Math.floor(Math.log(bytes) / Math.log(1024))), 10)
    if (i === 0) return `${bytes} ${sizes[i]}`
    return `${(bytes / (1024 ** i)).toFixed(1)} ${sizes[i]}`
  }
</script>

<h2 class="text-xl mb-2">Feedback</h2>
<hr class="border-neutral-600 mb-4 overflow-y-auto">
{#if JSON.stringify(resp) === "{}"}
  <p class="flex-grow justify-center items-center flex text-md leading-snug text-gray-400">Run something for feedback!</p>
{:else}
  {#if resp.success === false}
    <p class="text-red-500 text-md leading-snug">Code did not run successfully.</p>
  {:else}
    <h3 class="text-lg text-gray-300">Memory Usage</h3>
    <p class="text-sm text-neutral-400 leading-snug mb-4">{bytesToSize(resp.memory)}</p>
    <h3 class="text-lg text-gray-300">Runtime</h3>
    <p class="text-sm text-neutral-400 leading-snug mb-4">{(resp.time * 1000).toFixed(3)}ms</p>
    <h3 class="text-lg text-gray-300 mb-2">Line Coverage</h3>
    <div class="overflow-x-auto bg-neutral-900 border-neutral-700 border-2 mb-4 p-2 min-h-[16rem]">
      <pre class="text-sm text-neutral-400 leading-snug">{resp.coverage}</pre>
    </div>

    {#if resp.analysis}
      <h3 class="text-lg text-gray-300">Complexity Analysis</h3>
      <p class="text-sm text-neutral-400 leading-snug mb-4">{@html resp.analysis.replaceAll("\n", "<br>")}</p>
    {/if}
  {/if}
{/if}
