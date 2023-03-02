from os.path import exists
import glob
import sys
import math
from termcolor import colored
import validate
import dataread
import processdata



#Validate command line Arguments
validate.validate_parms()
path=validate.validate_path()
validate.validate_flag()

# reading data in dataframe pandas

df=dataread.read_data(path)


#Now we Will Process data to extract information
processdata.proccess(df)