<script lang="ts">
  import DropdownLanguage from "./lib/DropdownLanguage.svelte";
  import svelteLogo from "./assets/svelte.svg";
  import CodeInput from "./lib/CodeInput.svelte";
</script>

<main>
  <div class="flex flex-row w-screen h-screen">
    <div class="flex-grow flex flex-col border-r-2 border-white">
      <DropdownLanguage />
      <CodeInput />
    </div>
    <div class="w-2/6 flex-none">
      right side
    </div>
  </div>
</main>
