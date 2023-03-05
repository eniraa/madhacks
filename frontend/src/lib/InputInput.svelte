<script lang="ts">
  import { Button, Spinner } from "flowbite-svelte";

  export let output = [];
  export let label = "Ready to test?";
  export let buttonLabel = "Run";
  export let userCode = "";
  export let userInputs = "";
  export let userLanguage = "";
  let fileExtension = {
    "Python": "py",
    "C++": "c",
    "C#": "cs",
    "JavaScript": "js",
    "Java": "java",
    "Rust": "rs",
    "C": "c"
  }
  let response;

  export let showSpinner = false;

  function runCode() {
    label = "Running...";
    showSpinner = true;

    fetch("http://127.0.0.1:5000/execute", {
      method: "POST",
      body: JSON.stringify({
        code: userCode,
        language: fileExtension[userLanguage],
        inputs: userInputs
      }),

      headers: {
        "Content-type": "application/json"
      }
    })
      .then(response => response.json())
      .then(response => {
        output = [];
        Object.entries(response).forEach(([key,value]) => {
          switch (key) {
            case "Memory":
              output.push(key + ": " + bytesToSize(value));
              break;
            case "Time":
              output.push(key + ": " + value + " seconds");
              break;
            default:
              output.push(key + ": " + value);
          }
        })
      })
      .then(toggleLabels);
  }

  function bytesToSize(bytes) {
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB']
    if (bytes === 0) return 'n/a'
    const i = parseInt(String(Math.floor(Math.log(bytes) / Math.log(1024))), 10)
    if (i === 0) return `${bytes} ${sizes[i]}`
    return `${(bytes / (1024 ** i)).toFixed(1)} ${sizes[i]}`
  }

  function toggleLabels(){
    showSpinner = showSpinner !== true;
    if (label != "Ready to test?") {
      label = "Ready to test?";
    } else {
      label = "Running...";
    }
  }
</script>

<div class="m-4 h-1/3 flex">
  <div class="flex-1 flex flex-col mr-4">
    <h2 class="text-xl mb-2">Input&nbsp;&nbsp;<span class="text-xs text-neutral-400">(stdin)</span></h2>

    <textarea
              bind:value={userInputs}
              spellcheck="false"
              class="flex-grow p-4 code-input bg-neutral-800 rounded-md focus:ring-0 focus:outline-none border-2 border-neutral-500 focus:border-neutral-500"
              placeholder="Your input here..."></textarea>
    <div class="flex flex-row mt-4 items-center">
      <div class="flex-grow flex flex-row-reverse mr-4 items-center"><p class="text-sm">{label}</p></div>
      {#if showSpinner}
       <Spinner class="mr-4" id="spinner" size={4} />
      {/if}
      <Button color="blue" disabled={showSpinner} size="xs" on:click={() => {runCode();}}>{buttonLabel}</Button>
    </div>
  </div>
  <div class="flex-1 ml-4 flex flex-col">
    <h2 class="text-xl mb-2">Output&nbsp;&nbsp;<span class="text-xs text-neutral-400"> (stdout)</span></h2>
    <div class="flex-grow p-4 code-input bg-neutral-800 rounded-md border-2 border-neutral-700">
      {#each output as field}
        {field}
        <br><br>
      {/each}
    </div>
  </div>
</div>
