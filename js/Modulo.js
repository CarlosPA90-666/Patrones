'use strict';



//----------------------------------Inicio.html----------------------------------
window.onload = init;
function init(){
    document.getElementById("anadir").addEventListener("click",anadirElemento);
    document.getElementById("reiniciar").addEventListener("click",reiniciarLista);
}

function anadirElemento(){
    var elementoUl = document.getElementById("elementoUl");
        var aux = document.getElementById("introduccionDatos");
        if (aux.value != ""){
            var elementoLi = document.createElement("li");
            elementoLi.innerHTML = aux.value;
            elementoUl.appendChild(elementoLi);
            aux.value="";
        }else{window.alert("Debes rellenar el formulario")}
}

function reiniciarLista(){
    var elementosEliminar = document.getElementsByTagName("li");
        
        while(elementosEliminar.length!=0){
        elementosEliminar[0].parentNode.removeChild(elementosEliminar[0]);   
    }
}   
//----------------------------------Inicio.html----------------------------------