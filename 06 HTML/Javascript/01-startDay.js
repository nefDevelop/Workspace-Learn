//load json

//changePass

document.getElementById("password").addEventListener("input", function () {
  let message = this.value;
  console.log(message);

  document.getElementById("passChange").textContent = message;
});

document
  .getElementById("togglePassword")
  .addEventListener("click", function () {
    let passwordInput = document.getElementById("password");
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      this.innerHTML = "&#128064;"; // Icono de ojo abierto
    } else {
      passwordInput.type = "password";
      this.innerHTML = "🔒"; // Icono de ojo cerrado
    }
  });

function copiarAlPortapapeles() {
  const contenido = document.getElementById("contenido").textContent;
  navigator.clipboard
    .writeText(contenido)
    .then(() => {
      alert("Texto copiado al portapapeles!");
    })
    .catch((err) => {
      console.error("Error al copiar: ", err);
    });
}
