<!-- 页头组件 -->
<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router';
const code = ref(localStorage.getItem('code'))
const user = ref(localStorage.getItem('user'))
const router = useRouter();
const activeIndex = ref('1');
const handleSelect = ((key: string, keyPath: string[]) => {
  console.log(key, keyPath)
  if (key === '0') {
    router.push({
      path: '/'
    })
  }
  if (key === '2') {
    router.push({
      path: '/login'
    })
  }
  if (key == '2-1') {
    router.push({
      path: '/userHome'
    })
  }
  if (key == '2-3') {
  //清除数据恢复默认
  localStorage.clear()
  router.push({
    path: '/'
  })
}
}
)

</script>

<template>
  <!-- 主导航栏 -->
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false" @select="handleSelect">
    <el-menu-item index="0">Home page</el-menu-item>
    <div class="flex-grow" />
    <!-- 副导航栏 -->
    <el-menu-item index="2" v-if="code != 0">login for more function</el-menu-item>
    <el-sub-menu index="3" v-else>
      <!-- 用户信息 -->
      <template #title>hi,{{ user }}</template>
      <el-menu-item index="2-1">My backtest</el-menu-item>
      <el-menu-item index="2-3">Log out</el-menu-item>
    </el-sub-menu>


  </el-menu>
</template>

<style>
.flex-grow {
  flex-grow: 1;
}
</style>
