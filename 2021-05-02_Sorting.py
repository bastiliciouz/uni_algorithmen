#!/usr/bin/python3.7
# -*-coding: utf-8-*-

# Sortiert eine übergebene Liste in aufsteigender Reihenfolge
def insertion_sort_asc(liste):
    for zahl in range(1, len(liste)):

        current_key = liste[zahl]
        index_before = zahl - 1

        while index_before >= 0 and liste[index_before] > current_key:
            liste[index_before + 1] = liste[index_before]
            index_before -= 1

        liste[index_before + 1] = current_key

    return liste


# Sortiert eine übergebene Liste in absteigender Reihenfolge
def insertion_sort_desc(liste):
    for zahl in range(1, len(liste)):

        current_key = liste[zahl]
        index_before = zahl - 1

        while index_before >= 0 and liste[index_before] < current_key:
            liste[index_before + 1] = liste[index_before]
            index_before -= 1

        liste[index_before + 1] = current_key

    return liste


# Sucht den übergebenen Wert in der übergebenen Liste und gibt wenn vorhanden den Index zurück. Ansonsten None.
def suche(liste, wert):
    for index, element in enumerate(liste):
        if wert is element:
            return index
    else:
        return None


# Gibt die Fakultät einer Zahl zurück (-Wert = Error, 0=1)
def fakultaet(z, m):
    rueckgabe = 1

    if m == 1:
        if z == 0:
            rueckgabe = 0
        elif z > 0:
            for wert in range(2, z + 1):
                rueckgabe *= wert
            else:
                rueckgabe = "Falsche Methode ausgewählt"
        else:
            rueckgabe = "Minuswert kann nicht berechnet werden"

    elif m == 2:
        import math
        rueckgabe = math.factorial(z)
    else:
        rueckgabe = "Falsche Methode ausgewählt"

    return rueckgabe



# Kontroll-Code
a = [31, 29, 59, 26, 41, 58]
b = [31, 29, 59, 26, 41, 58]
print(f"Suche nach Index:     {suche(a, 41)}")
print(f"Aufsteigend sortiert: {insertion_sort_asc(a)}")
print(f"Absteigend sortiert:  {insertion_sort_desc(b)}")

zahl = 5
methode = 2  # 1 = Normal, 2 = Math
print(f"Fakultaet von {zahl}: {fakultaet (zahl, methode)}")

c = [31, 29, 59, 26, 59, 58]
print(merge_sort(c))
