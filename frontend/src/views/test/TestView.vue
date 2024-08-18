<template>
  
  <h1> This is a test View</h1>
  <h1> use Flask as backend</h1>
  <h1> get data from mysql</h1>
    <div v-if="data">
      <!-- 使用数据 -->
      {{ data }}
    </div>
    <div v-else>
      Loading...
    </div>

</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        data: null,
      };
    },
    mounted() {
      axios.get('http://127.0.0.1:5000/api/data')
        .then(response => {
          this.data = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
  };
  </script>
  
  