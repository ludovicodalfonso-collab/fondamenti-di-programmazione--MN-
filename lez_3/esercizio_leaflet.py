
from modulo_leaflet import leggi_template, genera_quadrato, genera_placemarks, sostituisci_placemarks, salva_mappa

def main():
    template = leggi_template('lez_3/leaflet/leaflet.template')
    locations = genera_quadrato()
    placemarks = genera_placemarks(locations)
    mappa = sostituisci_placemarks(template, placemarks)
    salva_mappa('lez_3/leaflet/output.html', mappa)

main()