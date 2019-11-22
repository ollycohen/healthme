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
    if($('#recipe-query').val() && $('#should-query').checked){
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
                console.log(json.totalNutrients.CHOCDF.quantity)
                //$('#carbs-query').value = json.totalNutrients.CHOCDF.quantity;
                $('#carbs-query').html(0); 

            },
            
            error : function(xhr, errmsg, err){
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }
}