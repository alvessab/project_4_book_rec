$(document).ready(function() {
    console.log("Page Loaded");

    $("#search").click(function() {
        // alert("button clicked!");
        knn_recommender();
        $("#output").show();
    });
});

// call Flask API endpoint
function knn_recommender() {
    var bookTitle = $("#bookTitle").val();

    // create the payload
    var payload = {
        "bookTitle": bookTitle,
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/knn",
        contentType: 'application/json;charset=UTF-8',
        // dataType: 'text json',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            // console.log(returnedData);
            var returnObject = JSON.parse(returnedData)
            console.log(returnObject.length);
            console.log(typeof returnObject);
            $('#output > tbody').empty();

            for (let i=0; i<returnObject.length; i++){
                let data = returnObject[i];

                let row = "<tr>";
                row += `<td><a href='${data.bookImage}' target='_blank'> <img src='${data.bookImage}'  width="100" height="150" ></a></td>`;
                row += `<td>${data.bookTitle}</td>`;
                row += `<td>${data.Author}</td>`;
                row += `<td>${data.bookDesc}</td>`;
                row += `<td>${data.Genre}</td>`;
                row += `<td>${data.bookRating}</td>`;
                $('#output > tbody').append(row);

            }
        },
        error: function(XMLHttpRequest) {
            alert("Unknown Book Title: Please see Data Table for spelling and availability!");
        }
    });

};