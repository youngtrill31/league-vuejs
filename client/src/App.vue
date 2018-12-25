<template>
  <b-container id="app">
    <h1>League App</h1>
    <MainNav></MainNav>
    <router-view></router-view>
  </b-container>
</template>

<script>
import Vue from 'vue';
import MainNav from '@/components/MainNav';
import Home from '@/components/Home';

export const serverBus = new Vue();

export default {
  name: 'App',
  components: {
    MainNav,
    Home,
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
