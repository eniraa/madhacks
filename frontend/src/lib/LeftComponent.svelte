<script lang="js">
    import { Button, Dropdown, DropdownItem, Chevron } from "flowbite-svelte";
    import CodeInput from "./CodeInput.svelte";

    export let language = "Python";
    let langs = ["Python", "Java", "JavaScript", "Rust", "C", "C++", "C#"];
    let text = "";

    let dropdownOpen = false;
</script>

<div class="flex items-center mx-4 h-16">
    <div class="flex-grow">
        <h1 class="text-xl">Code Analyzer</h1>
    </div>
    <div class="flex-none relative">
        <Button color="blue" size="xs"><Chevron>{language}</Chevron></Button>
        <Dropdown class="py-1 w-24" bind:open={dropdownOpen}>
            {#each langs as lang}
                <DropdownItem on:click={() => {
                    language = lang;
                    dropdownOpen = false;
                }}>{lang}</DropdownItem>
            {/each}
        </Dropdown>
    </div>
</div>
<CodeInput language={language} />

