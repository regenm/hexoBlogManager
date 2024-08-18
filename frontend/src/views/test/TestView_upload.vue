<template>
    <div>
      <form @submit.prevent="uploadFile">
        <input type="file" @change="handleFileUpload">
        <button type="submit">Upload</button>
      </form>
      <!-- 文件上传按钮以及选框 -->
    </div>
  
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        file: null
      };
    },
    methods: {
      handleFileUpload(event) {
        this.file = event.target.files[0];
      },
      uploadFile() {
        const formData = new FormData();
        formData.append('file', this.file);
        //向后端发送POST
        axios.post('http://127.0.0.1:5000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
      }
    }
  };
  </script>
  