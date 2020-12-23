import { createApp } from 'vue'
import App from './App.vue'
import MyChart from './components/MyChart.vue'


const app = createApp(App);
app.use(MyChart);
app.mount('#app')

// createApp(App).mount('#app')
