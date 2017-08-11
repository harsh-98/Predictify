/*********LINE GRAPH*************/

function plotGraphs(line,pie1,pie2)
{

  var data = {
    labels: [1,2,3],
    datasets: [{
      label: "Your Score",
      borderColor: "rgba(255,99,132,1)",
      data: line,
      // data: [7,8,10],
      fill: false,
    },
    {
      label: "Average",
      borderColor: "#0095FF",
      data: [{x:1,y:11},{x:2,y:11},{x:3,y:11}],
      fill: false,
    }
    ]
  };

  var options = {
    maintainAspectRatio: false,
    scales: {
      yAxes: [{
        stacked: false,
        gridLines: {
          display: true,
        },
        ticks: {
          beginAtZero: true,
        },
        scaleLabel: {
          display: true,
          labelString: 'Score'
        }
      }],
      xAxes: [{
        gridLines: {
          display: false
        },
        scaleLabel: {
          display: true,
          labelString: 'Exam Number'
        }
      }]
    },
    layout: {
      padding: {
        left: 15, 
        right: 15,
        top: 15,
        bottom: 15,
      }
    }
  };

  var ctx = document.getElementById("chart").getContext("2d");

  var chart = new Chart(ctx, {
    type: 'line',
    data: data, 
    options: options
  })
  /**********PIE CHART I****************/

  var data={
    labels: ['A','B','C','D','E'],
    datasets: [{
      data: pie1,
      // data: [3.35,8.33,66.28,16.76,5.27],
      backgroundColor: [
                  "#FF6384",
                  "#63FF84",
                  "#84FF63",
                  "#8463FF",
                  "#6384FF"
              ],
    }],
  };

  var ctx2 = document.getElementById("pie-chart1").getContext("2d");

  var options ={
        legend: {
          display: true,
          position: 'left',
        },
        responsive: true,
        layout: {
        padding: {
          left: 15, 
          right: 15,
          top: 25,
          bottom: 15,
        }
      }
    };

  var chart2 = new Chart(ctx2,{
    type: 'pie',
    data: data,
    options: options 
  });


  var data={
    labels: ['A','B','C','D','E'],
    datasets: [{
      data: pie2,
      // data: [1.82,6.51,63.03,28.16,0.48],
      backgroundColor: [
                  "#FF6384",
                  "#63FF84",
                  "#84FF63",
                  "#8463FF",
                  "#6384FF"
              ],
    }],
  };

  var ctx3 = document.getElementById("pie-chart2").getContext("2d");

  var chart3 = new Chart(ctx3,{
    type: 'pie',
    data: data,
    options: options 
  });
}