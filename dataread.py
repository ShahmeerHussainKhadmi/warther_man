import pandas as pd
import glob
import calendar


def read_data(path):

    #path="/home/dev/Desktop/weatrherman/Murree_weather/"
    path=path+'/'
    files=glob.glob(path+"*.txt")
    print(path)
    li=[pd.read_csv(file,index_col=None) for file in files]
    df=pd.concat(li,axis=0,ignore_index=True)
    df.to_csv("data.csv")
    return df





    
    
    
    