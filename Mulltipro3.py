#Mulltipro3

#3.Zdefiniuj funkcję matematyczną, a następnie użyj `multiprocessing` do równoległego obliczania
#wartości funkcji dla różnych zestawów parametrów.

from multiprocessing import Pool
import os

def math_function(x):
    print(f"{x} = {os.getpid()}")
    print(3.14*x**2)

if __name__ =="__main__":
    with Pool() as p:
        wynik=p.map(math_function,[1,2,3,4,5,700,3213,2,3123,123,123,12,312,312,3,123,12312,3,12,312,43,5,43,5,35,56346,43,65434,534,6,34,6345])

