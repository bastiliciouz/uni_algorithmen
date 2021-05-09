#!/usr/bin/python3.7
# -*-coding: utf-8-*-
from random import randint

def merge_sort(menge):              # Link zur Erklärung und Code: https://www.educative.io/edpresso/merge-sort-in-python
    global counter
    counter += 1

    if len(menge) > 1:              # Solange die Menge größer als 1 ist
        mitte = len(menge)//2       # Wird die Mitte bestimmt (Ganzzahl abgerundet, bei Länge 5 wäre es 2)
        links = menge[:mitte]       # Links = Anfang bis Mitte
        rechts = menge[mitte:]      # Rechts = Mitte bis Ende

        merge_sort(links)           # Rekursiver Aufruf für Teilmenge, solange bis Links komplett aufgeteilt ist
        merge_sort(rechts)          # Dann rekursiver Aufruf für Teilmenge, bis Rechts komplett aufgeteilt ist
                                    # Alle Aufrufe werden auch für Teilmengen gemacht um immer weiter zu splitten

                                    # Hier geht es weiter sobald Menge = 1 ist!!
        i = j = k = 0               # Laufvariablen für weiteren Verlauf

        while i < len(links) and j < len(rechts):   # Für Fälle solange links und rechts verglichen werden können
            if links[i] < rechts[j]:                # Falls links größer ist: Menge[k] = Links
                menge[k] = links[i]
                i += 1
            else:                                   # Falls rechts größer ist: Menge[k] = Rechts
                menge[k] = rechts[j]
                j += 1
            k += 1

        while i < len(links):       # Für Fälle wo die Menge links größer als rechts ist
            menge[k] = links[i]     # Direkt Menge[k] = Links setzen (Leftover)
            i += 1
            k += 1

        while j < len(rechts):      # Für Fälle wo die Menge rechts größer als links ist
            menge[k] = rechts[j]    # Direkt Menge[k] = Rechts setzen (Leftover)
            j += 1
            k += 1

# Kontroll-Code
a = []
for zahl in range(0, 100):          # Generierung von 100 Zufallszahlen in der Range von 0-100
    a.append(randint(0, 100))

counter = 0                         # Zur Zählung der iterativen Aufrufe von merge_sort()
merge_sort(a)                       # Initialer Aufruf der Funktion
print(f"Merge Sort Ergebnis: {a}")
print(f"Aufrufe der Funktion insgesamt: {counter}")