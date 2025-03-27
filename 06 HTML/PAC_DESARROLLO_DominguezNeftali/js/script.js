// Este script lo ejecutamos en index, guarda la informacion en sessionStorage
function saveCompra(){
  sessionStorage.setItem("name",document.getElementById("name").value);
  sessionStorage.setItem("surname",document.getElementById("surname").value);
  sessionStorage.setItem("id",document.getElementById("id").value);
  sessionStorage.setItem("place",document.getElementById("place").value);
  sessionStorage.setItem("date",document.getElementById("date").value);
  sessionStorage.setItem("category",document.getElementById("category").value);
  sessionStorage.setItem("numberT",document.getElementById("numberT").value);
  
  var pay = document.querySelector('input[name="pay"]:checked');
  
  if (pay) {
    sessionStorage.setItem("pay", pay.value);
  }

  sessionStorage.setItem("agreeTerms",document.getElementById("agreeTerms").checked);
}



function loadCompra(){
////// Con sessionStorage
  const name = sessionStorage.getItem("name");
  const surname = sessionStorage.getItem("surname");
  const id = sessionStorage.getItem("id");
  const place = sessionStorage.getItem("place");
  const date = sessionStorage.getItem("date");
  const category = sessionStorage.getItem("category");
  const numberT = sessionStorage.getItem("numberT");
  const pay = sessionStorage.getItem("pay");
  const agreeTerms = sessionStorage.getItem("agreeTerms");

  document.getElementById("name").textContent = name;
  document.getElementById("surname").textContent = surname;
  document.getElementById("id").textContent = id;
  document.getElementById("place").textContent = place;
  document.getElementById("date").textContent = date;
  document.getElementById("category").textContent = category;
  document.getElementById("numberT").textContent = numberT;
  document.getElementById("pay").textContent = pay;
  
  if (agreeTerms){
    document.getElementById("agreeTerms").textContent = 'De acuerdo';
  }
}
  ////// Sin SessionStorage
  // Obtener los parámetros de la URL
  // const params = new URLSearchParams(window.location.search);

  // Cogemos parametro a parametro para declararlos en una variable
  //const name = params.get("name");
  // const surname = params.get("surname");
  // const id = params.get("id");
  // const place = params.get("place");
  // const date = params.get("date");
  // const category = params.get("category");
  // const numberT = params.get("numberT");
  // const pay = params.get("pay");
  // const agreeTerms = params.get("agreeTerms"); //No hace falta, es un dato requerido
  
  // Mostrar la información que trae la página en la URL
  // console.log(params);

  // document.getElementById("name").textContent = name;
  // document.getElementById("surname").textContent = surname;
  // document.getElementById("id").textContent = id;
  // document.getElementById("place").textContent = place;
  // document.getElementById("date").textContent = date;
  // document.getElementById("category").textContent = category;
  // document.getElementById("numberT").textContent = numberT;
  // document.getElementById("pay").textContent = pay;
  // document.getElementById("agreeTerms").textContent = 'De acuerdo';

  // if ( agreeTerms == "on") {
  // }