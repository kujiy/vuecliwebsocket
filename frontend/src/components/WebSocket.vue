<template>
  <div>
      <div v-for="message in messages" :key=message :value=message>
          {{message}}
      </div>
  </div>
</template>

<script>
//@ts-check
export default {
  data() {
    return {
      messages: []
    };
  },
  created() {
      const ws = this.ws = new WebSocket(`ws://${location.host}/websocket`);
      ws.onopen = () => {
      }
      ws.onmessage = (message) => {
          this.messages.push(message);
      }
  }
};
</script>

<style>
</style>
