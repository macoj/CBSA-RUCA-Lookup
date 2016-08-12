function openExternalCBSA(){
    var cbsa = document.getElementById('cbsa').value;
    window.open("http://tbed.org/demo/index.php?table_name=CBSA&function=details&items_table_name=Place&where_field=CBSA_Code&where_value=" + cbsa);
}

function getCBSACode(){
    var cbsa = document.getElementById('cbsa').value;
    document.getElementById('cbsatype').innerHTML = "asdf";
    $.ajax('http://jsonp-aware-endpoint.com/user', {
        jsonp: 'callback',
        dataType: 'jsonp',
        data: {
            id: 123
        }
    }).then(function(response) {
        // handle requested data from server
    });

}
