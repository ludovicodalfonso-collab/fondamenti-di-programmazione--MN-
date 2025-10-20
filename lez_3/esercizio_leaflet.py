def leggi_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def sostituisci_placemarks(template, placemarks):
    return template.replace("{{PLACEMARKS}}", placemarks)

def genera_placemarks(locations):
    placemarks = ""
    for loc in locations:
        placemarks += f'L.marker([{loc[0]}, {loc[1]}]).addTo(map).bindPopup("{loc[2]}")\n'
    return placemarks   

def salva_mappa(file_path, mappa):
    with open(file_path, 'w') as file:
        file.write(mappa)

def main():
    template = leggi_template('lez_3/leaflet/leaflet.template')
    locations = [
        (44.63276, 10.871231, "Cognento"),
        (44.83276, 10.871231, "Cognento2")
    ]
    placemarks = genera_placemarks(locations)
    mappa = sostituisci_placemarks(template, placemarks)
    salva_mappa('lez_3/leaflet/leaflet.html', mappa)
