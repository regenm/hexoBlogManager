<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();

const toComponentMethod = (subpath) => {
  router.push({ path: '/main' + subpath });
}
</script>


<template>
  <div class="common-layout">
    <el-container>
      <div class="header">
        <el-header ><h1 style="color: aqua; font-size: 20px; position: absolute;">Blog Manager V1.0</h1></el-header>
      
      <el-container>
        <el-aside width="200px">
      <el-scrollbar>
        <el-menu >
          <el-sub-menu index="1" @click="toComponentMethod('/bloginfo')">
            <template #title>
              博客信息
            </template>
            
            
            
          </el-sub-menu>
          <el-sub-menu index="2" @click="toComponentMethod('/blogmanager')">
            <template #title>
              管理博客
            </template>
            
            
          </el-sub-menu>
          <el-sub-menu index="3" @click="toComponentMethod('/blogscript')" >
            <template #title>
              执行
            </template>
            
          </el-sub-menu>
        </el-menu>
      </el-scrollbar>
    </el-aside>

        <el-main>
          <RouterView/>
        </el-main>
      </el-container>
      </div>
    </el-container>
  </div>
</template>

<style scoped>
.header{
  background:url("../assets/1.jpg");
  width:100%;			
  height:8%;			
  position:fixed;
  background-size:100% 100%;
}

</style>