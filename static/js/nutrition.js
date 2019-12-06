$('#id_food_name').on('blur', function(event){
    event.preventDefault();
    console.log("blur")
    query_macros();
});

$('#id_autofill_macros').on('change', function(evenet){
    console.log($('#id_autofill_macros').val())
    query_macros();
});

function query_macros(){
    if($('#id_food_name').val() && $('#id_autofill_macros').prop("checked")){
        var ingredParam = encodeURI($('#id_food_name').val())
        var ingredParams = $('#id_food_name').val()
        var url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
        console.log(ingredParam)

        $.ajax({
            url: url,
            headers: {
                'X-RapidAPI-Host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com',
                'X-RapidAPI-Key': 'adf5f496e3msh6d36ddf1155e6e2p113747jsnca35354e5b7e'
            },
            data: {query: ingredParams, number: "10"},
            type: "GET",
            dataType: 'JSON',
            contentType: 'application/json; charset=utf-8',

            success : function(json){
                console.log(json)


                var id = json.results[0].id
                var urlNutrition =  'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/' + id + '/nutritionWidget.json'

                $.ajax({
                    url: urlNutrition,
                    headers: {
                        'X-RapidAPI-Host': 'spoonacular-recipe-food-nutrition-v1.p.rapidapi.com',
                        'X-RapidAPI-Key': 'adf5f496e3msh6d36ddf1155e6e2p113747jsnca35354e5b7e'
                    },
                    type: "GET",
                    dataType: 'JSON',
                    contentType: 'application/json; charset=utf-8',
                    success : function(json){
                        var carb_count = json.carbs
                        carb_count = carb_count.substring(0, carb_count.length-1)

                        var fat_count = json.fat
                        fat_count = fat_count.substring(0, fat_count.length-1)

                        var protein_count = json.protein
                        protein_count = protein_count.substring(0, protein_count.length-1)

                        $('#id_grams_of_carbs').val(carb_count); 
                        $('#id_grams_of_fat').val(fat_count); 
                        $('#id_grams_of_protein').val(protein_count); 
    
                        $('#id_grams_of_carbs').siblings("label").addClass("active")
                        $('#id_grams_of_fat').siblings("label").addClass("active")
                        $('#id_grams_of_protein').siblings("label").addClass("active")
                    },
                    error : function(xhr, errmsg, err){
                        console.log("error")
                    }
                });
        },
            error : function(xhr, errmsg, err){
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }
}