<script setup>
import LayoutHeader from '../Layout/components/LayoutHeader.vue';
import { useRouter } from 'vue-router';
// 引入图标
import { TopRight, MagicStick } from '@element-plus/icons-vue'
import { onMounted, ref } from 'vue';

// 使用路由
const router = useRouter();
// 跳转回首页
const backHome = () => {
  router.push({
    path: '/'
  })
}
const register = () => {
  router.push({
    path: '/register'
  })
}
// 星评值
const value = ref(5)
// 需要写出函数，加载时自动调用，点击验证码时调用
// 生成随机字符串key并保存在本地



// 登录参数
const loginPara = ref({
  account: '',
  code: '',
  key: '',
  password: ''
})
// 使用用户数据

// 点击登录上传key以及参数
const access = () => {
  msg.value = '模拟登录'
  loginPara.value.key = key.value
  
  router.push({
    path: '/loading',
  })
  // 获取登录结果
  // login(loginPara.value).then(res => {
  //   console.log(res.code);
  //   if (res.code != '0') {
  //     msg.value = res.msg
  //   } else {
  //     localStorage.setItem("token",res.data.token.token)
  //     //存储数据
  //     const account=res
  //     // console.log('登录:用户数据',res)
  //     accountStore.setAccount(account)
  //     //登陆成功跳转首页 并传递数据
  //     router.push({
  //       path: '/loading',
  //     })
  //   }
  // })
}
//提示信息
const msg = ref('')
//同意协议
const agree = ref(1)

</script>

<template>
  <!-- 在此页面内隐藏副导航栏 -->
  <LayoutHeader />
  <!-- 登录组件 -->
  <el-row style="margin-bottom: 30px;">
    <el-col :span="9"></el-col>
    <el-col :span="6">
      <!-- 登陆卡片 -->
      <el-card class="box-card">
        <div class="card-header">
          <el-rate v-model="value" />
        </div>
        <div>
          <!-- 账号 -->
          <el-input class="input" v-model="loginPara.account" placeholder="your user name">
            <template #prepend>
              <el-icon>
                <TopRight />
              </el-icon>
            </template>
          </el-input>
          <!-- 密码 -->
          <el-input class="input" v-model="loginPara.password" show-password placeholder="your password">
            <template #prepend>
              <el-icon>
                <TopRight />
              </el-icon>
            </template>
          </el-input>
          <!-- 验证码 -->
          <div style="margin-top: 5px;">
            <!-- 验证码图片 -->
            <!-- 这是一个模拟图片 -->
          </div>
          <!-- 跳转回首页 -->
          <div>
            <el-button size="small" plain @click="backHome">To home page</el-button>
            <el-text type="danger" style="margin-left: 15px;">{{ msg }}</el-text>
          </div>

          <!-- 登录按钮/注册 -->
          <div style="text-align:center;margin-top: 50px;">
            <el-button-group>
              <!-- 登录 -->
              <el-button class="button" type="primary" size="large" @click="access">Login</el-button>
              <!-- 注册 -->
              <el-button type="primary" @click="register" size="large">Register
                <el-icon style="margin-left: 10px;" size="20">
                  <MagicStick />
                </el-icon>
              </el-button>
            </el-button-group>
          </div>
          <!-- 协议框 -->

        </div>
      </el-card>

    </el-col>
    <el-col :span="9"></el-col>
  </el-row>
</template>

<style scoped>
.button {
  width: 160px;
}

.input {
  margin-top: 25px;
  height: 38px;
  width: 100%;
}

.input-mini {
  margin-top: 20px;
  height: 38px;
  width: 50%;
}

.title {
  font-size: 13px;
  color: #444444;
  padding-left: 5px;
}

.img {
  height: 50px;
  margin-top: 20px;
  margin-left: 10px;
}

.card-header {
  display: flex;
  justify-content: center;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  margin-top: 30px;
  margin-left: 0;
  width: 100%;
  height: 480px;
  border-radius: 15px;
}
</style>