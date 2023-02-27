import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize():
    dataset=pd.read_csv('../dataset.csv')
    del dataset['id'] 
    sns.regplot(x='bathrooms',y='price',data=dataset,scatter=True,marker='x')
    plt.title('Bathrooms vs Price')
    plt.xlabel('Number of Bathrooms')
    plt.ylabel('Price')
	plt.show()

visualize()