<script lang="ts">
  const url = import.meta.env.VITE_API_URL;
  async function fetchData() {
    const res = await fetch(url);
    const data = await res.json();
    console.log(data);
  }
  fetchData();

  let name: string;
  let font_size: number;
  let font_weight: number;
  let font_family: string;
  let text_position: number;
  let image: FileList;
  let csv: FileList;

  async function postData() {
    const formData = new FormData();
    formData.append("name", name);
    formData.append("font_size", font_size.toString());
    formData.append("font_weight", font_weight.toString());
    formData.append("font_family", font_family);
    formData.append("text_position", text_position.toString());
    formData.append(
      "image",
      document.querySelector('input[type="file"]').files[0],
    );

    console.log(formData);
    const res = await fetch(url, {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    console.log(data);
  }

  async function showImage() {
    if (image.length > 0) {
      const src = URL.createObjectURL(image[0]);
      document.querySelector("#imgPreview").setAttribute("src", src);
    }
  }
</script>

<p class="text-3xl">This is home page</p>
<a href="/about" class="text-blue-600 underline">Go to about</a>
<!-- <img src="http://localhost:8000/images/05Mar24_19h25m12s.png" alt="" /> -->
<form
  on:submit|preventDefault={postData}
  class="grid grid-cols-2 w-1/3 gap-2 p-4"
>
  <label for="name">Name</label>
  <input
    type="text"
    name="name"
    id="name"
    bind:value={name}
    class="border-blue-600 border-2 rounded-md"
    required
  />
  <label for="font_size">Font size</label>
  <input
    type="number"
    name="font_size"
    id="font_size"
    bind:value={font_size}
    class="border-blue-600 border-2 rounded-md"
    required
  />
  <label for="font_weight">Font Weight</label>
  <input
    type="number"
    name="font_weight"
    id="font_weight"
    bind:value={font_weight}
    class="border-blue-600 border-2 rounded-md"
    required
  />
  <label for="font_family">Font Family</label>
  <input
    type="text"
    name="font_family"
    id="font_family"
    bind:value={font_family}
    class="border-blue-600 border-2 rounded-md"
    required
  />
  <label for="text_position">Text Position</label>
  <input
    type="number"
    name="text_position"
    id="text_position"
    bind:value={text_position}
    class="border-blue-600 border-2 rounded-md"
    required
  />
  <label for="image">Image</label>
  <input
    type="file"
    name="image"
    accept="image/*"
    bind:files={image}
    on:change={showImage}
  />
  <!-- <label for="csvFile">CSV File(name, email)</label> -->
  <!--   <input -->
  <!--     type="file" -->
  <!--     name="csv" -->
  <!--     accept="document/csv" -->
  <!--     bind:files={csv} -->
  <!--   /> -->

  <button
    type="submit"
    class="px-4 py-2 col-span-2 bg-slate-950 text-white rounded-md"
    >Submit</button
  >
</form>

<img src="" alt="" id="imgPreview" />
