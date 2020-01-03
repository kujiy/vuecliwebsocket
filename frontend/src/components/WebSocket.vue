<template>
  <div>
    <label for="message">テキスト</label>
    <input type="text" name="message" v-model="message">
    <button @click="connect('connect_1')">connect 1</button>
    <button @click="connect('connect_2')">connect 2</button>
    <button @click="send">送信</button>
    <hr>
    <template>
      <pre>
        {{ message }}
      </pre>
    </template>
    <hr>
  </div>
</template>

<script>
/* eslint-disable */
const axios = require('axios');

//@ts-check
export default {
  data() {
    return {
      message: "",
      ws: undefined,
      key: ""
    };
  },
  created() {
  },
  methods: {
    connect(key) {
      this.key = key;
      console.log(key);
      // console.log(e.currentTarget.getAttribute('session_type'));
      const ws = (this.ws = new WebSocket(`ws://${location.host}/websocket?key=${key}`));
      ws.onopen = () => {ws.send(`Hello WebSocket=${key}`)};
      ws.onmessage = message => {
        this.message = message.data;
      };
      this.intervalRequest(key);
    },
    send() {
      this.ws.send(this.message);
    },
    intervalRequest(key) {
      setInterval(function() {
        console.log(key);
        this.send();
      }.bind(this), 1000, key);
      // window.setInterval(() => console.log(key), 1000, key);
    },
    request() {
      axios
          .get('http://localhost:8080/websocket/cmd?key=' + this.key)
          .then(response => (
                  this.message = response.data
          ))
    }
  }
};
</script>

<style>
</style>
