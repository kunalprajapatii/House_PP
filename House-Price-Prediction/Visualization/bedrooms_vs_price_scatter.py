# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:05:46 2018

@author: pravin
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize():
    dataset=pd.read_csv('../dataset.csv')
    del dataset['id'] #as we know id of a house is not important in predicting its price
    sns.regplot(x='bedrooms',y='price',data=dataset,scatter=True,marker='x')
    plt.title('Bedrooms vs Price')
    plt.xlabel('Number of Bedrooms')
    plt.ylabel('Price')
    plt.show()

visualize()#who is ready to buy a 33-bedroom for less price? ;)