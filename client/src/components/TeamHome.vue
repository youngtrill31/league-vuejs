<template>
  <div class="container" v-if="auth=='loggedin'">
      <h3>Team Home</h3>
      <p>
          This is the Team Home area
      </p>
  </div>
  <div v-else>Not logged in!</div>
</template>

<script>
import { serverBus } from '../App';

export default {
  name: 'TeamHome',
  data() {
    return {
      auth: '',
    };
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
    #secure {
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 20px;
        margin-top: 10px;
    }
</style>
