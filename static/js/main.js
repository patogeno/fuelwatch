$(function() {

    $(".stationsForm form").submit(function(event){
        event.preventDefault();
        var suburb = document.forms['stationForm']['suburbsSelect'].value;
        var productId = document.forms['stationForm']['productsSelect'].value;
        var url = '/' + suburb + '/' + productId;
        window.open(url,"_self");
    });
    
});