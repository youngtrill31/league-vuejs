<template>
    <div class="container">
        <h4>Team Login</h4>
        <input type="text" name="manager_email"
               v-model="manager_email" placeholder="Manager Email" />
        <input type="password" name="password"
               v-model="password" placeholder="Password" />
        <button type="button" v-on:click="login()">Login</button>
    </div>
</template>

<script>
import axios from 'axios';
import { serverBus } from '../App';

export default {
  data() {
    return {
      manager_email: '',
      password: '',
    };
  },
  methods: {
    login() {
      axios.post('http://127.0.0.1:5000/team_login',
        {
          manager_email: this.manager_email,
          password: this.password,
        },
      ).then((res) => {
        localStorage.setItem('userToken', res.data);
        this.manager_email = '';
        this.password = '';
        this.$router.push({ path: '/teamHome' });
      }).catch((err) => {
        console.log(err);
      });
      this.emitMethod();
    },
    emitMethod() {
      serverBus.$emit('logged-in', 'loggedin');
    },
  },
};
</script>

<style scoped>

</style>
