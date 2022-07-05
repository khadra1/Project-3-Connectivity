// console.log("data=" + alldata.x);
// World countries bar chart
let title = alldata.filter1;

let trace1 = {
  x: alldata.x,
  y: alldata.y,
  marker:{color: '#004c6d'},
  type: 'bar'
};
let data = [trace1];
let layout = {
  title: title
};
Plotly.newPlot("plot", data, layout);

// Creating function to make the World Map legend dynamic according to the dataset

function countDigits(number){
  return parseInt(number).toString().length;
}

// World Map function filtering by year and data1 
async function drawChart(data1, year) {
  console.log("data1=", data1)
  //  World Map legend function
  let avg = 0;
  data1.forEach(elem=>avg+=countDigits(elem.value))

  //total number of element -> average length of digits = 2
  avg = parseInt(avg / data1.length);
  console.log("average ",avg)

  // Highcharts.js World Mpap function
  const topology = await fetch(
    'https://code.highcharts.com/mapdata/custom/world.topo.json'
  ).then(response => response.json());
  let factor = Math.pow(10,avg); // 0 -> 100,
  return Highcharts.mapChart('container-map', {
    chart: {
      map: topology,
      borderWidth: 1
    },

    // Legend colours
    colors: [ '#c1e7ff','#a3cbe5','#86b0cc','#6996b3','#4c7c9b','#2d6484',
    '#004c6d'],

    //  Map title changes with the year slider and option submit button
    title: {
      text: title + " " + year
    },

    mapNavigation: {
      enabled: true
    },

    legend: {
      title: {
        text: '',
        style: {
          color: ( // theme
            Highcharts.defaultOptions &&
            Highcharts.defaultOptions.legend &&
            Highcharts.defaultOptions.legend.title &&
            Highcharts.defaultOptions.legend.title.style &&
            Highcharts.defaultOptions.legend.title.style.color
          ) || 'black'
        }
      },
      align: 'left',
      verticalAlign: 'bottom',
      floating: true,
      layout: 'vertical',
      valueDecimals: 0,
      backgroundColor: ( // theme
        Highcharts.defaultOptions &&
        Highcharts.defaultOptions.legend &&
        Highcharts.defaultOptions.legend.backgroundColor
      ) || 'rgba(255, 255, 255, 0.85)',
      symbolRadius: 0,
      symbolHeight: 14
    },
    //  Using factor steps (*2) to populate the world map legend automatically according to dataset
    colorAxis: {
      dataClassColor: 'category',
      dataClasses: [{
        to: factor*2
      }, {
        from: factor*2,
        to: factor*4
      }, {
        from: factor*4,
        to: factor*6
      }, {
        from: factor*6,
        to: factor*8
      }, {
        from: factor*8,
        to: factor*10
      }, {
        from: factor*10
      }]
    },
//  Using the data saved under data1 to map the countries using ISO codes
    series: [{
      data: data1,
      joinBy: ['iso-a3', 'code'],
      animation: true,
      name: '',
      states: {
        hover: {
          color: '#a4edba'
        }
      },
      tooltip: {
        valueSuffix: ''
      },
      shadow: false
    }]
  });
};

// Line chart for world regions 

//  creating the years ranges
const yearsRange = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021];

// Getting the date keys from the tracedata dict in main.py where we stored the data from the internet usage excel sheet
const differentDataKeys = Object.keys(alldata.tracedata)

    // Functions created for the option buttons and to populate regions line chart(printBtn and drawLineChart) 
