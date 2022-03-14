minFunksjon();
minFunksjon();
minFunksjon();

function minFunksjon(){
    document.writeln("Dette er skrevet av en funksjon");
    document.writeln("<br>");
}

leggsammentotall(2,3); //kaller opp funksjonen leggsammentotall med parameter
leggsammentotall(4,5);
leggsammentotall(7,8);

function leggsammentotall(tall1,tall2){
    var sum = tall1+tall2;
    document.writeln(tall1 + " pluss " + tall2 + " blir "+ sum + "<br>");
}
//Arealet 

areal(34,43)

function areal(tall1,tall2){
    var sum = tall1*tall2;
    document.writeln(" Arealet i et rektagel med sidene " +tall1 + " og " + tall2 + " blir "+ sum + "<br>");
}

//Omkretsen

omkretsen(12,34)

function omkretsen(tall1,tall2){
    var sum = tall1-
    tall2;
    document.writeln(" omkretsen blir " +tall1 + " og " + tall2 + " blir "+ sum + "<br>");
}