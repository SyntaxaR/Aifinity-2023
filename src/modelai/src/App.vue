<script>
import ducklogo from './assets/ducklogo.png'
import ducklogotrans from './assets/ducklogotrans.png'
import { Search } from '@vicons/fa'
import { Flash20Filled } from '@vicons/fluent'
import axios from 'axios'
import TypeIt from 'typeit'
import { onMounted } from 'vue'

export default {
    name: 'App',
    setup() {
        onMounted(()=>{
            new TypeIt('#slogan').type('You search, We model.').pause(1000).delete().pause(300).type('Realise your design potential!').pause(1000).delete().pause(300).type('Human do the thinking, AI do the work.').pause(1000).delete().pause(300).type('Hosted by Amazon Web Services.').pause(1000).delete().pause(300).type('U^2Net Powered Algorithms.').pause(1000).delete().pause(300).type('SyntaxaR - STEMazon').go()
        })
    },
    data() {
        return {
            title: "model.ai",
            slogan: "You search, We model.",
            Search: Search,
            Flash20Filled: Flash20Filled,
            ducklogo: ducklogo,
            ducklogotrans: ducklogotrans,
            keyword: '',
            activeKey: "Search",  
            menu: [{label: "Search", key: "Search"}, {label: "About", key: "1"}, {label: "Contact", key: "2"}],
            imgs: [],
            placeholder: "Search it!",
            status: "undefined",
            pending: false
        }
    },
    methods: {
        sendQuery() {
            console.log(this.keyword)
            if(this.keyword == ''){
                        this.status = "error"
                        this.placeholder = "Aww, we need a keyword!"
                        return
                    }
                    this.status = "success"
                    this.placeholder = "Hold on, searching..."
                    this.pending = true
                    let query = this.keyword
                    this.keyword = ""
                    axios({
                        method: 'post',
                        url: 'https://5y4rww4upxjiqvqgejoybl3o5m0oulab.lambda-url.ap-southeast-1.on.aws/',
                        data: {
                            query: query
                        }
                    }).then((res) => {
                        console.log(res.data.result)
                        res.data.result.forEach((item) => {
                            this.imgs.push({"title": 'tbe', "url": "https://stemazon-processed.s3.ap-southeast-1.amazonaws.com/"+item+".png"})
                        })
                        this.pending = false
                        this.status = "undefined"
                        this.placeholder = "Search it!"
                    }).catch((err) => {
                        console.log(err)
                        this.pending = false
                        this.status = "error"
                        this.placeholder = "Ops, something was wrong!"
                    })
        }
    }
}

</script>

<template>
    <div style="width: 100%; height: 100%; position:absolute;">\
        <n-layout position="absolute">
            <n-layout-header position="absolute" style="align-items: center;height: 60px; display: grid; grid-template-columns: 200px 1fr; grid-column-gap:30px; padding: 0 32px;">
                <n-text style="display: flex; align-items: center; padding-left: 10px; padding-top: 10px;"><n-avatar size="medium" :src="ducklogo" :bordered="false" style=" margin-right: 10px;"/>Model.ai</n-text>
                <div style="display: flex; align-items: center; height: 100%; padding-top: 10px;">
                    <n-menu mode="horizontal" v-model="activeKey" :options="menu" style="height: 100%;"/>
                </div>
            </n-layout-header>
            
            <n-layout-content position="relative" class="layout-content" style="min-height: 800px;">
                <n-space vertical justify="center" style="margin-top: 100px; margin-bottom: 50px; align-items: center; margin-top: 10px;">
                <n-gradient-text type="info" :size="150" style="--n-font-weight:1000;">
                {{title}}
                </n-gradient-text>
                <n-gradient-text id="slogan" :gradient="{from: 'rgb(85, 85, 85)',to: 'rgb(170, 170, 170)'}" :size="35" style="--n-font-weight:800;">
                </n-gradient-text>
                </n-space>
            <n-space horizontal justify="center">
                <n-input round :placeholder="placeholder" :loading="pending" v-bind:status="status" v-model:value="keyword">
                    <template #prefix>
                        <n-icon color="#FF9900" :component="Flash20Filled"/>
                    </template>
                </n-input>
                <n-button circle :disabled="pending" @click="sendQuery">
                    <template #icon>
                        <n-icon color="#58629b" :component="Search"/>
                    </template>
                </n-button>
            </n-space>
            <div v-masonry="containerId" transition-duration="0.3s" column-width="200" horizontal-order="true" item-selector=".item">
                <div v-masonry-tile class="item" v-for="(item, index) in imgs">
                    <n-image :src="item.url" :alt="item.title" :width="100" :height="auto" />
                </div>
            </div>
            <n-back-top :right="100"/>
            </n-layout-content>

            <n-layout-footer position="relative">
                <div class="footer-box">
                    <ul class="footer-col">
                        Resources
                        <li>Model.aPi</li>
                        <li>Documentation</li>
                        <li>DevForum</li>
                    </ul>
                    <ul class="footer-col">
                        Help
                        <li>FAQ</li>
                        <li>Update Log</li>
                        <li>Report</li>
                    </ul>
                    <ul class="footer-col">
                        Clients
                        <li>Web Search</li>
                        <li>Mobile App</li>
                        <li>MS Office Plugin</li>
                    </ul>
                    <ul class="footer-col" style="padding-right: 20px;">
                        Contact
                        <li>Discord</li>
                        <li>GitHub</li>
                        <li>Facebook</li>
                    </ul>
                    <n-avatar :size="70" :src="ducklogotrans" :bordered="false" style="margin: auto; background-color: #24262b;"/>
                </div>
            </n-layout-footer>
        </n-layout>
    </div>
</template>

<style scoped>
.footer-col {
    color: azure;
    align-items: flex-start;
    display: flex;
    flex: 1 0 0;
    flex-direction: column;
    padding-bottom: 24px;
    padding-right: 24px;
}

.footer-box {
    margin: auto;
    background-color: #24262b;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    padding: 56px;
    padding-bottom: 0;
    padding-top: 32px;
}

.layout-content {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding-bottom: 0;
    top:56px;
}

</style>