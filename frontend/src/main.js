import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'     // import your router we created router.js


// order here matters. you have to use the router before mounting the app
const app = createApp(App)    // create a constant called app to hold the Vue application
app.use(router)               // tell the app to use the router
app.mount('#app')             // mount the app to 

