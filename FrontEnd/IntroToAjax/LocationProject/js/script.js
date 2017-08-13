
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    var street = $('#street').val();
    var city = $('#city').val();

    var address = street + ' , ' + city;
    var url = 'http://maps.googleapis.com/maps/api/streetview?size=600x300&location=' + address + '';
   // $.ajax();

    $body.append('<img class="bgimg" src="' +  url +  '" />')
    
    // NewYork API Use

    var nyurl = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=' + address + "&apikey=375acff6fecf4c06b7946ad5ad82c6fa";
    $.getJSON(nyurl , null , function(data) {
        $nytHeaderElem.text(street +  ' Articles')
        data.response.docs.forEach(function(elm) {
            $nytElem.append('<li class="article">' + elm.snippet + '</li>')
        });
    })

    return false;
};

$('#form-container').submit(loadData);
