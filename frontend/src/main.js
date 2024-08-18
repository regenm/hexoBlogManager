import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

const app = createApp(App);

app.use(router);

app.mount('#app');
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
app.use(ElementPlus)