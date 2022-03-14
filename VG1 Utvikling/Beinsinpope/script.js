// Laget av MathiasApple og med hjelp av Raito Lorenzo
 
function beregn(){
    var dieselValg = document.getElementById("diesel").checked;
    var bensinValg = document.getElementById("bensin").checked;
    var literVar = document.getElementById("liter").value;
 
    var pris = Math.round(2.5);
 
    if(dieselValg){
        pris = literVar * 12.90;
    }
    else if(bensinValg){
        pris = literVar * 13.40;
    }
    document.getElementById("resultat").innerHTML = pris + " kr"
}

