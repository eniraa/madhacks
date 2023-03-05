<script lang="ts">
  import LeftComponent from "./lib/LeftComponent.svelte";
  import InputInput from "./lib/InputInput.svelte";
</script>

<main>
  <div class="flex flex-row w-screen h-screen">
    <div class="flex-grow flex flex-col border-r-2 border-gray-600">
      <LeftComponent/>
      <InputInput/>
    </div>
    <div class="w-2/6 flex-none flex flex-col p-6">
      <h2 class="text-xl mb-2">Feedback</h2>
      <p class="text-md leading-snug text-gray-400">Wow your code sucks</p>
    </div>
  </div>
</main>
