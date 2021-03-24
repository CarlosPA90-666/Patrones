home();

function pauseVid(){
    let video1 = document.getElementById("vidrefranes");
    video1.pause();

    let video2 = document.getElementById("vidoveja");
    video2.pause();

    let video3 = document.getElementById("vidquien");
    video3.pause();

    let video4 = document.getElementById("vidcancion");
    video4.pause();

    let video5 = document.getElementById("vidpalabras");
    video5.pause();
}


function home(){
    document.getElementById('ovejacontent').style.display="none";
    document.getElementById('refranescontent').style.display="none";
    document.getElementById('quiencontent').style.display="none";
    document.getElementById('cancioncontent').style.display="none";
    document.getElementById('palabrascontent').style.display="none";
    document.getElementById('Rderefranes').style.display="none"; 
    document.getElementById('Rdeoveja').style.display="none"; 
    document.getElementById('Rdequien').style.display="none"; 
    document.getElementById('Rdecancion').style.display="none"; 
    document.getElementById('Rdepalabras').style.display="none"; 

}

//--------------------------------REFRANES--------------------------------
function mostrarrefranes(){
    document.getElementById('Mentales-subtitulos').style.display="none";
    document.getElementById('refranescontent').style.display="block";   
    document.getElementById('Rderefranes').style.display="block";
}

$("#Refran").click(function(){
	mostrarrefranes();
});

function regresarderefranes(){
    document.getElementById('Mentales-subtitulos').style.display="block";
    document.getElementById('refranescontent').style.display="none";
    document.getElementById('Rderefranes').style.display="none"; 
    
}

$("#Rderefranes").click(function(){
    pauseVid();
	regresarderefranes();
});
//--------------------------------REFRANES-------------------------------

//--------------------------------OVEJA--------------------------------
function mostraroveja(){
    document.getElementById('Mentales-subtitulos').style.display="none";
    document.getElementById('ovejacontent').style.display="block";   
    document.getElementById('Rdeoveja').style.display="block";
}

$("#Oveja").click(function(){
	mostraroveja();
});

function regresardeoveja(){
    document.getElementById('Mentales-subtitulos').style.display="block";
    document.getElementById('ovejacontent').style.display="none";
    document.getElementById('Rdeoveja').style.display="none"; 
    
}

$("#Rdeoveja").click(function(){
    pauseVid();
	regresardeoveja();
});
//--------------------------------OVEJA-------------------------------

//--------------------------------QUIEN--------------------------------
function mostrarquien(){
    document.getElementById('Mentales-subtitulos').style.display="none";
    document.getElementById('quiencontent').style.display="block";   
    document.getElementById('Rdequien').style.display="block";
}

$("#Quien").click(function(){
	mostrarquien();
});

function regresardequien(){
    document.getElementById('Mentales-subtitulos').style.display="block";
    document.getElementById('quiencontent').style.display="none";
    document.getElementById('Rdequien').style.display="none"; 
    
}

$("#Rdequien").click(function(){
    pauseVid();
	regresardequien();
});
//--------------------------------QUIEN-------------------------------

//--------------------------------CANCION--------------------------------
function mostrarcancion(){
    document.getElementById('Mentales-subtitulos').style.display="none";
    document.getElementById('cancioncontent').style.display="block";   
    document.getElementById('Rdecancion').style.display="block";
}

$("#Cancion").click(function(){
	mostrarcancion();
});

function regresardecancion(){
    document.getElementById('Mentales-subtitulos').style.display="block";
    document.getElementById('cancioncontent').style.display="none";
    document.getElementById('Rdecancion').style.display="none"; 
    
}

$("#Rdecancion").click(function(){
    pauseVid();
	regresardecancion();
});
//--------------------------------CANCION-------------------------------

//--------------------------------PALABRAS--------------------------------
function mostrarpalabras(){
    document.getElementById('Mentales-subtitulos').style.display="none";
    document.getElementById('palabrascontent').style.display="block";   
    document.getElementById('Rdepalabras').style.display="block";
}

$("#Palabra").click(function(){
	mostrarpalabras();
});

function regresardepalabras(){
    document.getElementById('Mentales-subtitulos').style.display="block";
    document.getElementById('palabrascontent').style.display="none";
    document.getElementById('Rdepalabras').style.display="none"; 
    
}

$("#Rdepalabras").click(function(){
    pauseVid();
	regresardepalabras();
});
//--------------------------------PALABRAS-------------------------------