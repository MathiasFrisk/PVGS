/**
 * Verdens kuleste funksjon. Forteller meg om jeg har fri eller ikke
 * svarer ja alle dager jeg har fri og nei dagene jeg ikke har fri
 */

function harjegfri () {
  return 'eg e i live'
}

/**
 * I Node kan du eksportere funksjoner slik at du kan gjenbruke de andre steder
 * Formatet er module.exports.<navnet på det du eksporterer> = <det du eksporterer>
 * Fordelen med å kunne eksportere og gjenbruke moduler er at du kan dele koden din i veldig små deler
 * Dette gjør det lett å ha oversikt og mye lettere å teste
 */
module.exports.harjegfri = harjegfri
