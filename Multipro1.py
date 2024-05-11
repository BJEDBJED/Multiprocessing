#Multi
"""
# 1. Stwórz funkcję, która przyjmuje listę dużych plików tekstowych, a następnie korzystając z
#`multiprocessing`, równolegle analizuje każdy plik, oblicza liczbę słów i zwraca sumę słów ze
#wszystkich plików.

import multiprocessing
import os

pliki = [
    r'C:\Users\USER\Desktop\NeuralNetwork.txt',
    r'C:\Users\USER\Desktop\dowysylki\anatman wyciety.txt',
    r'C:\Users\USER\Desktop\Writings\bliskiwschod.txt'
]

def teksty_to_slowa(file):
    print(f"{file} = {os.getpid()}") #sprawdzenie multi
    with open(file,'r') as file:
        tekst=file.read()
        words=len(tekst.split())
        return words

def multipro(lista_plikow):
    pool=multiprocessing.Pool()
    liczenie=pool.map(teksty_to_slowa,lista_plikow)
    pool.close()
    pool.join()
    total=sum(liczenie)
    return total

if __name__=="__main__":
    total=multipro(pliki2)
    print(f"Calkowita ilosc slow to {total}")

#DOCXXXXXXXXXXXX

import multiprocessing
import os
from docx import Document

pliki2 = [
    r'C:\Users\USER\Desktop\Broccoli.docx',
    r'C:\Users\USER\Desktop\Cosniecos.docx',
    r'C:\Users\USER\Desktop\IT.docx',
]

def teksty_to_slowa(file_path):
    print(f"Processing {file_path} in process ID: {os.getpid()}")  # Check for multiprocessing
    doc = Document(file_path)
    full_text = [paragraph.text for paragraph in doc.paragraphs]
    words = sum(len(paragraph.split()) for paragraph in full_text)
    return words

def multipro(lista_plikow):
    pool = multiprocessing.Pool()
    liczenie = pool.map(teksty_to_slowa, lista_plikow)
    pool.close()
    pool.join()
    total = sum(liczenie)
    return total

if __name__ == "__main__":
    total = multipro(pliki2)
    print(f"Calkowita ilosc slow to {total}")

"""

#2. Zaimplementuj algorytm sortowania (np. quicksort) i użyj `multiprocessing`, aby równolegle
# sortować podział listy. Połącz posortowane listy w jedną wynikową listę.

import numpy as np

random_numbers = np.random.rand(1000)
rannum_list = random_numbers.tolist()

l_list=[]
r_list=[]
medium=[]
def quicksort(list):
    share=len(list)//2
    for x in list:
        if x < share:
            l_list.appednd(x)
        elif x > share:
            r_list.append(x)
        else:
            medium.append(x)
    return quicksort(l_list) + medium + quicksort(r_list)

quicksort(rannum_list)    




