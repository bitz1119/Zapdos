var data_Speeding_crime = 0 ;

Plotly.d3.csv('https://raw.githubusercontent.com/singhsanket143/Zapdos/master/mapbox/dataset.csv', function(err, rows){

  var classArray = unpack(rows, 'problem');
  var classes = [...new Set(classArray)];
  // console.log(classes);
  // console.log(classArray);
  function unpack(rows, key) {
    return rows.map(function(row) { return row[key]; });
  }

  var data = classes.map(function(classes) {
    var rowsFiltered = rows.filter(function(row) {
        return (row.problem === classes);
    });
    return {
       type: 'scattermapbox',
       name: classes,
       lat: unpack(rowsFiltered, 'Latitude'),
       lon: unpack(rowsFiltered, 'Longitude')
    };
  });
  console.log(data);
  // console.log(rows);

  var layout = {
	 title: 'Problem Mapping',
	 font: {
		 color: 'white'
	 },
    dragmode: 'zoom',
    mapbox: {
      center: {
        lat: 25.42 ,
        lon: 81.56
      },
      domain: {
        x: [0, 1],
        y: [0, 1]
      },
      style: 'dark',
      zoom: 5
    },
    margin: {
      r: 20,
      t: 40,
      b: 20,
      l: 20,
      pad: 0
    },
    paper_bgcolor: '#191A1A',
    plot_bgcolor: '#191A1A',
    showlegend: true,
	 annotations: [{
		 x: 0,
       y: 0,
       xref: 'paper',
       yref: 'paper',
		 text: 'Problem Mapping',
		 showarrow: false
	 }]
  };







    var layout_2 = {
  	 title: 'Problem Mapping',
  	 font: {
  		 color: 'white'
  	 },
      dragmode: 'zoom',
      mapbox: {
        center: {
          lat: 25.42 ,
          lon: 81.56
        },
        domain: {
          x: [0, 1],
          y: [0, 1]
        },
        style: 'dark',
        zoom: 5
      },
      margin: {
        r: 20,
        t: 40,
        b: 20,
        l: 20,
        pad: 0
      },
      paper_bgcolor: '#191A1A',
      plot_bgcolor: '#191A1A',
      showlegend: true,
  	 annotations: [{
  		 x: 0,
         y: 0,
         xref: 'paper',
         yref: 'paper',
  		 text: 'Problem Mapping',
  		 showarrow: false
  	 }]
    };





  Plotly.setPlotConfig({
    mapboxAccessToken: 'pk.eyJ1IjoicmlzaGFiLXNoYXJtYSIsImEiOiJjamVsNnh5N3QxZXcwMzNudWJ4YWM4eTJiIn0.eBysOBBUyW6GZvYCTLDSgQ'
  });

  // Plotly.plot('graphDiv', data, layout);



  var abc = Plotly ;


   Plotly.d3.csv('https://raw.githubusercontent.com/singhsanket143/Zapdos/master/mapbox/speed.csv',  function(err2, rows_new){


           console.log(rows_new);
           // var classArray_new = unpack_new(rows_new, 'problem');
           // var classes_new = [...new Set(classArray_new)];
           //
           // function unpack_new(rows_new, key) {
           //   return rows_new.map(function(row) { return row[key]; });
           // }
           //
           // var data_new = classes_new.map(function(classes_new) {
           //   var rowsFiltered = rows_new.filter(function(row) {
           //       return (row.problem === classes_new);
           //   });
           //   return {
           //      type: 'scattermapbox',
           //      name: classes_new,
           //      lat: unpack_new(rowsFiltered, 'Latitude'),
           //      lon: unpack_new(rowsFiltered, 'Longitude')
           //   };
           // });




    var c = 0;

    var counter = 0;

    var refresh = setInterval(function() {

      if(!(c==0)) {
        abc.deleteTraces('graphDiv' , [-2 , -1]) ;
        c=1;
      }
      console.log(data_new);
      console.log(counter, counter+4, data_new.length);
      if(counter+4>=data_new.length) {
        clearInterval(refresh);
      }
      window['data_Speeding_crime'] = data_new ;

      abc.plot('graphDiv', raw_data , layout) ;
      counter = counter+4;


    }, 1000);


    // console.log(data_new);







  });









  // Plotly.plot('graphDiv', data_Speeding_crime , layout);






});





//
//
//
// Plotly.d3.csv('https://raw.githubusercontent.com/singhsanket143/Zapdos/master/mapbox/spped.csv', function(err, rows){
//
//   var classArray = unpack(rows, 'problem');
//   var classes = [...new Set(classArray)];
//   console.log(classes);
//   console.log(classArray);
//   function unpack(rows, key) {
//     return rows.map(function(row) { return row[key]; });
//   }
//
//   var data = classes.map(function(classes) {
//     var rowsFiltered = rows.filter(function(row) {
//         return (row.problem === classes);
//     });
//     return {
//        type: 'scattermapbox',
//        name: classes,
//        lat: unpack(rowsFiltered, 'Latitude'),
//        lon: unpack(rowsFiltered, 'Longitude')
//     };
//   });
//   console.log(data);
//   console.log(rows);
//
//   var layout = {
// 	 title: 'Problem Mapping',
// 	 font: {
// 		 color: 'white'
// 	 },
//     dragmode: 'zoom',
//     mapbox: {
//       center: {
//         lat: 25.42 ,
//         lon: 81.56
//       },
//       domain: {
//         x: [0, 1],
//         y: [0, 1]
//       },
//       style: 'dark',
//       zoom: 12
//     },
//     margin: {
//       r: 20,
//       t: 40,
//       b: 20,
//       l: 20,
//       pad: 0
//     },
//     paper_bgcolor: '#191A1A',
//     plot_bgcolor: '#191A1A',
//     showlegend: true,
// 	 annotations: [{
// 		 x: 0,
//        y: 0,
//        xref: 'paper',
//        yref: 'paper',
// 		 text: 'Problem Mapping',
// 		 showarrow: false
// 	 }]
//   };
//
//   Plotly.setPlotConfig({
//     mapboxAccessToken: 'pk.eyJ1IjoicmlzaGFiLXNoYXJtYSIsImEiOiJjamVsNnh5N3QxZXcwMzNudWJ4YWM4eTJiIn0.eBysOBBUyW6GZvYCTLDSgQ'
//   });
//
//   Plotly.plot('graphDiv', data, layout);
// });
