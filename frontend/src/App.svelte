<script lang="ts">
  import LeftComponent from "./lib/LeftComponent.svelte";
  import RightComponent from "./lib/RightComponent.svelte";
</script>

<main>
  <div class="flex flex-row w-screen h-screen">
    <div class="flex-grow flex flex-col border-r-2 border-neutral-600">
      <LeftComponent/>
    </div>
    <div class="w-2/6 flex-none flex flex-col p-6 overflow-y-auto">
      <RightComponent/>
    </div>
  </div>
</main>
