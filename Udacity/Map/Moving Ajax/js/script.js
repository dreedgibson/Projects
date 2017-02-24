
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview

    // get the street and city name
    var street = $('#street').val();
    var city = $('#city').val();
    var apikey = 'AIzaSyAsKoUUZ9ovsA0mcL_bejTdUj1q76KH2pM';
    var location = street + ', ' + city;

    $greeting.text('Showing ' + location);
    var url = 'https://maps.googleapis.com/maps/api/streetview?size=600x400&location=' + location + '&key=' + apikey;
    $body.append("<img class='bgimg' src='" + url + "'>");

    var urlNY = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    urlNY += '?' + $.param({
        'api-key': "9ef7d9380fe6449aacafceaf6f936c20",
        'q': city,
        'fl': "headline,web_url,snippet,multimedia"
    });

    $.getJSON(urlNY, function( data ) {
        articles = data['response']['docs'];
        $nytHeaderElem.text('Articles from the New York times about: ' + city);
        articles.forEach(function(article) {
            $('#nytimes-articles').append('<li class="article-item"><a href="' + article.web_url + '">' + article.headline.main + '</a></li>');
            $('.article-item:last').append('<p>' + article.snippet + '</p>');
        });
    }).fail(function(e) {
         $nytHeaderElem.text('New York Times Articles could not be loaded');
    });


    var urlWiki = 'https://en.wikipedia.org/w/api.php?' + $.param({
        action: 'opensearch',
        format: 'json',
        search: city,
        limit: '20',
        origin: '*'
    })
    $.getJSON(urlWiki,function(data) {
        console.log(data);
        for (var i = 0; i < data[1].length; i++) {
            $wikiElem.append('<li><a href="' + data[3][i] + '">' + data[1][i] + '</a></li>'); 
        }     
    }).fail(function(e) {
        $wikiElem.text("failed to get wikipedia resources")
    });
    
    return false;
};

$('#form-container').submit(loadData);
