function getCBSACode(){
    console.log("getCBSACOde() called.");
    var address = document.getElementById('address').value;
    document.getElementById('rucacode').innerHTML = "Searching...";
    document.getElementById('cbsadesignation').innerHTML = "Searching...";
    $.ajax({
      type: "GET",
      url: "http://localhost:5000/",
      data: {"address":address},
      dataType: "jsonp",
      success: function(returndata)
      {
        document.getElementById('rucacode').innerHTML = returndata["RUCA_code"];
        document.getElementById('cbsadesignation').innerHTML = returndata["CBSA_designation"];
      },
      error: function(returndata)
        {
            document.getElementById('rucacode').innerHTML = "Searching...";
            document.getElementById('cbsadesignation').innerHTML = "Searching...";
        }
    });
}
