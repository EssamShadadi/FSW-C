<template>
  <div class="container mt-4">
    <h2>Create Ticket</h2>
    <form @submit.prevent="submitForm">
      <div class="mb-3">
        <label for="employee_name" class="form-label">Employee Name</label>
        <input v-model="formData.employee_name" type="text" class="form-control" placeholder="Employee Name" id="employee_name" required>
      </div>



      <div class="mb-3">
        <label for="problem_description" class="form-label">Problem Description</label>
        <textarea v-model="formData.problem_description" class="form-control" id="problem_description" rows="3" required></textarea>
      </div>

      <div class="mb-3">
        <label for="problem_type" class="form-label">Problem Type</label>
        <select v-model="formData.problem_type" class="form-select" id="problem_type" @change="updateproblem_type" required>
          <option value="" disabled>Select Problem Type</option>
          <option value="hardware">Hardware</option>
          <option value="software">Software</option>
        </select>
      </div>

      <div v-if="formData.problem_type === 'hardware'" class="mb-3">
        <label for="deviceSerialNumber" class="form-label">Device Serial Number</label>
        <input v-model="formData.deviceSerialNumber" type="text" class="form-control" id="deviceSerialNumber">
      </div>

      <div v-if="formData.problem_type === 'software'" class="mb-3">
        <label for="osVersion" class="form-label">OS Version</label>
        <input v-model="formData.osVersion" type="text" class="form-control" id="osVersion">
      </div>

      <!-- Add more fields based on problem type -->

      <button type="submit" class="btn btn-primary">Submit Ticket</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      formData: {
        employee_name: '',
        problem_description: '',
        problem_type: '',
        device_type: '',
        deviceSerialNumber: '',
        osVersion: '',
        softwareApplication: '',
        errorCode: '',
        devicePicture: null,
        screenshot: null,
      },
    };
  },
  methods: {
    submitForm() {
      const formData = new FormData();
      Object.keys(this.formData).forEach((key) => {
        if (this.formData[key]) {
          formData.append(key, this.formData[key]);
        }
      });

      axios.post('http://localhost:8000/api/tickets/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      .then((response) => {
        alert('Ticket submitted successfully!');
        this.resetForm();
      })
      .catch((error) => {
        console.error(error);
        alert('Error submitting ticket.');
      });
    },
    resetForm() {
      this.formData = {
        employee_name: '',
        problem_description: '',
        problem_type: '',
        device_type: '',
        deviceSerialNumber: '',
        osVersion: '',
        softwareApplication: '',
        errorCode: '',
        devicePicture: null,
        screenshot: null,
      };
    },
    updateproblem_type() {
      // Handle additional logic when problem type changes
    }
  },
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
