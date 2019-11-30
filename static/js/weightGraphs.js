function generateWorkoutGraphs(workoutData) {
  var exerciseToWorkoutsForThatExerciseMap = generateExerciseMaps(workoutData);
  // map from exercise name to [
  //  ['excericse_name', ...1_rep_maxes_for_each_day],
  //  ['exercise_name + _dates, ...dates]
  // ]
  var nameToArrayWithOneRepMaxesAndDates = new Map();
  var xs = {};
  var columns = [];

  //   exerciseToWorkoutsForThatExerciseMap.forEach((value, key, map) => {
  for (const [key, value] of exerciseToWorkoutsForThatExerciseMap.entries()) {
    // const value = exerciseToWorkoutsForThatExerciseMap.get(key);
    // results for each excercise will have a map from date to weight
    var results = [];
    var dateToWeight = new Map();
    for (var i = 0; i < value.length; i++) {
      dateToWeight.set(new Date(value[i].date), value[i].weight);
    }

    // sort this map based on date (key), taken from https://stackoverflow.com/questions/31158902/is-it-possible-to-sort-a-es6-map-object
    var sortedMap = new Map(
      [...dateToWeight].sort((a, b) => (a[0] > b[0] ? 1 : -1))
    );
    var dateArray = [];
    var weightArray = [];

    sortedMap.forEach((weight, date, map) => {
      dateArray.push(
        date.getFullYear() +
          "-" +
          parseInt(date.getMonth() + 1) +
          "-" +
          date.getDate()
      );
      weightArray.push(weight);
    });

    weightArray.unshift(key);
    dateArray.unshift(key + "_dates");
    // show that the weight array and date array map to eachother for the graph
    xs["" + key] = key + "_dates";
    columns.push(dateArray);
    columns.push(weightArray);
    console.log(dateArray);
  }
  var chart = c3.generate({
    data: {
      xs: xs,
      xFormat: "%Y-%m-%d",
      columns: columns
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
          text: "Weight",
          position: "outer-middle"
        }
      }
    }
  });
}

// returns a map from each exercise to an array of the data for that exercise
function generateExerciseMaps(workoutData) {
  var exercises = new Map();
  workoutData.forEach(workout => {
    if (exercises.has(workout.exercise_name)) {
      exercises.get(workout.exercise_name).push(workout);
    } else {
      var workoutArray = [];
      workoutArray.push(workout);
      exercises.set(workout.exercise_name, workoutArray);
    }
  });
  return exercises;
}

function generateWeightGraphs(weightData) {
  console.log("generating weight graph");
  var weightArray = [];
  var dates = [];
  weightData.forEach(weight => {
    weightArray.push(weight.weight);
    date = new Date(weight.date);
    dates.push(
      date.getFullYear() +
        "-" +
        parseInt(date.getMonth() + 1) +
        "-" +
        date.getDate()
    );
  });
  console.log(dates);
  var chart = c3.generate({
    bindto: "#graph",
    data: {
      x: "Dates",
      xFormat: "%Y-%m-%d",
      columns: [
        ["Dates", ...dates],
        ["Weight", ...weightArray]
        // ["data1", 30, 200, 100, 400, 150, 250],
        // ["data2", 50, 20, 10, 40, 15, 25]
      ]
    },
    axis: {
      x: {
        type: "category",
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
          text: "Weight",
          position: "outer-middle"
        }
      }
    }
  });
}
