def inlezen_beginstation(stations):
    while True:
        beginstation = input('Wat is je beginstation?\n')
        if beginstation in stations:
            return beginstation
        else: print('Deze trein begint niet in',beginstation)

def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input('Wat is je eindstation\n')
        if eindstation in stations and stations.index(eindstation) > stations.index(beginstation):
            return eindstation
        elif eindstation in stations:
            print('Error -incorrecte volgorde- ')
        else: print('Deze trein stopt niet in',eindstation)

def omroepen_reis(stations, beginstation, eindstation):
    print ('Het beginstation', beginstation, 'is het', str(stations.index(beginstation)+1)+'e station in het traject.')
    print('Het eindstation', eindstation, 'is het', str(stations.index(eindstation)+1) + 'e station in het traject.')
    aantal_stations = (stations.index(eindstation)) - stations.index(beginstation)
    print('De afstand bedraagt', aantal_stations, 'station(s).')
    print('De prijs van een kaartje is', aantal_stations * 5, 'Euro')
    print('Jij stapt in de trein in:', beginstation)
    for tussen_station in stations[stations.index(beginstation)+1:stations.index(eindstation)]:
        print('-', tussen_station)
    print('Jij stapt weer uit de trein in:', eindstation)

stations = ['Schagen', 'Heerhugowaard','Alkmaar','Castricum', 'Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal','’s-Hertogenbosch',
'Eindhoven', 'Weert','Roermond','Sittard', 'Maastricht']

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)