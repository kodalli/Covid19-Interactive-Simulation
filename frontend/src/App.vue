<template>
  <div id="app">

    <form @submit.prevent="submitForm">
      <div class="form-group">
        <input type="text" class="form-control row mt-3" placeholder="Healthy Young"
          v-model="simDataAttribute.healthyYoung">
        <input type="text" class="form-control row mt-3" placeholder="Healthy Young Freerider"
          v-model="simDataAttribute.healthyYoungFreerider">
        <input type="text" class="form-control row mt-3" placeholder="Sick Young" v-model="simDataAttribute.sickYoung">
        <input type="text" class="form-control row mt-3" placeholder="Healthy Elderly"
          v-model="simDataAttribute.healthyElderly">
        <input type="text" class="form-control row mt-3" placeholder="Healthy Elderly Freerider"
          v-model="simDataAttribute.healthyElderlyFreerider">
        <input type="text" class="form-control row mt-3" placeholder="Sick Elderly"
          v-model="simDataAttribute.sickElderly">
        <input type="text" class="form-control row mt-3" placeholder="Vaccines" v-model="simDataAttribute.vaccines">
        <input type="text" class="form-control row mt-3" placeholder="Time Span (Days)"
          v-model="simDataAttribute.timeSpan">
        <button class="btn btn-success row mt-3">Run Simulation</button>
      </div>
    </form>


    <table class="table">
      <thead>
        <th>Healthy Young</th>
        <th>Healthy Young Freerider</th>
        <th>Sick Young</th>
        <th>Healthy Elderly</th>
        <th>Healthy Elderly Freerider</th>
        <th>Sick Elderly</th>
        <th>Vaccines</th>
        <th>Time Span (Days)</th>
      </thead>
      <tbody>
        <tr v-for="item in simData" :key="item.id" @dblclick="$data.simDataAttribute = item">
          <td>{{ item.healthyYoung }}</td>
          <td>{{ item.healthyYoungFreerider }}</td>
          <td>{{ item.sickYoung }}</td>
          <td>{{ item.healthyElderly }}</td>
          <td>{{ item.healthyElderlyFreerider }}</td>
          <td>{{ item.sickElderly }}</td>
          <td>{{ item.vaccines }}</td>
          <td>{{ item.timeSpan }}</td>
          <td>
            <button class="btn btn-outline-danger bt-sm mx-1" @click="deleteSimData(item)">del</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        simDataAttribute: {},
        simData: []
      }
    },

    async created() {
      await this.getSimData();
    },

    methods: {
      submitForm() {
        if (this.simDataAttribute.id === undefined) {
          this.createSimData();
        } else {
          this.editSimData();
        }
      },

      async getSimData() {
        var response = await fetch('http://127.0.0.1:8000/api/simulation/')
        this.simData = await response.json()
      },

      async createSimData() {
        await this.getSimData();

        await fetch('http://127.0.0.1:8000/api/simulation/', {
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.simDataAttribute)
        });
        await this.getSimData();
      },

      async editSimData() {
        await this.getSimData();

        await fetch(`http://127.0.0.1:8000/api/simulation/${this.simDataAttribute.id}/`, {
          method: 'put',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.simDataAttribute)
        });
        await this.getSimData();
        this.simDataAttribute = {};
      },

      async deleteSimData(simDataAttribute) {
        await this.getSimData();

        await fetch(`http://127.0.0.1:8000/api/simulation/${simDataAttribute.id}/`, {
          method: 'delete',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(simDataAttribute)
        });
        await this.getSimData();
      }
    }
  }
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>