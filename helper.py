import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

def one_hot(lst, possible):
    list_of_lists = []
    for l in lst:
        one_hot_list = [0 for i in possible] 
        for i,j in enumerate(possible):
            if j in l:
                one_hot_list[i]=1
        list_of_lists.append(one_hot_list)
    id_df = pd.DataFrame(list_of_lists, columns = possible)
    
    return id_df

def one_hot_one(lst, possible):
    one_hot_list = [0 for i in possible] 
    for i,j in enumerate(possible):
        if j in lst:
            one_hot_list[i]=1
    one_hot_df = pd.DataFrame([one_hot_list],columns = possible )
    return one_hot_df