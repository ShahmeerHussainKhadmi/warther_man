import calendar
import math
from termcolor import colored


def print_flag_e(maxT,minT,maxH):
   
   if(maxT[1]==0):
       raise Exception("File not found for the provided date")

   date=maxT[1].split('-')
   print("Highest: "+str(int(maxT[0]))+"c on "+calendar.month_name[int(date[1])]+" "+date[2])

   date=minT[1].split('-')
   print("Lowest: "+str(int(minT[0]))+"c on "+calendar.month_name[int(date[1])]+" "+date[2])

   date=maxH[1].split('-')
   print("Humid: "+str(int(maxH[0]))+"% on "+calendar.month_name[int(date[1])]+" "+date[2])


def print_flag_a(maxT,minT,maxH):
   if(maxT[1]==0):
       raise Exception("data not found for the provided date")
   print("Highest Average: "+str(int(maxT[0]))+"c")
   print("Lowest Average: "+str(int(minT[0]))+"c")
   print("Average Humid: "+str(int(maxH[0]))+"%")

def print_flag_c(maxT,minT):
    if(maxT[1]==0):
       raise Exception("Data not found for the provided date")
    if(maxT!=[-math.inf,0]): 
        print_plus(maxT,'red')
    if(minT!=[math.inf,0]):
        print_plus(minT,'blue')

def print_plus(data,color):
    print(data[0].split('-')[2],end=" ")
    if str(data[1])=='nan':
        print("NA")
    else:
        for i in range(0,int(data[1])):
            print(colored("+",color),end="")
        print(int(data[1]))