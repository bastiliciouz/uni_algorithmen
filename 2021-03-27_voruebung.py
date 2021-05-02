#!/usr/bin/python3.7
# -*-coding: utf-8-*-

def func(u, v):
    while u > 0:
        if u < v:
            u, v = v, u
        u = u - v
    return v


print(func(84, 231))
