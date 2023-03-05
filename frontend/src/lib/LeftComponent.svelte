<script lang="js">
    import { Button, Dropdown, DropdownItem, Chevron } from "flowbite-svelte";
    import CodeInput from "./CodeInput.svelte";

    export let language = "Python";
    export let themeMode = "Twilight";
    let langs = ["Python", "Java", "JavaScript", "Rust", "C", "C++", "C#"];
    let themes = ["Vibrant Ink","Chaos","Clouds Midnight","Twilight","Monokai"];
    let text = "";
    let dropdownOpen = false;
    let themeDropdown = false;
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
        <Button color="blue" size="xs"><Chevron>{themeMode}</Chevron></Button>
        <Dropdown class="py-1 w-40" bind:open={themeDropdown}>
            {#each themes as theme}
                <DropdownItem on:click={() => {
                    themeMode = theme
                    themeDropdown = false;
                }}>{theme}</DropdownItem>
            {/each}
        </Dropdown>
    </div>
</div>
<CodeInput language={language} themeMode={themeMode} />

