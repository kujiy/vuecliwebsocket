<template>
  <div>
    dateコマンドの結果をサーバサイドから送っています
    <label for="message">テキスト</label>
    <input type="text" name="message" v-model="message">
    <button @click="send">RUN(uso)</button>
    <div v-for="(message,index) in messages" :key="index" :value="message">{{message}}</div>
  </div>
</template>

<script>
//@ts-check
export default {
  data() {
    return {
      messages: [],
      message: "",
      ws: undefined,
    };
  },
  created() {
    const ws = (this.ws = new WebSocket(`ws://${location.host}/websocket`));
    ws.onopen = () => {};
    ws.onmessage = message => {
      this.messages = [message.data];
      // this.messages.push(message.data);
    };
  },
  methods: {
    send() {
      this.ws.send(this.message);
    }
  }
};
</script>

<style>
</style>
