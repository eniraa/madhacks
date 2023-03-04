<script lang="ts">
	import { AceEditor } from "svelte-ace";
	import "brace/mode/c_cpp";
	import "brace/mode/python";
	import "brace/theme/twilight";
	let text = "";

	export let language = "Python";
	let modes = {
		"Python": "python",
		"C++": "c_cpp",
	}
</script>

<AceEditor
	width='100%'
	height='100%'
	lang={modes[language]}
	theme="twilight"
	value={text} />
