from os.path import exists
import glob
import sys
import os 
import math
from termcolor import colored

def validate_parms():
    if(len(sys.argv)!=4):
        raise Exception("Invalid number of params")
        sys.exit()

def get_path():
    n = len(sys.argv)
    if(n>3):
        for i in range(4, n):
            sys.argv[3]+=sys.argv[i]
    return sys.argv[3]

def validate_year(year):
    try:
        year=int(year)
    except:
        raise Exception("Invalid data type of year")
        sys.exit()
    if year<1:
        raise Exception("Invalid year")
        sys.exit()

def validate_month(month):
    try:
        month=int(month)
    except:
        raise Exception("Invalid data type of month")
        sys.exit()
    if month>0 and month <13:
        return 
    raise Exception("inavalid month")
    sys.exit()

def validate_date_parms():
    flag=sys.argv[1]
    if(flag=='-a' or flag=='-c'):
        if(len(sys.argv[2].split('/'))!=2):
            raise Exception('Wrong date params')
            sys.exit()
    elif(flag=='-e'):
        if(len(sys.argv[2].split('/'))!=1):
            raise Exception('Wrong date params')
            sys.exit()  
    else:
        raise Exception("Invalid Flag")
        sys.exit()




def validate_flag():
    flag = sys.argv[1]
    validate_date_parms()
    if(flag == '-a' or flag=='-c'):
        if len(sys.argv[2].split('/')) < 3:
            validate_month(sys.argv[2].split('/')[1])
            validate_year(sys.argv[2].split('/')[0])
        else:
            raise Exception("Invalid date arguments")
            sys.exit()
    elif(flag =='-e'):
        if len(sys.argv[2].split('/'))==1:
            validate_year(sys.argv[2])
        else:
            raise Exception("Invalid Date arguments")
            sys.exit()
        
def validate_path():
    path=get_path()
    if not os.path.isdir(path):
        raise Exception("Invalid Path")
        sys.exit()
    return path

    
