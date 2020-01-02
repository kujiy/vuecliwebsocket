<template>
  <div>
    <label for="message">テキスト</label>
    <input type="text" name="message" v-model="message">
    <button @click="connect('')">connect 1</button>
    <button @click="connect('2')">connect 2</button>
    <button @click="send">送信</button>
    <div v-for="(message,index) in messages" :key="index" :value="message">{{message}}</div>
  </div>
</template>

<script>
/* eslint-disable */

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
  },
  methods: {
    connect(key) {
      console.log(key);
      // console.log(e.currentTarget.getAttribute('session_type'));
      const ws = (this.ws = new WebSocket(`ws://${location.host}/websocket${key}`));
      ws.onopen = () => {ws.send('Hello WebSocket')};
      ws.onmessage = message => {
        this.messages.push(message.data);
      };
    },
    send() {
      this.ws.send(this.message);
    }
  }
};
</script>

<style>
</style>
