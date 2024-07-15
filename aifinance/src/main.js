import { createApp } from 'vue'
import router from "./router";
import * as echarts from "echarts";
import App from "./App.vue";
import ElementPlus from "element-plus"; // 导入 element-plus
import "element-plus/theme-chalk/index.css"; // 根据 node_modules 文件夹选择对应的 theme-chalk/index.css 文件
import zhCn from "element-plus/es/locale/lang/zh-cn";
import store from "@/store/store.ts"; // 设置 element-plus 语言

const app = createApp(App)
app.config.globalProperties.$echarts = echarts; // 挂载到 app.config.globalProperties 上
app.use(ElementPlus, { locale: zhCn }); // 使用 element-plus, 并设置语言
app.use(store).use(router).mount("#app"); // 挂载 store 和 router

app.config.globalProperties.$changeTitle = function () {
    document.title = "visualization";
};
