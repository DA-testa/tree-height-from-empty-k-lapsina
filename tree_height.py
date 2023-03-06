# python3

import sys
import threading
import numpy
import os

def compute_height(n, parents):

    max_height = 0
    for i in range(n):
        height = 0
        child = i
        while child != -1:
            height += 1
            child = parents[child]
        max_height=max(max_height, height)
    return max_height


def main():

    text = input().strip().upper()
    if text == 'I':
        n = int(input("Elementu skaits: "))
        people = list(map(int, input("Vērtības: ").split(" ")))
        parents = numpy.array(people, dtype=int)
    elif text == 'F':
        name = input("Faila nosaukums: ")
        if 'a' in name:
            print("Nepareizs nosaukums")
            return
        file_path = os.path.join(os.getcwd(), 'test', name)
        with open(file_path, 'r') as fails:
            n = int(fails.readline())
            values = fails.readline()
            parents = list(map(int, values.split(" ")))
    else:
        print("Nepareiza ievade")
        return
    
    

    
    max_height = compute_height(n, parents)
    print(max_height)


sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()