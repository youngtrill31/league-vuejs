<template>
  <b-navbar>
    <router-link to="/">Home</router-link>
    <div v-if="auth==''">
      <router-link to="/teamRegistration">Team Registration</router-link>
    </div>
    <div v-if="auth=='loggedin'">
      <router-link to="/teamHome">Team Home</router-link>
    </div>
    <router-link to="/standings">Standings</router-link>
    <router-link to="/teams">Teams</router-link>
    <div v-if="auth==''">
      <router-link to="/teamLogin">Team Login</router-link>
    </div>
    <div v-if="auth=='loggedin'">
      <a href="" v-on:click="logout">Logout</a>
    </div>
  </b-navbar>
</template>

<script>
import { serverBus } from '../App';

export default {
  name: 'MainNav',
  data() {
    return {
      auth: '',
    };
  },

  methods: {
    logout() {
      localStorage.removeItem('userToken');
    },
  },

  mounted() {
    serverBus.$on('logged-in', (status) => {
      this.auth = status;
      console.log(status);
    });
  },
};
</script>

<style scoped>

</style>
