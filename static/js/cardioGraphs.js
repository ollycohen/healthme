generateCardioGraphs = cardioData => {
  var mapDateToCardio = createCardioMap(cardioData);
  var dates = [];
  var distanceTotals = [];
  var durationTotals = [];
  var mapTypeToNumberOfTimesThatTimeIsPerformed = new Map();

  // sum up values for each day
  mapDateToCardio.forEach((value, key, map) => {
    distanceTotals.push(value.distance);
    durationTotals.push(value.duration);

    let previousAmountThisTypeHasBeenPerformed = mapTypeToNumberOfTimesThatTimeIsPerformed.has(
      value.type
    )
      ? mapTypeToNumberOfTimesThatTimeIsPerformed.get(value.type)
      : 0;

    mapTypeToNumberOfTimesThatTimeIsPerformed.set(
      value.type,
      previousAmountThisTypeHasBeenPerformed + 1
    );

    var date = new Date(key);
    dates.push(
      date.getFullYear() +
        "-" +
        parseInt(date.getMonth() + 1) +
        "-" +
        date.getDate()
    );
  });

  generateCardioDistanceGraph(dates, distanceTotals);
};

function createCardioMap(cardioData) {
  var dateToCardio = new Map();
  // map from a date to an object holding all data for the date
  for (index in cardioData) {
    var cardio = cardioData[index];
    console.log("This is a cardio");
    console.log(cardio);
    if (dateToCardio.has(cardio.date)) {
      var cardio = dateToCardio.get(cardio.date);
      cardio.duration += parseFloat(cardio.protein_grams);
      cardio.distance += parseFloat(cardio.fat_grams);
    } else {
      dateToCardio.set(cardio.date, {
        type: cardio.type,
        duration: parseFloat(cardio.duration),
        distance: parseFloat(cardio.distance)
      });
    }
  }

  return dateToCardio;
}

generateCardioDistanceGraph = (dates, distanceTotals) => {
  console.log("dates");
  console.log(dates);
  console.log("distances");
  console.log(distanceTotals);
  var chart = c3.generate({
    bindto: "#cardioDistance",
    title: "Cardio Distance by Day",
    data: {
      x: "Dates",
      xFormat: "%Y-%m-%d",
      columns: [
        ["Dates", ...dates],
        ["Distance", ...distanceTotals]
      ]
    },
    axis: {
      x: {
        type: "timeseries",
        tick: {
          format: "%Y-%m-%d",
          rotate: 90,
          multiline: false
        },
        label: {
          text: "Date",
          position: "outer-center"
        }
      },
      y: {
        label: {
          text: "Distance",
          position: "outer-middle"
        }
      }
    }
  });
};
