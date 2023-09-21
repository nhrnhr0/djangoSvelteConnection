<script>
import { onMount } from "svelte";
let names;
let entered_name = "";
function save_name() {
  fetch("http://127.0.0.1:8000/my-api/add-name/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name: entered_name }),
  })
    .then((response) => response.json())
    .then((data) => {
      // we are setting the names to the names variable
      names = data;
      entered_name = "";
    });
}
onMount(() => {
  // we are fetching all the names from 127.0.0.1:8000/my-api/name
  fetch("http://127.0.0.1:8000/my-api/name/")
    .then((response) => response.json())
    .then((data) => {
      // we are setting the names to the names variable
      names = data;
    });
});
</script>

{#if names}
  {#each names as name}
    <p>{name.name}</p>
  {/each}
{/if}

<input type="text" bind:value={entered_name} placeholder="Enter your name" />
<button on:click={save_name}>Submit</button>
