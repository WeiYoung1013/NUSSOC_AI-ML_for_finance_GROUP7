<script setup>

// eslint-disable-next-line no-unused-vars
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router';

// 获取登陆数据

const code = ref(999);

//跳转登录页
const router = useRouter();
const ToBackTest = () => {
    if (localStorage.getItem('code')) {
        router.push({
            path: '/editor',
            query: {
                modify: 0
            }
        })
    } else {
        router.push({
            path: '/login'
        })
    }
}

const articleList = ref([])
onMounted: {
    // code.value = account.code
    // 获取后端数据
    // getUserArticleList().then(res => {
    //     articleList.value = res.data.pageInfo.list;
    // });
    articleList.value = [{
        title: 'Linux入门'
    },
    {
        title: '前端实现分页'
    },
    {
        title: '部署vue项目'
    },
    ]
}
</script>

<template>
    <div>
        <div style="height: 30px;"></div>
        <el-row>

            <el-col class="row" :span="8">
                <el-button type="success" @click="ToBackTest">BackTest+</el-button>
            </el-col>
        </el-row>
        <div style="height: 10px;"></div>
        <!-- 显示一些状态 -->
        <div style="height: 20px;"></div>
        <el-text class="title">Stock List</el-text>
        <el-card shadow="hover" class="card">
            <h3>Stock1.....</h3>
            <h4>some info</h4>
        </el-card>
    </div>
</template>

<style scoped>
.row {
    display: flex;
    align-items: center;
    justify-content: center;
}

.title {
    font-size: 18px;
    font-weight: bolder;
    color: #000;
    padding-left: 25px;
}

.card {
    margin-top: 10px;
    margin-left: 25px;
    margin-right: 25px;
}

.text {
    margin-left: 25px;
    width: 300px;
}
</style>


  
  