// Made by MathiasApple

function beregn(){
    var personer= document.getElementById("passasjer").value;//henter verdi fra antall personer
    var lengde= document.getElementById("lengde").value;//henter verdi fra antall lengde
    tall1=lengde*150/personer;
    tall2=lengde*52;
    tall3=lengde*32;
    tall4=lengde*103;
    tall5=lengde*340;
    
document.getElementById("fly").style.width = tall5/1000+"px";
fly.innerHTML=(tall5);

document.getElementById("bussland").style.width = tall4/1000+"px";
bussland.innerHTML=(tall4);

document.getElementById("tog").style.width = tall3/1000+"px";
tog.innerHTML=(tall3);

document.getElementById("buss").style.width = tall2/1000+"px";
buss.innerHTML=(tall2);

document.getElementById("bil").style.width = tall1/1000+"px";
bil.innerHTML=(tall1);
}