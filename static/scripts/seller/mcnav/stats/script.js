function plot(){
    const mcnav_graph = document.querySelector(".mcnav_seller_stats")

    console.log(mcnav_graph)

    const data = [
        {
            x: [1, 2, 3],
            y: [1, 2, 3],
            type: 'scatter', // Other options: 'bar', 'line', etc.
            mode: 'lines+markers',
            marker: { color: 'blue' }
        }
    ]
    const layout = {
        title: 'Testing',
        xaxis: { title: 'X-Axis Label' },
        yaxis: { title: 'Y-Axis Label' }
    }

    Plotly.newPlot(mcnav_graph, data, layout)
}

plot()
