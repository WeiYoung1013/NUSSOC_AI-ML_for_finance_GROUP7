import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
//配置
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

// https://vitejs.dev/config/
export default defineConfig({
  server:{
    proxy:{
            '/api': {  //代理别名
              target: 'http://127.0.0.1:7777/',   //代理目标服务器地址
              changeOrigin: true,
              secure: true,
              pathRewrite:{  //替换路径中的/api
                '^/api':''
              }
        }
    }
  },
  plugins: [
    vue(),
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [
        //配置elementPlus采用sass样式配色系统
        ElementPlusResolver({ importStyle: "sass" })
      ],
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `
          @use "@/styles/element/index.scss" as *;
          @use "@/styles/var.scss" as *;
        `,
      }
    }
  },
  build: {
    rollupOptions: {
      external: ['stream']
    }
  }
})
