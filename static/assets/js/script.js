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


function customSearch() {
    var table, tr, td, i;
    table = document.getElementById("searchTable");
    tr = table.getElementsByTagName("tr");
    //console.log(tr)
     if (tr.length > 2 && tr[2].outerText!="No matching records found") {
        var search = new Set();
        for (i = 2; i < tr.length; i++) { //i=2 since first 2 are header rows<exempt them!>
            td = tr[i].getElementsByTagName("td")[4];
            search.add(td.innerHTML);
        }
       // console.log(search);
        document.getElementById("clgCount").innerHTML = search.size;
    }
    else {
        document.getElementById("clgCount").innerHTML = 0;
    }

// above code displays the count of distinct colleges for options selected
// below code displays the selected dropdown option as summary

    var avail_opts = {
        'programtag':'Program',
        'coursetag':'Course',
        'subcoursetag':'SubCourse'
    }; // to display more summary add the required Ids into the dictionary/object
       // here keys are Ids associated to the summary <p> tags in custom search page
       // values are the text to be displayed

    var td = tr[1].getElementsByTagName('td');
    var opt = document.getElementsByClassName('searchDropdown') 
    
    for (i = 0; i < Object.keys(avail_opts).length;i++) {
        var opt_selected = opt[i].options[opt[i].selectedIndex].text;
        if (opt_selected === 'ALL') {
            document.getElementById(Object.keys(avail_opts)[i]).innerHTML = ''
        }
        else if (opt_selected!='ALL') {
            document.getElementById(Object.keys(avail_opts)[i]).innerHTML = avail_opts[Object.keys(avail_opts)[i]]+' Selected: ' + opt_selected
        
            if (Object.keys(avail_opts)[i] === 'coursetag') {
                document.getElementById(Object.keys(avail_opts)[i]).innerHTML += "  |   "
            }
        }
    }
}
