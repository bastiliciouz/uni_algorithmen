#!/usr/bin/python3.7
# -*-coding: utf-8-*-

import math
from time import process_time

hash_dict = dict()
a = (math.sqrt(5) - 1) / 2                  # Zufallskonstante
m = 100000                                  # Slotmenge
schluessel = [i for i in range(0, 1000000)]  # Schlüssel-Generierung


def einfuegen(swert):
    hwert = int(m * ((swert * a) % 1))
    counter = 0

    if hwert not in hash_dict:
        sub_dict = {"0": swert}
        hash_dict[hwert] = sub_dict

    else:
        laenge = len(hash_dict[hwert])
        to_add = {laenge: swert}
        hash_dict[hwert].update(to_add)
        counter += 1

    return counter


t1 = process_time()

retrans = 0
for s in schluessel:
    retrans += einfuegen(s)

i = 0
while i <= 100:
    try:
        print(hash_dict[i])
    except:
        pass
    i += 1

print(f"Länge des Dictionaries:   {len(hash_dict)}")
print(f"Retransmissions: {retrans}")

t2 = process_time()
print(f"Laufzeit in Sekunden: {t2-t1}")
