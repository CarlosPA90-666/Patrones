"use strict";

function cambiarTrack(track) {
  let path = track.getAttribute("path");
  let viejo_audio = document.getElementById("reproductor");
  let audio_padre = viejo_audio.parentNode;
  audio_padre.removeChild(viejo_audio);
  let nuevo_audio = document.createElement("audio");
  nuevo_audio.setAttribute("id", "reproductor");
  nuevo_audio.setAttribute("controls", "controls");
  // nuevo_audio.setAttribute("autoplay", "autoplay")

  let source = document.createElement("source");
  source.setAttribute("src", path);
  source.setAttribute("type", "audio/mpeg");
  source.setAttribute("id", "reproductorSource");
  nuevo_audio.appendChild(source);
  audio_padre.appendChild(nuevo_audio);
}
function cargarReproductor() {
  let select = document.getElementById("selectTrack");
  let path = select.options[0].getAttribute("path");
  let nuevo_audio = document.createElement("audio");
  nuevo_audio.setAttribute("id", "reproductor");
  nuevo_audio.setAttribute("controls", "controls");
  let source = document.createElement("source");
  source.setAttribute("src", path);
  source.setAttribute("type", "audio/mpeg");
  source.setAttribute("id", "reproductorSource");
  nuevo_audio.appendChild(source);
  let padre = document.getElementById("reproductorBox");
  padre.appendChild(nuevo_audio);
}
cargarReproductor();
