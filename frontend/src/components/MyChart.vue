<template>
    <div>
        <h1>This is some text</h1>
        <!-- <my-chart :chartdata="chartdata" :options="options"></my-chart> -->
    </div>
</template>

<script>
    import {
        Bar
    } from 'vue-chartjs'

    export default {
        extends: Bar,
        data: () => ({
            chartdata: {
                labels: ['January', 'February'],
                datasets: [{
                    label: 'Data One',
                    backgroundColor: '#f87979',
                    data: [40, 20]
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        }),

        mounted() {
            this.renderChart(this.chartdata, this.options)
        }
    }
</script>