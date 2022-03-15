function beregn () {
    //data fra input
	var mannValg = document.getElementById("mann").checked;
	var kvinneValg = document.getElementById("kvinne").checked;
	var alderVar = document.getElementById("alder").value;
    var hoydeVar = document.getElementById("hoyde").value;

    var magisktall=0;

    if(mannValg){
        magiskTall = alderVar * alderVar - hoydeVar;
        console.log(magisktall);
    }
    else if (kvinneValg){
		magiskTall = alderVar * hoydeVar - 3;
		console.log(magiskTall);
	}
    else
    document.getElementById("utTekst2").innerHTML = "Du må velge kjønn"

    //Sjekker om det magiske tallet er odde eller partall
	if (magiskTall%2==0){
        document.getElementById("utTekst").innerHTML = "Det vil gå deg godt her i verden... For at spådommen skal gå i oppfyllelse, må du betale inn 100 kr til følgende kontonummer: 1234.12.12345"
    }
else
        document.getElementById("utTekst").innerHTML = "Stakkars deg! Alt kommer til å gå deg galt... For at spådommen ikke skal gå i oppfyllelse, må du betale inn 100 kr til følgende kontonummer: 1234.12.12345"
}
