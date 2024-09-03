require("./bootstrap");

import { createApp } from "vue";
import App from "./pages/App.vue";
import FontAwesomeIcon from "./assets/fontawesome-icons.js";

createApp(App)
	.component("font-awesome-icon", FontAwesomeIcon)
	.mount("#app");
