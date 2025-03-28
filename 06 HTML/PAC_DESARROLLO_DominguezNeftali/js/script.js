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

// Con esta funcion cargamos los datos del sessionStorage a los labels
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


  // Mientras escribimos, vamos comprobando los inputs
  document.getElementById('formulario').addEventListener('input', function(e) {
    // Detiene el envío automático
    e.preventDefault();
    let isValid = true;

    // console.log("input");

    // Resetear errores
    document.querySelectorAll('.invalid').forEach(el => el.classList.remove('invalid'));

    // Validar campos
    const name = document.getElementById('name');
    const surname = document.getElementById('surname');
    const id = document.getElementById('id');
    const place = document.getElementById("place");
    const date = document.getElementById("date");
    // const category = document.getElementById("category");
    const numberT = document.getElementById("numberT");
    const pay = document.querySelector('input[name="pay"]:checked');
    const agreeTerms = document.getElementById("agreeTerms");

    // Validar nombre
    if (!name.value.trim()) {
        name.classList.add('invalid');
        isValid = false;
    }
    
    if (!surname.value.trim()) {
        surname.classList.add('invalid');
        isValid = false;
    }
    
    // Validar dni
    if (id.value.length < 8) {
        id.classList.add('invalid');
        isValid = false;
    }
    
    // Validar select place
    if (!place.value) {
      place.classList.add('invalid');
      isValid = false;
    }

    // Validar select date
    if (!date.value) {
      date.classList.add('invalid');
      isValid = false;
    }

    if (!numberT.value.trim()) {
      numberT.classList.add('invalid');
      isValid = false;
    }
    if (!pay) {
      document.querySelectorAll('input[name="pay"]').forEach(el => el.classList.add('invalid'));
      isValid = false;
    }
    if (!agreeTerms.checked){
      agreeTerms.classList.add('invalid');
      isValid = false; 
    }
            
  });


  document.getElementById("submit").addEventListener("click", function(e){
    let isValid = true;
    e.preventDefault();

    // Validar campos
    const name = document.getElementById('name');
    const surname = document.getElementById('surname');
    const id = document.getElementById('id');
    const place = document.getElementById("place");
    const date = document.getElementById("date");
    // const category = document.getElementById("category");
    const numberT = document.getElementById("numberT");
    const pay = document.querySelector('input[name="pay"]:checked');
    const agreeTerms = document.getElementById("agreeTerms");

    
    // Validar nombre
    if (!name.value.trim()) {
        // console.log("name" + name.value.trim());
        name.classList.add('invalid');
        isValid = false;
    }
    
    if (!surname.value.trim()) {
        surname.classList.add('invalid');
        isValid = false;
    }
    
    // Validar dni
    if (id.value.length < 8) {
        id.classList.add('invalid');
        isValid = false;
    }

    // Validar select place
    if (!place.value) {
      // console.log("place" + place.value);
      place.classList.add('invalid');
      isValid = false;
    }

    // Validar select date
    if (!date.value) {
      date.classList.add('invalid');
      isValid = false;
    }

    if (!numberT.value) {
      numberT.classList.add('invalid');
      isValid = false;
    }

    if (!pay) {
      // console.log("pay" + pay);
      document.querySelectorAll('input[name="pay"]').forEach(el => el.classList.add('invalid'));
      isValid = false;
    }

    if (!agreeTerms.checked){
      // console.log("agree" + agreeTerms);
      agreeTerms.classList.add('invalid');
      isValid = false; 
    }

    // Console.log(isValid);
  
    // Si todo válido, guardamos info
    if (isValid) {
        //this.submit(); // Esto deberia enviarlo pero por más que lo intento me da error
        saveCompra();
        window.location.assign("confirmacion.html")

        console.log('Formulario válido, enviando...');
    } else {
        alert('Por favor corrija los errores');
        console.log('Por favor corrija los errores');
    }
  })


  
  //   let name = document.getElementById("name").value.trim();
  //   let surname = document.getElementById("surname").value.trim();
  //   let id = document.getElementById("id").value.trim();
  //   let place = document.getElementById("place").value;
  //   let date = document.getElementById("date").value;
  //   let category = document.getElementById("category").value;
  //   let numberT = document.getElementById("numberT").value;
  //   let pay = document.querySelector('input[name="pay"]:checked');
  //   let agreeTerms = document.getElementById("agreeTerms").checked;

  //   if (!name || !surname || !id || !place || !date || !category || !numberT || !pay || !agreeTerms) {
  //       alert("Por favor, completa todos los campos y acepta los términos.");
  //       return; // Detiene la función aquí
  //   }

  //   if (parseInt(numberT) <= 0 || isNaN(parseInt(numberT))) {
  //       alert("El número de entradas debe ser al menos 1.");
  //       return;
  //   }

  //   // Verificar que el formulario se seleccionó correctamente
  // if (form) {
  //     form.submit(); // Enviar el formulario correctamente
  // } else {
  //     console.error("No se encontró el formulario con id='form'");
  // }