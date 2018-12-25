import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import Standings from '@/components/Standings';
import TeamLogin from '@/components/TeamLogin';
import TeamRegistration from '@/components/TeamRegistration';
import TeamRegistrationConfirmation from '@/components/TeamRegistrationConfirmation';
import NotFound from '@/components/error-pages/NotFound';
import Teams from '@/components/Teams';
import Logout from '@/components/Logout';
import TeamHome from '@/components/TeamHome';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound,
    },
    {
      path: '/teamLogin',
      name: 'TeamLogin',
      component: TeamLogin,
    },
    {
      path: '/standings',
      name: 'Standings',
      component: Standings,
    },
    {
      path: '/teamRegistration',
      name: 'TeamRegistration',
      component: TeamRegistration,
    },
    {
      path: '/teamRegistrationConfirmation',
      name: 'TeamRegistrationConfirmation',
      component: TeamRegistrationConfirmation,
    },
    {
      path: '/teams',
      name: 'Teams',
      component: Teams,
    },
    {
      path: '/teamHome',
      name: 'TeamHome',
      component: TeamHome,
    },
    {
      path: '/logout',
      name: 'Logout',
      component: Logout,
    },
  ],
  mode: 'history',
});
