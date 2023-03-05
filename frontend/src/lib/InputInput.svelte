<script lang="ts">
  import { Button, Spinner } from "flowbite-svelte";

  export let output = "the wrong answer";
  export let label = "Ready to test?"
  export let buttonLabel = "Run";

  export let showSpinner = false;
  function runCode() {
    label = "Running...";
    showSpinner = true;
    let userInput = document.getElementById("input-code-text").textContent;
    doPost();
  }

  async function doPost () {
    fetch("http://127.0.0.1:5000/execute", {

      method: "POST",

      body: JSON.stringify({
      code: "print('hello world')",
      language: "py",
      inputs: "…"
      }),

      headers: {
        "Content-type": "application/json"
      }
    })
      .then(response => response.json())
      .then(response => output = JSON.stringify(response))
  }
</script>

<div class="m-4 h-1/3 flex">
  <div class="flex-1 flex flex-col mr-4">
    <h2 class="text-xl mb-2">Input&nbsp;&nbsp;<span class="text-xs text-neutral-400"> (this gets fed to stdin)</span></h2>

    <!--    Form -->
    <textarea
              id="input-code-text"
              spellcheck="false"
              class="flex-grow p-4 code-input bg-neutral-800 rounded-md focus:ring-0 focus:outline-none border-2 border-neutral-500 focus:border-neutral-500"
              placeholder="Your input here..."></textarea>
    <div class="flex flex-row mt-4 items-center">
      <div class="flex-grow flex flex-row-reverse mr-4 items-center"><p class="text-sm">{label}</p></div>
      {#if showSpinner}
       <Spinner class="mr-4" id="spinner" size={4} />
      {/if}
      <!--submit button -->
      <Button color="blue" disabled={showSpinner} size="xs" on:click={() => runCode()}>{buttonLabel}</Button>
    </div>
  </div>
  <div class="flex-1 ml-4 flex flex-col">
    <h2 class="text-xl mb-2">Output&nbsp;&nbsp;<span class="text-xs text-neutral-400"> (stdout)</span></h2>
    <div class="flex-grow p-4 code-input bg-neutral-800 rounded-md border-2 border-neutral-700">{output}</div>
  </div>
</div>
