<script lang="js">
    import { Button, Dropdown, DropdownItem } from "flowbite-svelte";
    import CodeInput from "./CodeInput.svelte";

    export let language = "Python";
    let langs = ["Python", "Java", "JavaScript", "Rust", "C", "C++", "C#"];
    let text = "";
</script>

<Button color="black">{language}</Button>
<Dropdown>
    {#each langs as lang}
        <DropdownItem class="w-1/2" on:click={() => language = lang}>{lang}</DropdownItem>
    {/each}
</Dropdown>
<CodeInput language={language} />

