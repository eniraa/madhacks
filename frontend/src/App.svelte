<script lang="ts">
  import LeftComponent from "./lib/LeftComponent.svelte";
</script>

<main>
  <div class="flex flex-row w-screen h-screen">
    <div class="flex-grow flex flex-col border-r-2 border-white">
      <LeftComponent/>
    </div>
    <div class="w-2/6 flex-none">
      right side
    </div>
  </div>
</main>
