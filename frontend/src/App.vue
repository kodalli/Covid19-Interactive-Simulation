<template>
  <div id="app">

    <column-chart :data="simDataAttribute"></column-chart>

    <div class="row">
      <!-- <div class="col-xs-6"> -->
      <div class="col-md-6">

        <form @submit.prevent="submitForm">
          <div class="form-group row">
            <label for="colFormLabel" class="col-sm-4 col-form-label">Healthy Young</label>
            <div class="col-sm-5">
              <input type="text" class="form-control" placeholder="Healthy Young"
                v-model="simDataAttribute.healthyYoung">
            </div>
          </div>

          <div class="form-group row">
            <label for="colFormLabel" class="col-sm-4 col-form-label">Healthy Young Freerider</label>
            <div class="col-sm-5">
              <input type="text" class="form-control" placeholder="Healthy Young Freerider"
                v-model="simDataAttribute.healthyYoungFreerider">
            </div>
          </div>

          <div class="form-group row">
            <label for="colFormLabel" class="col-sm-4 col-form-label">Sick Young</label>
            <div class="col-sm-5">
              <input type="text" class="form-control" placeholder="Sick Young" v-model="simDataAttribute.sickYoung">
            </div>
          </div>

          <div class="form-group row">
            <label for="colFormLabel" class="col-sm-4 col-form-label">Healthy Elderly</label>
            <div class="col-sm-5">
              <input type="text" class="form-control" placeholder="Healthy Elderly"
                v-model="simDataAttribute.healthyElderly">
            </div>
          </div>

          <div class="form-group row">
            <label for="colFormLabel" class="col-sm-4 col-form-label">Healthy Elderly Freerider</label>
            <div class="col-sm-5">
              <input type="text" class="form-control" placeholder="Healthy Elderly Freerider"
                v-model="simDataAttribute.healthyElderlyFreerider">
            </div>
          </div>

          <div class="form-group row">
            <label for="colFormLabel" class="col-sm-4 col-form-label">Sick Elderly</label>
            <div class="col-sm-5">
              <input type="text" class="form-control" placeholder="Sick Elderly" v-model="simDataAttribute.sickElderly">
            </div>
          </div>

          <div class="form-group row">
            <label for="colFormLabel" class="col-sm-4 col-form-label">Vaccines</label>
            <div class="col-sm-5">
              <input type="text" class="form-control" placeholder="Vaccines" v-model="simDataAttribute.vaccines">
            </div>
          </div>

          <div class="form-group row">
            <label for="colFormLabel" class="col-sm-4 col-form-label">Time Span (Days)</label>
            <div class="col-sm-5">
              <input type="text" class="form-control" placeholder="Time Span (Days)"
                v-model="simDataAttribute.timeSpan">
            </div>
          </div>

          <button class="btn btn-outline-dark row mt-3" style="outline">Run Simulation</button>

        </form>

      </div>

      <!-- <div class="col-xs-6"> -->
      <div class="col-md-6">

        <table class="table">
          <thead>
            <th>HY</th>
            <th>HYF</th>
            <th>SY</th>
            <th>HE</th>
            <th>HEF</th>
            <th>SE</th>
            <th>V</th>
            <th>Days</th>
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
    </div>
  </div>
  <!-- </div> -->
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