<script lang="ts" setup>

import { ref } from 'vue'
const input = ref('')

</script>


<template>
    
    <div class="grid-container">
        <el-card  class="card">
            <p style="font-size: 80px;font-weight: 100;margin: 10% 15% ">生成部署</p>
            
        </el-card>
        <el-card  class="card">
            <p style="font-size: 80px;font-weight: 100;margin: 15% 0% ">执行其他脚本</p>

        </el-card>
    </div>
</template>


<style scoped>

.card{
  
  width: 300px;
  height: 300px;
  border-radius: 10%;
  background-color:rgba(255,255,255,0.6);
}
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr; /* 每列各占 1fr，即 50% 宽度 */
  gap: 20px; /* 可选，用于控制网格项之间的间距 */
}

</style>
