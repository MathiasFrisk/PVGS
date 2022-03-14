// oppgave 1 // ps det er veldig lite på denne scrpit delen det skjedde noe med script som gjorde at det bare sa at det var feil hele tiden og det ville ikke jeg vett ikke hva problemet var.
function buttonEn() {
    var navnVar = document.getElementById("navn").value; //henter data fra html
    console.log("Hei på deg", "navn"); //denne skal egentlig skrive navnet ditt i console hvis du skriver det i taben på html greia men jeg husker ikke helt hvordan det funger
    document.getElementById("minDiv").innerHTML = "Hei på deg", document.getElementById("navn"); // samme her bare i sleve siden.
}

//oppgave2
function buttonjul() {
    var julVar = document.getElementById("jultall").value; //henter data fra html

    var JuleTall=24; //riktig jule tall

    if(Juletallriktig){ //dette er hva som skjer hvis tallet er 24
        julTall = 24;
        console.log(JuleTall);
        
    }
    else if (JuletallFeil){ // detter skjer hvis jule tallet er feil.
		julTall = 0;
        console.log(JuleTall);
    }
    if (juleTall = 24){
        document.getElementById("minDivTo").innerHTML = "Happy christmas det er 24 desember" // sier om det er jul eller ikke, denne sier at det er jul
    }
}


// oppgave 3 // fikk ikke til oppgave 2 så starter ikke på oppgave 3