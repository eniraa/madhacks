<script lang="ts">
	import { AceEditor } from "svelte-ace";
	import "brace/mode/c_cpp";
	import "brace/mode/python";
	import "brace/mode/rust";
	import "brace/mode/javascript";
	import "brace/mode/java";
	import "brace/mode/csharp";
	import "brace/theme/twilight";
	let text = "";

	export let language = "Python";
	let modes = {
		"Python": "python",
		"C++": "c_cpp",
		"C#": "csharp",
		"JavaScript": "javascript",
		"Java": "java",
		"Rust": "rust",
		"C": "c_cpp"
	}
</script>

<div class="h-2/3 border-b-2 border-gray-600">
	<AceEditor
		width='100%'
		height='100%'
		lang={modes[language]}
		theme="twilight"
		value={text} />
</div>

