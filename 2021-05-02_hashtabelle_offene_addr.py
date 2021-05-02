#!/usr/bin/python3.7
# -*-coding: utf-8-*-

from time import process_time

hash_dict = dict()
m = 11                                  # Slotmenge
schluessel = [10, 11, 12, 13, 14, 15, 16, 205, 18, 19, 20]  # Schlüssel-Generierung


def einfuegen(swert):
    hwert = int(swert % m)
    counter = 0

    if hwert not in hash_dict:
        hash_dict[hwert] = swert

    else:
        while hwert in hash_dict:
            hwert = int((swert + counter) % m)
            counter += 1
        else:
            hash_dict[hwert] = swert

    return counter


t1 = process_time()

retrans = 0
for s in schluessel:
    retrans += einfuegen(s)

print(hash_dict)
print(f"Länge des Dictionaries:   {len(hash_dict)}")
print(f"Retransmissions: {retrans}")

t2 = process_time()
print(f"Laufzeit in Sekunden: {t2-t1}")
