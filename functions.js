function openExternalCBSA(){
    var cbsa = document.getElementById('cbsa').value;
    window.open("http://tbed.org/demo/index.php?table_name=CBSA&function=details&items_table_name=Place&where_field=CBSA_Code&where_value=" + cbsa);
}

function getCBSACode(){
    var address = document.getElementById('address').value;
    document.getElementById('cbsatype').innerHTML = address;
    $.ajax({
      type: "GET",
      url: "http://localhost:5000/",
      data: {"address":address},
      dataType: "jsonp",
      success: function(returndata)
      {
        document.getElementById('cbsatype').innerHTML = JSON.stringify(returndata);
      },
      error: function(returndata)
        {
            alert(JSON.stringify(returndata));
        }
    });
}
