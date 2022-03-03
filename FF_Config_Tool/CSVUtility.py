import imp


import csv
import openpyxl

class DataFrame:
    pass

class WorkSheet:
    name : str
    path : str
    dataframe : DataFrame
    
def Open(path : str) ->(WorkSheet):
    return WorkSheet()

def Load(path : str) ->(WorkSheet):
    return WorkSheet()