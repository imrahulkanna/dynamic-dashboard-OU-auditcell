function courseSearch() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput2");
    filter = input.value.toUpperCase();
    finalFilter = filter.replace(/[^a-zA-Z]/g, '');
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().replace(/[^a-zA-Z]/g, '').indexOf(finalFilter) > -1) {
            a[i].style.display = "";
        }
        else {
            a[i].style.display = "none";
        }
    }
}

function clgSearch() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    finalFilter = filter.replace(/[^a-zA-Z]/g, '');
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[3];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().replace(/[^a-zA-Z]/g, '').indexOf(finalFilter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function prgrmSearch() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    finalFilter = filter.replace(/[^a-zA-Z]/g, '');
    table = document.getElementById("course-table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().replace(/[^a-zA-Z]/g, '').indexOf(finalFilter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}


// function globalSearchfn() {
//     var input, filter, table, tr, td, i, txtValue;
//     input = document.getElementById("gsearchId");
//     filter = input.value.toUpperCase();
//     finalFilter = filter.replace(/[^0-9a-zA-Z]/g, '');
//     table = document.getElementById("searchTable");
//     tr = table.getElementsByTagName("tr");
//     for (i = 0; i < tr.length; i++) {
//         for (j = 0; j < 7; j++) {
//             td = tr[i].getElementsByTagName("td")[j];
//             if (td) {
//                 txtValue = td.textContent || td.innerText;
//                 if (txtValue.toUpperCase().replace(/[^a-zA-Z]/g, '').indexOf(finalFilter) > -1) {
//                     tr[i].style.display = "";
//                 } else {
//                     tr[i].style.display = "none";
//                 }
//             }
//         }
//     }
// }

function customSearch() {
    var input, filter, table, tr, td, i, txtValue;
    table = document.getElementById("searchTable");
    tr = table.getElementsByTagName("tr");
    console.log(tr)
     if (tr.length > 2 && tr[2].outerText!="No matching records found") {
        var search = new Set();
        for (i = 2; i < tr.length; i++) { //i=2 since first 2 are header rows<exempt them!>
            td = tr[i].getElementsByTagName("td")[4];
            search.add(td.innerHTML);
        }
        console.log(search);
        document.getElementById("clgCount").innerHTML = search.size;
    }
    else {
        document.getElementById("clgCount").innerHTML = 0;
    }
}
