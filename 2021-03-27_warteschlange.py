#!/usr/bin/python3.7
# -*-coding: utf-8-*-

"""
ENQEUE(Q,x)
Q[Q.ende] = x
if Q.ende == Q.länge
    Q.ende = 1
else Q.ende = Q.ende +1

DEQEUE(Q)
x = Q[Q.kopf]
if Q.kopf == Q.länge
    Q.kopf = 1
else Q.kopf = Q.kopf + 1
return x
"""
from collections import deque

warteschlange = deque(maxlen=5)
eingabe = "placeholder"


def queue(eing, warteschl):
    if eing != 'd':
        if len(warteschlange) == 5:
            print("Maximale Laenge erreicht, erster Wert wurde ueberschrieben")
        warteschl.append(eingabe)
    elif eing == "d":
        try:
            warteschl.popleft()
        except:
            print("Queue ist leer!")

    return warteschl


while eingabe != "x":
    eingabe = input("Zahl oder 'd' eingeben ('x' für Ende): ")
    
    if eingabe != "x":
        queue(eingabe, warteschlange)
    else:
        pass

    print(warteschlange)
