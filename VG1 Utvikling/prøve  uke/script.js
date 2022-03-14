//Oppgave1
function text1(){
    console.log("Hei dette er i console")
}
//Oppgave2
function Tregangen(){
    for(var i = 0; i<24; i=i+3)
        console.log(i);
}
//Oppgave3

var utregning1 = 5;
var utregning2 = 3;

function Utregning(){
// vet ikke helt hvordan man gjør denne oppgaven prøve på noe
for(var i = utregning1; i<utregning2;i++)
    console.log(i);
}

//oppgave 6

var bortover = 6;
var nedover = 6;

function Pyramide(){
for(var j = 0;j<nedover;j++){
 if(j == 6){bortover = 6;}
 if(j == 5){bortover = 5;}
 if(j == 4){bortover = 4;}
 if(j == 3){bortover = 3;}
 if(j == 2){bortover = 2;}
 if(j == 1){bortover = 1;}
 for(var i = 0; i<bortover;i++){
document.writeln("@");
}
document.writeln("<br>");
}
}
//for en rar grunn så får jeg ikke denne til å fungere.