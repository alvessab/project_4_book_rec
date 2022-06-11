$(document).ready(function() {
    doWork();
});

function doWork() {
    var filepath = "static/data/goodreads_final_bagowords.csv";  
    requestD3(filepath, 'table');
}