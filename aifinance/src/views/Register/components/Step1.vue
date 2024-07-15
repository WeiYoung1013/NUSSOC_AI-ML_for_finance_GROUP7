<!-- 步骤一 -->
<script setup>
import { TopRight, MagicStick } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router';
const router = useRouter();

const nextStep=()=>{
  router.push({
    path: '/register/2'
  })
}
</script>

<template>
    <div style="display: flex;flex-direction: column;justify-content: center;align-items: center;">
        <h1 style="margin-top: 70px;margin-bottom: 10px;">欢迎在此相聚</h1>
        <el-tag effect="dark" round type="success">步骤1 账户与密码</el-tag>
        <el-card class="box-card">

            <div>
                <!-- 账号 -->
                <el-input class="input" placeholder="创建你的账号名">
                    <template #prepend>
                        <el-icon>
                            <TopRight />
                        </el-icon>
                    </template>
                </el-input>
                <!-- 密码 -->
                <el-input class="input" show-password placeholder="设置你的密码">
                    <template #prepend>
                        <el-icon>
                            <TopRight />
                        </el-icon>
                    </template>
                </el-input>
                <!-- 验证码 -->
                <div style="margin-top: 5px;">
                    <!-- 验证码图片 -->
                </div>

                <!-- 下一步 -->
                <div style="text-align:center;margin-top: 40px;">
                    <el-button-group>
                        <el-button type="primary" @click="nextStep" size="large">下一步
                            <el-icon style="margin-left: 10px;" size="20">
                                <MagicStick />
                            </el-icon>
                        </el-button>
                    </el-button-group>
                </div>
            </div>
        </el-card>
    </div>
</template>

<style scoped>
.input {
    margin-top: 25px;
    height: 38px;
    width: 100%;
}

.box-card {
    margin-top: 10px;
    margin-left: 0;
    width: 340px;
    height: 410px;
    border-radius: 15px;
}
</style>