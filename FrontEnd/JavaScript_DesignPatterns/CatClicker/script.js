window.onload = function () {
    var $cat1Elm = document.getElementById('catImg1');
    var $cat2Elm = document.getElementById('catImg2');

    var $cat1Div = document.getElementById('cat1Div')
    var $cat2Div = document.getElementById('cat2Div')

    var cat1Counter = 0;
    var cat2Counter = 0;

    $cat1Elm.addEventListener('click', function () {
        cat1Counter++;
        $cat1Div.innerText = cat1Counter.toString()
    })

    $cat2Elm.addEventListener('click', function () {
        cat2Counter++;
        $cat2Div.innerText = cat2Counter.toString()
    })
}