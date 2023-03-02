import calendar
import sys
import numpy as np
import printdata
import math


def proccess(df):
    flag=sys.argv[1]
    if(flag=='-a'):
        function_flag_a(df)
    elif(flag=='-e'):
        function_flag_e(df)
    else:
        function_flag_c(df)



def function_flag_e(df):
    maxT=[-math.inf,0]
    minT=[math.inf,0]
    maxH=[0,0]
    lst=[df['PKT'],df['Max TemperatureC'],df['Min TemperatureC'],df['Max Humidity']]
    for i,x in enumerate(lst[0]):
        if str(x).split('-')[0]==sys.argv[2].split('/')[0]:

            maxT,minT,maxH = update_value(lst,i,maxT,minT,maxH)
    
    printdata.print_flag_e(maxT,minT,maxH)

def function_flag_a(df):
    maxT=[-math.inf,0]
    minT=[math.inf,0]
    maxH=[0,0]
    date=sys.argv[2].split('/')    
    lst=[df['PKT'],df['Mean TemperatureC'],df['Mean TemperatureC'],df[' Mean Humidity']]
    for i,x in enumerate(lst[0]):
        if str(x).split('-')[0]==date[0] and str(x).split('-')[1]== date[1]:
            maxT,minT,maxH = update_value(lst,i,maxT,minT,maxH)

    printdata.print_flag_a(maxT,minT,maxH)           

def update_value(lst,i,maxT,minT,maxH):
    if(str(lst[1][i])!='nan' and int(lst[1][i])>maxT[0]):
        maxT[0]=lst[1][i]
        maxT[1]=lst[0][i]
    if(str(lst[2][i])!='nan' and int(lst[2][i])<minT[0]):
        minT[0]=lst[2][i]
        minT[1]=lst[0][i]
    if(str(lst[3][i])!='nan' and int(lst[3][i])>maxH[0]):
        maxH[0]=lst[3][i]
        maxH[1]=lst[0][i]

    return maxT,minT,maxH


def function_flag_c(df):
    maxT=[-math.inf,0]
    minT=[math.inf,0]
    date=sys.argv[2].split('/')    

    lst=[df['PKT'],df['Max TemperatureC'],df['Min TemperatureC']]
    for i,x in enumerate(lst[0]):
         if str(x).split('-')[0]==date[0] and str(x).split('-')[1]== date[1]:
            maxT[0]=lst[0][i]
            maxT[1]=lst[1][i]
            minT[0]=lst[0][i]
            minT[1]=lst[2][i]
            printdata.print_flag_c(maxT,minT)


