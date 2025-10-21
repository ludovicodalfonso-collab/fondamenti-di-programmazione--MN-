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

def genera_quadrato(lat = 44.63276, lon = 10.871231, n=10, step=0.01):
    locations = []
    for _ in range(n):
        locations.append((lat, lon, f"Ciao"))
        lat += step
    for _ in range(n):
        locations.append((lat, lon, f"Ciao"))
        lon += step
    for _ in range(n):
        locations.append((lat, lon, f"Ciao"))
        lat -= step
    for _ in range(n):
        locations.append((lat, lon, f"Ciao"))
        lon -= step
    return locations