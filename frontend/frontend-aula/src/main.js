import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Bootstrap from 'bootstrap' 

/* Bootstrap */
import 'bootstrap/dist/css/bootstrap.min.css' 
// import 'bootstrap' 


const app = createApp(App) 


app.use(router)

app.use(Bootstrap) 

app.mount('#app')
