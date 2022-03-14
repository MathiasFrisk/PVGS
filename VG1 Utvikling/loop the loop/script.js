// opg1
for(var i = 0; i<100; i ++){
    document.writeln(i); 
}

//opg2
document.writeln("<br>");
document.writeln("<br>");
document.writeln("<Oppgave2>");
document.writeln("<br>");

for(var i = 100; i>0; i--){
    document.writeln(i)
}

//opg3
for(var i = 0; i<100; i=i+2){
    document.writeln(i);
}

//opg4
for(var i = 0; i<100; i=i+4){
    document.writeln(i);
}

//a
for(var i = 0; i<100; i=i+5){
    document.writeln(i);
}




//opg6

var bortover = 4;
var nedover = 5;
 
for(var j = 0;j<nedover;j++){
 if(j == 1){bortover = 1;}
 if(j == 3){bortover = 1;}
 if(j == 2){bortover = 2;}
 if(j == 4){bortover = 4;}
 for(var i = 0; i<bortover;i++){
 document.writeln("*");
 }
 document.writeln("<br>");
 }