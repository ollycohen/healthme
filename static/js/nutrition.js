// setting up spinner while request is loading
jQuery.ajaxSetup({
  beforeSend: function() {
    var inputFormElements = $("#loader").show();
  },
  complete: function() {
    $("#loader").hide();
  },
  success: function() {}
});

$("#id_food_name").on("blur", function(event) {
  event.preventDefault();
  console.log("blur");
  query_macros();
});

$("#id_autofill_macros").on("change", function(evenet) {
  console.log($("#id_autofill_macros").val());
  query_macros();
});

function query_macros() {
  if ($("#id_food_name").val() && $("#id_autofill_macros").prop("checked")) {
    var ingredParam = encodeURI($("#id_food_name").val());
    // hide other form entries, display spinner while waiting for request
    $.ajax({
      url:
        "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search",
      headers: {
        "X-RapidAPI-Host":
          "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "adf5f496e3msh6d36ddf1155e6e2p113747jsnca35354e5b7e",
        "Access-Control-Allow-Origin": "*"
      },
      data: { query: ingredParam },
      type: "GET",
      dataType: "json",
      beforeSend: function() {
        // hide all form elements after food name
        var inputFormElements = $("#nutrition-form")[0].children;
        // first 3 children are the food name field and checkbox for autofilling macros
        for (var i = 3, element; (element = inputFormElements[i++]); ) {
          $(element).hide();
        }
        // show spinner
        $(".start-hidden").css("visibility", "visible");
        $(".start-hidden").show();
      },
      complete: function() {
        // hide all form elements after food name
        var inputFormElements = $("#nutrition-form")[0].children;
        // first 3 children are the food name field and checkbox for autofilling macros
        for (var i = 3, element; (element = inputFormElements[i++]); ) {
          $(element).show();
        }
        // show spinner
        $(".start-hidden").css("visibility", "hidden");
        // $(".start-hidden").show();
      },

      success: function(json) {
        // check for empty result(food not found)
        if (json.results.length == 0) {
          M.toast({
            html:
              "Nutrition results not found! Please manually enter the macronutrients."
          });

          // clear out old macronutrient results
          $("#id_grams_of_carbs").val(0);
          $("#id_grams_of_fat").val(0);
          $("#id_grams_of_protein").val(0);
          $("#id_grams_of_carbs")
            .siblings("label")
            .addClass("active");
          $("#id_grams_of_fat")
            .siblings("label")
            .addClass("active");
          $("#id_grams_of_protein")
            .siblings("label")
            .addClass("active");
          return;
        }

        var id = json.results[0].id;
        var urlNutrition =
          "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" +
          id +
          "/nutritionWidget.json";

        $.ajax({
          url: urlNutrition,
          headers: {
            "X-RapidAPI-Host":
              "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            "X-RapidAPI-Key":
              "adf5f496e3msh6d36ddf1155e6e2p113747jsnca35354e5b7e",
            "Access-Control-Allow-Origin": "*"
          },
          type: "GET",
          dataType: "json",

          success: function(json) {
            console.log(json);
            console.log("UPDATED");

            var carb_count = 0;
            var protein_count = 0;
            var fat_count = 0;
            if (json.carbs) {
              carb_count = parseInt(
                json.carbs.substring(0, json.carbs.length - 1)
              );
            }
            if (json.carbs) {
              protein_count = parseInt(
                json.protein.substring(0, json.protein.length - 1)
              );
            }
            if (json.fat) {
              fat_count = parseInt(json.fat.substring(0, json.fat.length - 1));
            }

            console.log(carb_count);
            $("#id_grams_of_carbs").val(carb_count);
            $("#id_grams_of_fat").val(fat_count);
            $("#id_grams_of_protein").val(protein_count);

            $("#id_grams_of_carbs")
              .siblings("label")
              .addClass("active");
            $("#id_grams_of_fat")
              .siblings("label")
              .addClass("active");
            $("#id_grams_of_protein")
              .siblings("label")
              .addClass("active");
          },

          error: function(xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
          }
        });

        console.log(json);
        console.log("UPDATED");
        if (json.results[0]) {
          var carb_count = json.results[0].carbs
            ? Math.round(json.results[0].carbs)
            : 0;
          var protein_count = json.results[0].protein
            ? Math.round(json.results[0].protein)
            : 0;
          var fat_count = json.results[0].fat
            ? Math.round(json.results[0].fat)
            : 0;

          console.log(carb_count);
          $("#id_grams_of_carbs").val(carb_count);
          $("#id_grams_of_fat").val(fat_count);
          $("#id_grams_of_protein").val(protein_count);

          $("#id_grams_of_carbs")
            .siblings("label")
            .addClass("active");
          $("#id_grams_of_fat")
            .siblings("label")
            .addClass("active");
          $("#id_grams_of_protein")
            .siblings("label")
            .addClass("active");
        }
      },

      error: function(xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText);
        console.log("NOT FOUND");
      }
    });
  }
}
