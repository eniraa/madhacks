<script lang="js">
  import {Button, Dropdown, DropdownItem} from 'flowbite-svelte'
  let selectedLanguage = "Select a language";
  let langs = ["Python", "Java", "Javascript", "Rust", "C", "C++", "C#"];
</script>

<Button color="blue">{selectedLanguage}</Button>
<Dropdown id="dropdown">
    {#each langs as lang}
      <DropdownItem on:click={() => selectedLanguage = lang}>{lang}</DropdownItem>
    {/each}
</Dropdown>

