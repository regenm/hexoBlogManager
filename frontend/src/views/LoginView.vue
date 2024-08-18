<script lang="ts" setup>
import { ref } from 'vue'
const input = ref('')
</script>

<template>
  <div class="background" >
    <el-card  class="card">
      <h2>Login</h2>
      <el-divider />
      
      <el-input
      v-model="input"
      style="width: 240px"
      type="password"
      placeholder="Magic Spell"
      show-password
      clearable
    />

          
    </el-card>
  </div>
</template>


<style  scoped>
.background{
  
  
  background:url("../assets/1.jpg");
  width:100%;			
  height:100%;			
  position:fixed;
  background-size:100% 100%;
  
}
.card{
  position:absolute ;left: 40%; top: 30%;
  width: 300px;
  height: 300px;
  border-radius: 10%;
  background-color:rgba(255,255,255,0.6);
}
</style>
