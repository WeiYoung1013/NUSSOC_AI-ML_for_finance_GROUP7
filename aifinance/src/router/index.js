import {createRouter, createWebHistory} from 'vue-router'
import Login from '@/views/Login/index.vue'
import Layout from '@/views/Layout/index.vue'
import Register from '@/views/Register/Register.vue'
import StepFirst from '@/views/Register/components/Step1.vue'
import StepSecond from '@/views/Register/components/Step2.vue'
import Home from '@/views/Home/index.vue'


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        // 一级路由 主页
        {
            path: '/',
            component: Layout,
            // 二级路由
            children: [
                {
                    path: '',
                    name: 'home',
                    component: Home,
                    props: true
                },
                // 注册
                {
                    path: 'register',
                    component: Register,
                    // 存在顺序关系的页面
                    children: [{
                        path: '',
                        component: StepFirst
                    },
                        {
                            path: '2',
                            component: StepSecond
                        }
                    ]
                },
                // 普通用户路由
                // 管理员路由
            ]
        },
        // 一级路由 登录
        {
            name: 'login',
            path: '/login',
            component: Login
        },
        // 一级路由 加载
    ]
})

// 路由守卫
router.beforeEach((to, from, next) => {

    let token = localStorage.getItem("token");  // 获取token
    if (to.name != 'login') {  //如果不是去登录页面需要判断是否有token
        // 白名单
        if (to.name == 'home' || to.path == '/register') {
            next()
        }


        if (!token) {
            next({name: "login"});

        } else {
            next();
        }

    } else {
        next();
    }
})
// to: 表示即将要进入的目标路由对象，包含路由信息。它包括目标路由的路径、名称、参数、查询参数等信息。
// from:表示当前导航正要离开的路由对象，也是一个包含路由信息的对象，
// next: 函数，确保导航一定会成功完成。在beforeEach中必须调用next()，否则跳转会被中止。
// next()可以接收一个参数，可以是字符串，Error实例对象，布尔值，或者一个路由对象。根据传递的参数不同，可以控制路由的不同行为

export default router

