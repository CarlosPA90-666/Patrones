"use strict";

window.onload = init;
function init() {
  document.getElementById("anadir").addEventListener("click", anadirElemento);
  document
    .getElementById("reiniciar")
    .addEventListener("click", reiniciarLista);
}

function anadirElemento() {
  let elementoUl = document.getElementById("elementoUl");
  let aux = document.getElementById("introduccionDatos");
  if (aux.value != "") {
    let elementoLi = document.createElement("li");
    elementoLi.innerHTML = aux.value;
    elementoUl.appendChild(elementoLi);
    aux.value = "";
  } else {
    window.alert("Debes rellenar el formulario");
  }
}

function reiniciarLista() {
  let elementosEliminar = document.getElementsByTagName("li");

  while (elementosEliminar.length != 0) {
    elementosEliminar[0].parentNode.removeChild(elementosEliminar[0]);
  }
}
