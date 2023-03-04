<script lang="js">
    import {Button, Dropdown, DropdownItem} from 'flowbite-svelte'
    import { AceEditor } from "svelte-ace";
    import "brace/mode/c_cpp";
    import "brace/mode/python";
    import "brace/theme/twilight";
    export let language = "Select a language";
    let langs = ["Python", "Java", "Javascript", "Rust", "C", "C++", "C#"];
    let modes = {
        "Python": "python",
        "C++": "c_cpp",
    }
    let text = "";
</script>

<Button color="black">{language}</Button>
<Dropdown>
    {#each langs as lang}
        <DropdownItem class="w-1/2" on:click={() => language = lang}>{lang}</DropdownItem>
    {/each}
</Dropdown>
<AceEditor
        width='100%'
        height='100%'
        lang={modes[language]}
        theme="twilight"
        value={text} />

