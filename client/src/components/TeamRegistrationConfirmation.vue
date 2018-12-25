<template>
    <div>
      <span>Team account created for {{ team }}!</span>
    </div>
</template>

<script>
import { serverBus } from '../App';

export default {
  data() {
    return {
      team: '',
    };
  },
  mounted() {
    serverBus.$on('confirm-page', (data) => {
      this.team = data;
      console.log(data);
    });
  },
};
</script>

<style scoped>

</style>
