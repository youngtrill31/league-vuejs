<template>
    <div class="container">
      <div class="row">
        <div class="col-md-6 mt-5 mx-auto">
          <form v-on:submit.prevent="register">
            <h1 class="h3 mb-3 font-weight-normal">Register Your Team</h1>
            <div class="form-group">
              <label for="name">Team Name</label>
              <input type="text" v-model="team_name" class="form-control" name="team_name"
                     placeholder="Enter your team name" v-validate="'required|min:2'">
              <div>
                <span>{{ errors.first('team_name') }}</span>
              </div>
            </div>
            <div class="form-group">
              <label for="name">Manager Name</label>
              <input type="text" v-model="manager_name" class="form-control"
                     name="manager_name" placeholder="Enter manager name"
                     v-validate="'required'">
            </div>
            <div>
              <span>{{ errors.first('manager_name') }}</span>
            </div>
            <div class="form-group">
              <label for="email">Manager Email</label>
              <input type="text" v-model="manager_email" class="form-control"
                     name="manager_email" placeholder="Enter manager email"
                      v-validate="'required|email'">
            </div>
            <div>
              <span>{{ errors.first('manager_email') }}</span>
            </div>
            <div class="form-group">
              <label for="password">Password</label>
              <input type="password" v-model="password" class="form-control"
                     name="password" placeholder="Enter password"
                      v-validate="'required|min:5'" ref="password">
            </div>
            <div>
              <span>{{ errors.first('password') }}</span>
            </div>
            <div class="form-group">
              <label for="password">Confirm Password</label>
              <input type="password" v-model="confirm_password" class="form-control"
                     name="confirm_password" placeholder="Confirm password"
                      v-validate="'required|confirmed:password'">
            </div>
            <div>
              <span>{{ errors.first('confirm_password') }}</span>
            </div>
            <div class="form-group">
              <label for="locations">Locations</label>
              <select class="form-control" v-model="selected_location">
                <option v-for="(location, index) in locations"
                        :key="index"
                        :value="location">
                  {{ location }}
                </option>
              </select>
            </div>
            <div class="form-group">
              <label for="Divisions">Divisions</label>
              <select class="form-control" v-model="selected_division">
                <option v-for="(division, index) in divisions"
                        :key="index"
                        :value="division">
                  {{ division }}
                </option>
              </select>
            </div>
            <br>
            <button type="submit" @click="validateForm"
                    class="btn btn-lg btn-primary btn-block"
                    :disabled="errors.any()">Submit</button>
          </form>
        </div>
      </div>
    </div>
</template>


<script>

import axios from 'axios';
import { serverBus } from '../App';

export default {
  data() {
    return {
      team_name: '',
      manager_name: '',
      manager_email: '',
      password: '',
      confirm_password: '',
      locations: [],
      selected_location: '',
      divisions: [],
      selected_division: '',
    };
  },

  computed: {
    isComplete() {
      return this.team_name && this.manager_name && this.manager_email && this.password;
    },
  },
  created() {
    axios.get('http://127.0.0.1:5000/locations')
      .then((response) => {
        this.locations = response.data;
      }).catch((e) => {
        this.errors.push(e);
      });
    axios.get('http://127.0.0.1:5000/divisions')
      .then((res) => {
        this.divisions = res.data;
      }).catch((e) => {
        this.errors.push(e);
      });
  },

  methods: {
    register() {
      axios.post('http://127.0.0.1:5000/team_registration',
        {
          team_name: this.team_name,
          manager_name: this.manager_name,
          manager_email: this.manager_email,
          password: this.password,
          selected_location: this.selected_location,
          selected_division: this.selected_division,
        },
      ).then((res) => {
        console.log(res);
      }).catch((err) => {
        console.log(err);
      });
      serverBus.$emit('confirm-page', this.team_name);
      this.$router.push({ path: '/teamRegistrationConfirmation' });
    },
    validateForm() {
      this.$validator.validateAll();
    },
  },
};
</script>

<style scoped>

</style>
