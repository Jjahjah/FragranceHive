<script setup>
import { ref, onMounted } from 'vue'   // ref is used to create reactive variables, onMounted is a lifecycle hook that runs when the component is mounted
import axios from "axios";  // axios is used to make allow communication with backend APIs

const message = ref("");    // this means message is a reactive variable and wioll update the template when changed

defineProps({
  msg: String,
})

onMounted(() => {
  axios.get("http://127.0.0.1:8000/test/")    //axios.get makes a GET request to the specified URL from the backend
    .then(res => {                           //res is the response object returned from the backend
      message.value = res.data.message;
    })
    .catch(err => console.error(err));
});

const count = ref(0) 
</script>

<template>
  <p>{{ message }}</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
