<template>
  <div>
    <h3>Teams</h3>
    <table class="table table-hover">
        <tbody>
            <tr>
                <th>Team</th>
            </tr>
            <tr v-for="(team, index) in teams" :key="index">
                <td>{{ team }}</td>
            </tr>
        </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      teams: [],
    };
  },

  created() {
    axios.get('http://127.0.0.1:5000/teams')
      .then((response) => {
        this.teams = response.data;
      }).catch((e) => {
        this.errors.push(e);
      });
  },
};
</script>

<style scoped>

</style>
