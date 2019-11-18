function generateMealGraphs(mealData) {
  console.log("mealData: " + mealData);

  var dateToNutrition = createNutritionMap(mealData);
  var calories_total = [];
  var calories_protein = [];
  var calories_fat = [];
  var calories_carb = [];
  var dates = [];

  calories_total.push("Calories");
  console.log("map");
  console.log(dateToNutrition);
  // extract all this data that each date maps to into an array for each field,
  // with each array having an entry for every date
  dateToNutrition.forEach((value, key, map) => {
    calories_total.push(value.calories);
    calories_protein.push(parseInt(value.protein_grams) * 4);
    calories_fat.push(parseInt(value.fat_grams) * 9);
    calories_carb.push(parseInt(value.carb_grams) * 4);
    var date = new Date(key);
    dates.push(
      date.getFullYear() +
        "-" +
        parseInt(date.getMonth() + 1) +
        "-" +
        date.getDate()
    );
  });
  alert("boom");
  alert(dates);
  alert(calories_carb);
  console.log("dates " + dates);
  console.log(calories_carb);
  createMacroBarGraph(dates, calories_carb, calories_fat, calories_protein);
  createMacroDonutGraph(calories_carb, calories_fat, calories_protein);
}

// takes in an array of meal objects and returns a map from each date to
// an object aggregating data for that date
function createNutritionMap(mealData) {
  var dateToNutrition = new Map();
  // map from a date to an object holding all data for the date
  for (index in mealData) {
    console.log("index: " + index);
    var meal = mealData[index];
    console.log("meal: " + meal.date);
    if (dateToNutrition.has(meal.date)) {
      var dateNutritionObject = dateToNutrition.get(meal.date);
      dateNutritionObject.calories += parseInt(meal.calories);
      dateNutritionObject.protein_grams += parseInt(meal.protein_grams);
      dateNutritionObject.fat_grams += parseInt(meal.fat_grams);
      dateNutritionObject.carb_grams += parseInt(meal.carb_grams);
    } else {
      dateToNutrition.set(meal.date, {
        calories: parseInt(meal.calories),
        protein_grams: parseInt(meal.protein_grams),
        fat_grams: parseInt(meal.fat_grams),
        carb_grams: parseInt(meal.carb_grams)
      });
    }
  }

  return dateToNutrition;
}

// creates stacked bar chart for macros
function createMacroBarGraph(
  dates,
  calories_carb,
  calories_fat,
  calories_protein
) {
  var chart = c3.generate({
    bindto: "#chart1",
    title: "Macronutrient Breakdown by Day",
    data: {
      x: "Dates",
      xFormat: "%Y-%m-%d",
      columns: [
        ["Dates", ...dates],
        ["Protein Calories", ...calories_protein],
        ["Carb Calories", ...calories_carb],
        ["Fat Calories", ...calories_fat]
      ],
      type: "bar",
      groups: [["Protein Calories", "Carb Calories", "Fat Calories"]]
    },
    axis: {
      x: {
        type: "category",
        tick: {
          format: "%Y-%m-%d"
        },
        label: {
          text: "Date",
          position: "outer-center"
        }
      },
      y: {
        label: {
          text: "Calories",
          position: "outer-middle"
        }
      }
    }
  });
}

// creates donut graph to show % of total calories for each macro
function createMacroDonutGraph(calories_carb, calories_fat, calories_protein) {
  var chart = c3.generate({
    bindto: "#chart2",
    data: {
      columns: [
        ["Protein Calories", ...calories_protein],
        ["Carb Calories", ...calories_carb],
        ["Fat Calories", ...calories_fat]
      ],
      type: "donut" //,
    },
    donut: {
      title: "Macronutrient Breakdown"
    }
  });
}
