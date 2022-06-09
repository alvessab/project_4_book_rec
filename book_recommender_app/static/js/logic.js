$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        recommendation_df();
    });
});



// call Flask API endpoint
function recommendation_df() {
    var bookTitle = $("#nlp_request").val();

    // check if inputs are valid

    // create the payload
    var payload = {
        "bookTitle": bookTitle
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/nlpRecommendations",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {


            // print it
            console.log(returnedData);

            $('#output > tbody').empty();

            for (let i=0; i<returnedData.recommendation.length; i++){
                let data = returnedData.recommendation[i];

                let row = "<tr>";
                row += `<td><a href='${data.Image}' target='_blank'> <img src='${data.Image}'  width="100" height="150" ></a></td>`;
                row += `<td>${data.Title}</td>`;
                row += `<td>${data.Author}</td>`;
                row += `<td>${data.Description}</td>`;
                row += `<td>${data.Genre}</td>`;
                row += `<td>${data.Rating}</td>`;
                row += `<td>${data.Score}</td>`;
                row += `<td><a  href='${data.URL}' target='_blank' >Link</a></td>`;
                $('#output > tbody').append(row);
            }
        },
        error: function(XMLHttpRequest) {
            alert("Unknown Book Title: Please see Data Table for spelling and availability!");
        }
    });

};