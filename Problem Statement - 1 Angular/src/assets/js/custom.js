google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ["executionm_method", "values", { role: "style" } ],
    ["lecture", 0.4, "red"],
    ["Other_methods", 0.35, "silver"]
  ]);

// Optional; add a title and set the width and height of the chart
  var options = {'title':'comparison', 'width':550, 'height':400};

// Display the chart inside the <div> element with id="piechart"

var chart = new google.visualization.BarChart(document.getElementById("barchart_values"));
  chart.draw(data,options);
  google.visualization.events.addListener(chart, 'select', selectHandler);
  // chart.getSelection()

  function selectHandler(e) {
    console.log(chart.getSelection());
    google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      var data = google.visualization.arrayToDataTable([
        ["executionm_method", "values", { role: "style" } ],
        ["lecture", 0.8, "yellow"],
        ["Other_methods", 0.56, "silver"]
      ]);
  console.log($.getElementById('barchart_values'))
  // Optional; add a title and set the width and height of the chart
	  var options = {'title':'comparison', 'width':550, 'height':400};

  // Display the chart inside the <div> element with id="piechart"
  
  var chart = new google.visualization.BarChart(document.getElementById("barchart_values"));
      chart.draw(data,options);
  }
  }
}
