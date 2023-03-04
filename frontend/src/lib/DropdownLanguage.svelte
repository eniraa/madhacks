<script lang="js">
  import {Button, Dropdown, DropdownItem} from 'flowbite-svelte'
  export let language = "Python";
  let langs = ["Python", "Java", "Javascript", "Rust", "C", "C++", "C#"];
</script>

<Button color="blue">{language}</Button>
<Dropdown id="dropdown" class="w-fit">
    {#each langs as lang}
      <DropdownItem class="w-1/2" on:click={() => language = lang}>{lang}</DropdownItem>
    {/each}
</Dropdown>

