<script setup>
import {onMounted} from "vue";
import axios   from "axios";

onMounted(async () => {
  console.log('HomeMain mounted')
  let stockListData =  await axios.get('http://127.0.0.1:5000/api/stockList');
  //process

})
</script>
<template>
  <el-tabs type="border-card">
    <el-tab-pane label="Top 10 market Cap ">
      这里是灵感来源与交流乐园
    </el-tab-pane>
    <el-tab-pane label="Top 10 growth amount ">
      这里是灵感来源与交流乐园
    </el-tab-pane>
    <el-tab-pane label="Top 10 growth rate ">
      这里是灵感来源与交流乐园
    </el-tab-pane>

  </el-tabs>
  <div style="height: 20px;"></div>
  <!-- 文章流 -->
  <div style="height: 15px;"></div>
</template>
  


  
