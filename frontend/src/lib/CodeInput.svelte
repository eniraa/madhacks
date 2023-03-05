<script lang="ts">
	import { AceEditor } from "svelte-ace";
	import "brace/mode/c_cpp";
	import "brace/mode/python";
	import "brace/mode/rust";
	import "brace/mode/javascript";
	import "brace/mode/java";
	import "brace/mode/csharp";
	import "brace/theme/twilight";
	import "brace/theme/vibrant_ink";
	import "brace/theme/chaos";
	import "brace/theme/clouds_midnight";
	import "brace/theme/monokai";
	import InputInput from "./InputInput.svelte";

	let codeInput = "";

	export let language = "Python";
	export let themeMode = "Twilight";

	let modes = {
		"Python": "python",
		"C++": "c_cpp",
		"C#": "csharp",
		"JavaScript": "javascript",
		"Java": "java",
		"Rust": "rust",
		"C": "c_cpp"
	}
	let themes = {
		"Vibrant Ink": "vibrant_ink",
		"Chaos": "chaos",
		"Clouds Midnight": "clouds_midnight",
		"Twilight": "twilight",
		"Monokai": "monokai"
	}

</script>

<div class="h-2/3 border-b-2 border-neutral-600">
	<AceEditor
		bind:value={codeInput}
		width='100%'
		height='100%'
		lang={modes[language]}
		theme={themes[themeMode]}
		options={{showPrintMargin: false}}
		/>
</div>
<InputInput userCode={codeInput} userLanguage="{language}"/>

