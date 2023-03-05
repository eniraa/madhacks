<script lang="ts">
  import { response } from "../store";
  import type { BackendResponse } from "../store";
  let resp: BackendResponse = {};
  response.subscribe((value) => resp = value);

  function bytesToSize(bytes) {
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB']
    if (bytes === 0) return 'n/a'
    const i = parseInt(String(Math.floor(Math.log(bytes) / Math.log(1024))), 10)
    if (i === 0) return `${bytes} ${sizes[i]}`
    return `${(bytes / (1024 ** i)).toFixed(1)} ${sizes[i]}`
  }
</script>

<h2 class="text-xl mb-2">Feedback</h2>
<hr class="border-neutral-600 mb-4">
{#if resp === {}}
  <p class="text-md leading-snug text-gray-400">Run something for feedback!</p>
{:else}
  {#if !resp.success}
    <p class="text-red-500 text-md leading-snug">Code did not run successfully.</p>
  {:else}
    <h3 class="text-lg text-gray-300">Memory Usage</h3>
    <p class="text-sm text-neutral-400 leading-snug mb-4">{bytesToSize(resp.memory)}</p>
    <h3 class="text-lg text-gray-300">Runtime</h3>
    <p class="text-sm text-neutral-400 leading-snug mb-4">{(resp.time * 1000).toFixed(3)}ms</p>
    <h3 class="text-lg text-gray-300">Line Coverage</h3>
    <p class="text-sm text-neutral-400 leading-snug mb-4">{resp.coverage}ms</p>
    {#if resp.analysis}
      <h3 class="text-lg text-gray-300">Complexity Analysis</h3>
      <p class="text-sm text-neutral-400 leading-snug mb-4">{resp.analysis}</p>
    {/if}
  {/if}
{/if}
