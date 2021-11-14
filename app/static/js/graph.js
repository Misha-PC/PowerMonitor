google.charts.load('current', {'packages':['line']});
google.charts.setOnLoadCallback(drawChart);


function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function drawChart()
{
   console.log('Request to api...')

    response = httpGet("api/get/array")
    console.log(response)
    p = JSON.parse(response)
    console.log(p)

  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Day');
  data.addColumn('number', 'Guardians of the Galaxy');
  data.addRows(p)


  var options = {
    chart: {
      title: 'Box Office Earnings in First Two Weeks of Opening',
      subtitle: 'in millions of dollars (USD)'
    },
    width: 900,
    height: 500,
    vAxis: {
            viewWindow: {
              max:260,
              min:0
            }
        },
  };

  var chart = new google.charts.Line(document.getElementById('linechart_material'));

  chart.draw(data, google.charts.Line.convertOptions(options));
}
