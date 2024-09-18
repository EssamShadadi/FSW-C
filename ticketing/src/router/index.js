import { createRouter, createWebHistory } from 'vue-router';
import TicketForm from '@/components/TicketForm.vue'; // Verify this path is correct

const routes = [
  {
    path: '/ticket-form',
    name: 'TicketForm',
    component: TicketForm,
  },
  // other routes
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
