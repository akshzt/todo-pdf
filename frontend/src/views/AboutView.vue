<template>
  <div class="about pa-6">
    <h1>{{heading}}</h1>
    <p>Click the below button to download a PDF of your tasks</p>
    <v-btn
      rounded
      color="primary"
      dark
      @click="getPdf"
    >
      Download PDF ⬇
    </v-btn>

  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      heading: "Downlaod PDF"
    }
  },
  methods: {
    async getPdf() {
      const response = await axios.get('/todo/file', { responseType: "arraybuffer" });

      const blob = new Blob([response.data], { type: "application/pdf" });
      const link = document.createElement("a");
      link.href = window.URL.createObjectURL(blob);
      link.download = "todo-tasks.pdf";
      link.click();
    }
  }
}
</script>
<style scoped>

</style>