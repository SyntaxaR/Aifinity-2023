import { createApp } from 'vue'
import {
    create,
    NButton,
    NIcon,
    NSpace,
    NInput,
    NBackTop,
    NGradientText,
    NPageHeader,
    NLayout,
    NLayoutHeader,
    NLayoutContent,
    NLayoutFooter,
    NText,
    NAvatar,
    NMenu,
    NImage,
    NAlert
} from 'naive-ui'

import { VueMasonryPlugin } from 'vue-masonry'

const naive = create({
    components: [NButton, NIcon, NSpace, NInput, NBackTop, NGradientText, NPageHeader, NLayout, NLayoutHeader, NLayoutContent, NLayoutFooter, NText, NAvatar, NMenu, NImage, NAlert],
})

import App from './App.vue'

import './assets/main.css'

const app = createApp(App)
app.use(VueMasonryPlugin)
app.use(naive)


app.mount('#app')
