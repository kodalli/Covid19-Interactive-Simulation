<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="This is a customizable vue component prop variable"/>
    <HelloWorld :somevar="[1.2, 4.3]"/>
    <MyChart/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import MyChart from './components/MyChart.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    MyChart
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
