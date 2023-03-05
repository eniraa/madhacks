<script lang="ts">
  import { Button } from "flowbite-svelte";
  export let output = "the wrong answer";
</script>

<div class="m-4 h-1/3 flex">
  <div class="flex-1 flex flex-col mr-4">
    <h2 class="text-xl mb-2">Input</h2>
    <textarea spellcheck="false"
              class="flex-grow p-4 code-input bg-neutral-800 rounded-md focus:ring-0 focus:outline-none border-2 border-neutral-500 focus:border-neutral-500"
              placeholder="Your input here..."></textarea>
    <div class="flex flex-row mt-4 items-center">
      <div class="flex-grow flex flex-row-reverse mr-4 items-center"><p class="text-sm">Ready to test?</p></div>
      <Button color="blue" size="xs">Run</Button>
    </div>
  </div>
  <div class="flex-1 ml-4 flex flex-col">
    <h2 class="text-xl mb-2">Output</h2>
    <div class="flex-grow p-4 code-input bg-neutral-800 rounded-md border-2 border-neutral-700">{output}</div>
  </div>
</div>
