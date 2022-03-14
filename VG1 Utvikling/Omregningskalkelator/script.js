function regnUt(PAL){ // funksjonen knappEn henter inn verdien fra et tekstfelst og regner ut verdien til BMR
    var vekt = document.getElementById("myText").value; // deklarere variablen vekt og tilegner den verdien hentet fra input div myText
    var BMR = 35.27 + (0.558*vekt); // Deklarere variabelen BRM og regner ut en verdi på bagrunn av den gitte formelen.
    
    console.log(BMR); // Skriver verdien til Consol.
    var energiforbuket = BMR * PAL;
    minDiv.innerHTML = (" BMR for en gutt 18 år og 180 cm er : " + BMR + " <br> og han energiforbruk er " + energiforbuket ); // kjørere ut verdien av BMR til div minDIv.
   }
