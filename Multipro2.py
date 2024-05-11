#2. Zaimplementuj algorytm sortowania (np. quicksort) i użyj `multiprocessing`, aby równolegle
# sortować podział listy. Połącz posortowane listy w jedną wynikową listę.


import multiprocessing
import numpy as np

def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        share=len(list)//2
        med=list[share]
        l_list=[]
        r_list=[]
        medium=[]
        for x in list:
            if x < med:
                l_list.append(x)                            
            elif x > med:
                r_list.append(x)
            else:
                medium.append(x)
        with multiprocessing.Pool() as pool:
            sorted_l, sorted_r=pool.map(quicksort,[l_list,r_list])
        return sorted_l + medium + sorted_r

if __name__=="__main__":
    random_numbers = np.random.rand(20)
    rannum_list = random_numbers.tolist()
    sorted_list=quicksort(rannum_list)
    print(sorted_list)