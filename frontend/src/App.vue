<template>
  <div id="app">
    <web-socket></web-socket>
  </div>
</template>

<script>
import WebSocket from './components/WebSocket.vue'

export default {
  name: 'app',
  components: {
    WebSocket
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  margin-top: 60px;
}
</style>
