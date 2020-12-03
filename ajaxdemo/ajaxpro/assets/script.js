//window.onload = "ajax_save()"

function ajax_save(){
    btns = document.getElementById("btn_save");
    btns.onclick = savebook;
}
function savebook(){
    var name = document.getElementById("name").value;
    var price = document.getElementById("price").value;
    var pages = document.getElementById("pages").value;
    var url = "/save_book1?name="+name+"&price="+price+"&pages="+pages;
       alert("inside ajax" +url);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        alert(this.responseText);
         document.getElementById("showbookdata").innerHTML = this.responseText
//        var data = eval(this.responseText);
//        alert(data[0].name);
//        document.getElementById("showbookdata").innerHTML = data[0].name;
    }
  };
  xhttp.open("GET", url, true);
  xhttp.send();
}