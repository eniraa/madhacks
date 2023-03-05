<script lang="ts">
  import { Button, Spinner, Checkbox } from "flowbite-svelte";
  import { response } from '../store';

  let output = ""
  let success = true
  let error = ""
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

  export let showSpinner = false;

  response.subscribe((value) => {
    output = value.output;
    success = value.success;
    error = value.error;
  });

  let runAnalysis = false;
  function runCode() {
    label = "Running...";
    showSpinner = true;

    fetch("http://127.0.0.1:5000/execute", {
      method: "POST",
      body: JSON.stringify({
        code: userCode,
        language: fileExtension[userLanguage],
        inputs: userInputs,
        analysis: runAnalysis
      }),

      headers: {
        "Content-type": "application/json"
      }
    })
      .then(resp => resp.json())
      .then(resp => {
        response.set(resp);
      })
      .then(toggleLabels);
  }

  function toggleLabels(){
    showSpinner = !showSpinner;
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
      <div class="flex-grow">
        <Checkbox disabled={showSpinner} bind:checked={runAnalysis}>Run time complexity analysis</Checkbox>
      </div>
      <div class="flex-none flex flex-row-reverse mr-4 items-center"><p class="text-sm">{label}</p></div>
      {#if showSpinner}
       <Spinner class="mr-4" id="spinner" size={4} />
      {/if}
      <Button color="blue" disabled={showSpinner} size="xs" on:click={() => {runCode();}}>{buttonLabel}</Button>
    </div>
  </div>
  <div class="flex-1 ml-4 flex flex-col">
    <h2 class="text-xl mb-2">Output&nbsp;&nbsp;<span class="text-xs text-neutral-400"> (stdout)</span></h2>
    <div class={`${success ? "" : "text-red-500" } flex-grow p-4 overflow-y-auto code-input bg-neutral-800 rounded-md border-2 border-neutral-700`}>
      <pre>{success ? (output ?? "") : (error ?? "")}</pre>
    </div>
  </div>
</div>
