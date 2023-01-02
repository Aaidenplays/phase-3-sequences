#!/usr/bin/env python3

def print_fibonacci(length):
    fibb = []
    for i in range(length):
        if i < 2:
            fibb.append(i)
        else:
            fibb.append(fibb[i-1] + fibb[i-2]) 
    print(fibb)