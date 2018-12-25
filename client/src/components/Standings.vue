<template>
  <div>
    <h3>Current Standings</h3>
    <table class="table table-hover">
        <tbody>
            <tr>
                <th>Team</th>
                <th>Wins</th>
                <th>Losses</th>
            </tr>
            <tr v-for="d in data" :key="d.id">
                <td>{{ d.team }}</td>
                <td>{{ d.wins }}</td>
                <td>{{ d.losses }}</td>
            </tr>
        </tbody>
    </table>
    <!--<p>{{ data }}</p>-->
  </div>
</template>

<script>
export default {
  name: 'Standings',
  data() {
    return {
      data: [
        {
          id: 1,
          team: 'Clippers',
          wins: 10,
          losses: 2,
        },
        {
          id: 2,
          team: 'Lakers',
          wins: 2,
          losses: 1,
        },
      ],
    };
  },
};
</script>
