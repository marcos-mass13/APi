import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import * as bootstrap from 'bootstrap'

/* Bootstrap */
import 'bootstrap/dist/css/bootstrap.min.css' 

const app = createApp(App) 


app.use(router)

app.use(bootstrap) 

app.mount('#app')
