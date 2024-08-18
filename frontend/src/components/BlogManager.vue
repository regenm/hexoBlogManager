<script lang="ts" setup>

import { ref } from 'vue'
const input = ref('')
const drawer_1 = ref(false)
const drawer_2 = ref(false)
</script>


<template>
    <div class="grid-container">
        <el-card  class="card" @click="drawer_1 = true">
            <p style="font-size: 80px;font-weight: 100;margin: 30% 15% ">ADD</p>
            
        </el-card>
        <el-drawer v-model="drawer_1" title="I am the title" :with-header="false">
            <h1>ADD</h1>
            <el-divider/>
        </el-drawer>

        <el-card  class="card" @click="drawer_2 = true">
            <p style="font-size: 80px;font-weight: 100;">DELETE</p>

        </el-card>
        <el-drawer v-model="drawer_2" title="I am the title" :with-header="false">
            <h1>DELETE</h1>
            <el-divider/>
        </el-drawer>
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