function printBtn() {
  var myButtons=document.getElementById("myButtons");
  for (var i = 0; i < differentDataKeys.length; i++) {
    var temp=document.createElement("button");
    temp.innerHTML=differentDataKeys[i];
    temp.setAttribute("value",differentDataKeys[i])
    temp.setAttribute("onClick","drawLineChart(this.value)")
    myButtons.appendChild(temp);
  }
}
printBtn()
drawLineChart("Fixed-telephone subscriptions");
function drawLineChart(dataType) {
  let traceAfrica = {
    x: yearsRange,
    y: alldata.tracedata[dataType].Africa,
    mode: 'lines+markers',
    connectgaps: true,
    name: "Africa",
    marker:{
      color: '#004c6d', 
      width: 0.2
    }
  };

  let traceAmericas = {
    x: yearsRange,
    y: alldata.tracedata[dataType].Americas,
    mode: 'lines+markers',
    connectgaps: true,
    name: "Americas",
    marker:{
      color: '#2b6989', 
      width: 0.2
    }
  };

  let traceArabStates = {
    x: yearsRange,
    y: alldata.tracedata[dataType].ArabStates,
    mode: 'lines+markers',
    connectgaps: true,
    name: "ArabStates",
    marker:{
      color: '#4a86a5', 
      width: 0.2
    }
  };

  let traceAsiaPacific = {
    x: yearsRange,
    y: alldata.tracedata[dataType]["Asia-Pacicific"],
    mode: 'lines+markers',
    connectgaps: true,
    name: "AsiaPacific",
    marker:{
      color: '#68a6c3', 
      width: 0.2
    }
  };
  let traceCIS = {
    x: yearsRange,
    y: alldata.tracedata[dataType].CIS,
    mode: 'lines+markers',
    connectgaps: true,
    name: "CIS",
    marker:{
      color: '#86c6e1', 
      width: 0.2
    }
  };

  let traceEurope = {
    x: yearsRange,
    y: alldata.tracedata[dataType].Europe,
    mode: 'lines+markers',
    connectgaps: true,
    name: "Europe",
    marker:{
      color: '#a6e7ff', 
      width: 0.2
    }
  };

  let regionData = [traceAfrica, traceAmericas, traceArabStates, traceAsiaPacific, traceCIS, traceEurope];

  var layoutRegion = {
    title: dataType,
    showlegend: true
  };

  Plotly.newPlot('line-chart', regionData, layoutRegion);
};


// year slider for the world map using (data.)x variable to populate the slider value
function update_slider_value(x)
{
 document.getElementById("show_slider_value").innerHTML=x;
}

// Variable for the World Regions Gender Chart

let titleGender = 'Percentage of individuals using the Internet, by sex'
let genderData = JSON.parse(alldata.genderData)

let values = Object.values(genderData);


// Percentage of individuals using the Internet, by Gender
let genderTrace1 = {
  x: ['World', 'Africa', 'Americas', 'Arab States', 'Asia-Pacific', 'CIS', 'Europe'],
  y: values.map(each=>each['% Total 2020']),
  marker: {color:'#004c6d'
},
  name: '% Total 2020',
  type: 'bar'
};

let genderTrace2 = {
  x: ['World', 'Africa', 'Americas', 'Arab States', 'Asia-Pacific', 'CIS', 'Europe'],
  y: values.map(each=>each['% Female 2020']),
  marker: {color: '#6996b3'
},
  name: '% Female 2020',
  type: 'bar'
};

let genderTrace3 = {
  x: ['World', 'Africa', 'Americas', 'Arab States', 'Asia-Pacific', 'CIS', 'Europe'],
  y: values.map(each=>each['% Male 2020']),
  marker: {color: '#c1e7ff'
},
  name: '% Male 2020',
  type: 'bar'
};


let dataGender = [genderTrace1,genderTrace2,genderTrace3];

let layoutGender = {barmode: 'group'};

Plotly.newPlot('gender-plot', dataGender, layoutGender);


//  Variables for the World Regions Age Chart
let ageData = JSON.parse(alldata.ageData)
values = Object.values(ageData);
// Percentage of individuals using the Internet, by Age
let ageTrace1 = {
  x: ['World', 'Africa', 'Americas', 'Arab States', 'Asia-Pacific', 'CIS', 'Europe'],
  y: values.map(each=>each['% Total 2020']),
  marker: {color:'#004c6d'
},
  name: '% Total 2020',
  type: 'bar'
};

let ageTrace2 = {
  x: ['World', 'Africa', 'Americas', 'Arab States', 'Asia-Pacific', 'CIS', 'Europe'],
  y: values.map(each=>each['% Youth(15-24) 2020']),
  marker: {color:'#6996b3'
},
  name: '% Youth(15-24) 2020',
  type: 'bar'
};

let ageTrace3 = {
  x: ['World', 'Africa', 'Americas', 'Arab States', 'Asia-Pacific', 'CIS', 'Europe'],
  y: values.map(each=>each['% Rest of Population 2020']),
  marker: {color:'#c1e7ff'
},
  name: '% Rest of Population 2020',
  type: 'bar'
};

let dataAge = [ageTrace1, ageTrace2, ageTrace3];

let layoutAge = {barmode: 'group'};

Plotly.newPlot('age-plot', dataAge, layoutAge);