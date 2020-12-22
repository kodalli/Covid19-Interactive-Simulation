<template>
  <div id="app">

    <form action="">
      <div class="form-group">
        <input type="text" class="form-control row mt-3" placeholder="Healthy Young">
        <input type="text" class="form-control row mt-3" placeholder="Healthy Young Freerider">
        <input type="text" class="form-control row mt-3" placeholder="Sick Young">
        <input type="text" class="form-control row mt-3" placeholder="Healthy Elderly">
        <input type="text" class="form-control row mt-3" placeholder="Healthy Elderly Freerider">
        <input type="text" class="form-control row mt-3" placeholder="Sick Elderly">
        <input type="text" class="form-control row mt-3" placeholder="Vaccines">
        <input type="text" class="form-control row mt-3" placeholder="Time Span (Days)">
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
        <tr v-for="item in simData" :key="item.id">
          <td>{{ item.healthyYoung }}</td>
          <td>{{ item.healthyYoungFreerider }}</td>
          <td>{{ item.sickYoung }}</td>
          <td>{{ item.healthyElderly }}</td>
          <td>{{ item.healthyElderlyFreerider }}</td>
          <td>{{ item.sickElderly }}</td>
          <td>{{ item.vaccines }}</td>
          <td>{{ item.timeSpan }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return {
      simData: []
    }
  },
  async created(){
    var response = await fetch('http://127.0.0.1:8000/api/simulation/')
    this.simData = await response.json()
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
