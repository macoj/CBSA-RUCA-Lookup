function openExternalCBSA(){
    var cbsa = document.getElementById('cbsa').value;
    window.open("http://tbed.org/demo/index.php?table_name=CBSA&function=details&items_table_name=Place&where_field=CBSA_Code&where_value=" + cbsa);
}

function getCBSACode(){
    var cbsa = document.getElementById('cbsa').value;
    document.getElementById('cbsatype').innerHTML = "asdf";
    $.ajax({
      type: "POST",
      url: "http://0.0.0.0:5000/",
      data: {"this is a request"},
      success: function(data)
      {
          alert("Successful");
      },
      error: function(data)
        {
            alert("fail");
        }
    });
}
