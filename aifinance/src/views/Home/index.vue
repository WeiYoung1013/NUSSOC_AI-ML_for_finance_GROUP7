<script setup>
import HomeLeft from './components/left/HomeLeft.vue';
import HomeMain from './components/main/HomeMain.vue';
</script>

<template>
    <div class="common-layout">
        <el-container>
            <el-affix :offset="0">
            <el-aside class="borderLeft">
                <HomeLeft />
            </el-aside>
            </el-affix>
            <el-main class="borderMain">
                <HomeMain />
            </el-main>
        </el-container>
    </div>
</template>
<style scoped>
.borderLeft {
    width: 350px;
    background-color: rgb(255, 255, 255);
    border-right: 1px solid;
    border-color: rgb(218, 218, 218);
    height: 100vh;
    left: 0;
    position: absolute;
    display: block;
}

.borderMain {
    border-color: rgb(218, 218, 218);
    position: absolute;
    left: 350px;
    width: 800px;
}

.borderRight {
    border-color: rgb(218, 218, 218);
    position: absolute;
    left: 1150px;
    width:350px
}

</style>