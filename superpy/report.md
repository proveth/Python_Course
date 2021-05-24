SuperPy:

Tijdens de initialisatie van het programma leest het de CSV file. De producten in de lijst worden intern opgeslagen als Product objecten in een lijst in een supermarkt object.

Vervolgens  wordt de argurment parser opgeroepen en de functie die daarbij hoort wordt opgeroepen. Eventuele None or “” worden vervangen door default waardes. Voor de argument parser is gebruik gemaakt van de argpase lib. Met een subparser omdat elk commando verschillende sub argumenten heeft.

Indien een product wordt ingekocht , wordt er een nieuw object van classe product aangemaakt en toegevoegd aan de inventaris lijst. Als het product wordt verkocht wordt het verkoop attribuut van het object in de lijst geupdated. Als het product al verkocht is of overdatum , mag het niet verkocht worden en het eerst volgende item wordt gekozen met de dezlfde naam. Indien er geen producten gevonden zijn wordt er een Index error gegeven. Deze fout wordt opgevangen door middel van try , except.

Elke file, classe heeft zijn eigen functies die meestal herbruikbaar zijn. Om redundante code te verkomen.

Nadat een actie is uitgevoerd wordt de csv file opnieuw opgeslagen door middel van een lijst iteratie.

Afgezien de gevraagde opgaven heb ik het volgende ook geimplementeerd:
 
1)	Object georiënteerd:
    Myn SuperPy heb ik opgedeeld in meerdere classes. 
    De Classe Product bevat alle attributen van een product zoals datum , price etc.
    Deze product objecten  worden in een dynamische lijst bijgehouden in een object van Supermarkt.
    Door dat Supermarkt ook een classe is , is het mogelijk om meerdere supermark locaties te maken
    Dit leek me handiger en uitdagender dan een grote lijst te maken. 

2)	Via mathlibplot is het mogelijk om een barplot te genereren van de inventory van een bepaalde datum. De aantallen van producten 
    worden hierin weergegeven. Indien meerdere producten met de zelfde naam dan wordt de hoeveelheid aangepast.
3)	Try and except toegepast by index Error
4)	Toepassen van Pytest op de verschilede objecten.
5)  opslaan van datum in tekst file.

Testpy:
the cvs file must only contain header, no double milk products other wise test test_sell_expired will fail.

Examples

# Buy orange 
Python3 superpy.py buy --product_name orange  --price 1.75 –expiration_date 2024-01-01

# Sell orange
Python3 superpy.py sell --product_name orange  --price 2.00  

# get inventory today
Python3 superpy.py report inventory 

# get inventory yesterday
Python3 superpy.py report inventory –date yesterday

# get inventory @date 
Python3 superpy.py report inventory –date <date>

# get profit from @date 
Python3 superpy.py report profit  –date <date>

# get revenu from @date 
Python3 superpy.py report revenue  –date <date>

# plot inventory @date 
Python3 superpy.py report plot –date <date>

# Print total list all items. 
Python3 superpy.py report total_list

# change date
Python3 superpy.py date_change --date tommorrow

# change date
Python3 superpy.py date_change --date today

# change date
Python3 superpy.py date_change --date yesterday

# change date
Python3 superpy.py date_change --date 2099-05-30
