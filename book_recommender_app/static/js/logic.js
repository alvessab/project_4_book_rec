$(document).ready(function() {
    console.log("Page Loaded");

    $("#search").click(function() {
        // alert("button clicked!");
        recommendation_df();
    });
});

// call Flask API endpoint
function recommendation_df() {
    var bookTitle = $("#nlp_request").val();
    var rating_min = $("#rating").val();

    // check if inputs are valid

    // create the payload
    var payload = {
        "bookTitle": bookTitle,
        "rating_min": rating_min
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/nlp",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);

            if (returnedData["recommendation"]) {
                $("#output").text("output");
            } else {
                $("#output").text("No Recommendations :(");
            }
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

};