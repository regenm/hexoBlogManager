<template>
    <div>
      <button @click="runScript">Run Script</button>
      <div v-if="output">
        <h3>Script Output:</h3>
        <pre>{{ output }}</pre>
      </div>
      <div v-if="error">
        <h3>Script Error:</h3>
        <pre>{{ error }}</pre>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        output: '',
        error: '',
      };
    },
    methods: {
      runScript() {
        axios.post('http://127.0.0.1:5000/run-script')
          .then(response => {
            this.output = response.data.output;
            this.error = response.data.error;
          })
          .catch(error => {
            this.error = error.message;
          });
      },
    },
  };
  </script>
  