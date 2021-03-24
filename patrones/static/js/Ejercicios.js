home();



function pauseVid(){
    let video1 = document.getElementById("vidbrujula");
    video1.pause();

    let video2 = document.getElementById("vidaros");
    video2.pause();

    let video3 = document.getElementById("vidpelota");
    video3.pause();

    let video4 = document.getElementById("videspejito");
    video4.pause();

    let video5 = document.getElementById("videstatua");
    video5.pause();
}



function home(){
    
    document.getElementById('brujulacontent').style.display="none";
    document.getElementById('aroscontent').style.display="none";
    document.getElementById('pelotacontent').style.display="none";
    document.getElementById('espejitocontent').style.display="none";
    document.getElementById('estatuacontent').style.display="none";
    document.getElementById('Rdebrujula').style.display="none";
    document.getElementById('Rdearos').style.display="none";
    document.getElementById('Rdeespejito').style.display="none";
    document.getElementById('Rdepelota').style.display="none";
    document.getElementById('Rdeestatua').style.display="none";

    let video1 = $("#vidbrujula").attr("src");
    $("#vidbrujula").attr("src","");
    $("#vidbrujula").attr("src",video1);

    let video2 = $("#vidaros").attr("src");
    $("#vidaros").attr("src","");
    $("#vidaros").attr("src",video2);

}

//--------------------------------BRUJULA--------------------------------
function mostrarbrujula(){
    document.getElementById('Ejercicios-subtitulos').style.display="none";
    document.getElementById('brujulacontent').style.display="block";   
    document.getElementById('Rdebrujula').style.display="block"; 
}

$("#brujula").click(function(){
	mostrarbrujula();
});

function regresardebrujula(){
    document.getElementById('Ejercicios-subtitulos').style.display="block";
    document.getElementById('brujulacontent').style.display="none";
    document.getElementById('Rdebrujula').style.display="none"; 
    
}

$("#Rdebrujula").click(function(){
    pauseVid();
	regresardebrujula();
});
//--------------------------------BRUJULA--------------------------------

//--------------------------------AROS--------------------------------
function mostrararos(){
    document.getElementById('Ejercicios-subtitulos').style.display="none";
    document.getElementById('aroscontent').style.display="block";    
    document.getElementById('Rdearos').style.display="block";
}

$("#Aros").click(function(){
	mostrararos();
});

function regresardearos(){
    document.getElementById('Ejercicios-subtitulos').style.display="block";
    document.getElementById('aroscontent').style.display="none";
    document.getElementById('Rdearos').style.display="none";
    
}

$("#Rdearos").click(function(){
    pauseVid();
	regresardearos();
});
//--------------------------------AROS--------------------------------


//--------------------------------PELOTA--------------------------------
function mostrarpelota(){
    document.getElementById('Ejercicios-subtitulos').style.display="none";
    document.getElementById('pelotacontent').style.display="block";    
    document.getElementById('Rdepelota').style.display="block";
}

$("#Pelota").click(function(){
	mostrarpelota();
});

function regresardepelota(){
    document.getElementById('Ejercicios-subtitulos').style.display="block";
    document.getElementById('pelotacontent').style.display="none";
    document.getElementById('Rdepelota').style.display="none";
    
}

$("#Rdepelota").click(function(){
    pauseVid();
	regresardepelota();
});
//--------------------------------PELOTA--------------------------------

//--------------------------------ESPEJITO--------------------------------
function mostrarespejito(){
    document.getElementById('Ejercicios-subtitulos').style.display="none";
    document.getElementById('espejitocontent').style.display="block";    
    document.getElementById('Rdeespejito').style.display="block";
}

$("#espejito").click(function(){
	mostrarespejito();
});

function regresardeespejito(){
    document.getElementById('Ejercicios-subtitulos').style.display="block";
    document.getElementById('espejitocontent').style.display="none";
    document.getElementById('Rdeespejito').style.display="none";
    
}

$("#Rdeespejito").click(function(){
    pauseVid();
	regresardeespejito();
});
//--------------------------------ESPEJITO--------------------------------

//--------------------------------ESTATUA--------------------------------
function mostrarestatua(){
    document.getElementById('Ejercicios-subtitulos').style.display="none";
    document.getElementById('estatuacontent').style.display="block";    
    document.getElementById('Rdeestatua').style.display="block";
}

$("#Estatua").click(function(){
	mostrarestatua();
});

function regresardeestatua(){
    document.getElementById('Ejercicios-subtitulos').style.display="block";
    document.getElementById('estatuacontent').style.display="none";
    document.getElementById('Rdeestatua').style.display="none";
    
}

$("#Rdeestatua").click(function(){
    pauseVid();
	regresardeestatua();
});
//--------------------------------ESTATUA--------------------------------


