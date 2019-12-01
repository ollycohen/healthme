$('#recipe-query').on('blur', function(event){
    event.preventDefault();
    console.log("blur")
    query_macros();
});

$('#should-query').on('change', function(evenet){
    console.log($('#should-query').val())
    query_macros();
});

function query_macros(){
    if($('#recipe-query').val() && $('#should-query').prop("checked")){
        var dataStr =  "app_id=ae4df3dc&app_key=88a35cbdea8755c723a9da95d2b83171&ingr="
        var ingredParam = encodeURI($('#recipe-query').val())
        dataStr = dataStr + ingredParam

        $.ajax({
            url: "https://api.edamam.com/api/nutrition-data",
            data: dataStr,
            type: "GET",
            dataType: "json",

            success : function(json){
                console.log(json);
                console.log("UPDATED")
                if(json.totalNutrients){
                    var carb_count = json.totalNutrients.CHOCDF ? Math.round(json.totalNutrients.CHOCDF.quantity) : 0;
                    var protein_count = json.totalNutrients.PROCNT ? Math.round(json.totalNutrients.PROCNT.quantity) : 0;
                    var fat_count = json.totalNutrients.FAT ? Math.round(json.totalNutrients.FAT.quantity) : 0;

                    console.log(carb_count)
                    $('#carbs-query').val(carb_count); 
                    $('#fat-query').val(fat_count); 
                    $('#protein-query').val(protein_count); 

                    $('#carbs-query').siblings("label").addClass("active")
                    $('#fat-query').siblings("label").addClass("active")
                    $('#protein-query').siblings("label").addClass("active")

                }
            },
            
            error : function(xhr, errmsg, err){
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }
}