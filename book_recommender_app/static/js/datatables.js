$(document).ready(function() {
    console.log("Page Loaded");

    getData();
});

function getData() {
    let filepath = "../static/data/goodreads_cleaned.csv";

    d3.csv(filepath).then(function(data) {
        // console.log(data);

    

        // do work
        let first_row = data[0];
        // console.log(first_row)
        let columns = Object.keys(first_row);
        // console.log(columns)
        let header_html = "<tr>"
           
        for (let i = 0; i < 11; i++) {
            col = columns[i];
            header_html += `<th>${col}</th>`;
        }
        header_html += "</tr>";

        $("#GOODREADS thead").append(header_html);

        // same thing, but for tbody
        let body_html = "";
        for (let j = 0; j < data.length; j++) {
            let row = data[j];
            console.log(row)
            let vals = Object.values(row);
            console.log(vals)
            let row_html = "<tr>"

            for (let k = 0; k < 11; k++) {
                val = vals[k];
                row_html += `<td>${val}</td>`;
            }
            row_html += "</tr>"
            body_html += row_html
        }

        $("#GOODREADS tbody").append(body_html);

        // add class
        // $("#GOODREADS").attr("class", "table table-striped table-hover");
        // $('#GOODREADS').DataTable();
    });
}

