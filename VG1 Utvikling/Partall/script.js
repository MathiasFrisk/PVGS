var partall1 = 20
var partall2 = 19;

var sum = partall1+partall2;

var ord = "Hewo world"
var n = ord.length;

// oppg.1

if(partall1 % 2 == 0){
    console.log("Tallet er et partall");
}
else{
    console.log("tallet er et oddetall");
}

// oppg.2

if(partall2 + partall1 % 2 == 0){
    console.log(" Partall1 + Partall2 blir et partall ");
}
else{
    console.log("partall1 + Partall2 blir et oddetall ");
}

// oppg.3

if(sum % 2 == 0 && sum >20){
    console.log("Summen blir et partall større enn 20");
}
else{
    console.log("Summen er ikke større enn 20 eller et partall");
}

// oppg.4

var ord = partall2
var n = ord.length;

var sum1 = ord + n

if(n > 20){
    console.log("Navnet består av mer en 20 bokstaver")
}
else{
    console.log("Navnet består ikke av mer enn 20 bokstaver")
}