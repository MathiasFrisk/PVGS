// Laget av: Staale Bergersen
// Creative Commons BY-SA

function beregn(){
	//Henter inn data fra input-elementene
	var mannValg = document.getElementById("mann").checked;
	var kvinneValg = document.getElementById("kvinne").checked;
	var alderVar = document.getElementById("alder").value;
	var hoydeVar = document.getElementById("hoyde").value;

	//Variabel for det magiske tallet
	var magiskTall=0;

	//Sjekker valgt radioknapp, og beregner magisk tall for mann eller kvinne.
	if(mannValg){
		magiskTall = alderVar * alderVar - hoydeVar;
		console.log(magiskTall);
	}
	else if (kvinneValg){
		magiskTall = alderVar * hoydeVar - 3;
		console.log(magiskTall);
	}
	else
		console.log("Du må velge kjønn!");

	//Sjekker om det magiske tallet er odde eller partall
	if (magiskTall%2==0){
			document.getElementById("utTekst").innerHTML = "Det vil gå deg godt her i verden... For at spådommen skal gå i oppfyllelse, må du betale inn 100 kr til følgende kontonummer: 1234.12.12345"
		}
	else
			document.getElementById("utTekst").innerHTML = "Stakkars deg! Alt kommer til å gå deg galt... For at spådommen ikke skal gå i oppfyllelse, må du betale inn 100 kr til følgende kontonummer: 1234.12.12345"
		
}