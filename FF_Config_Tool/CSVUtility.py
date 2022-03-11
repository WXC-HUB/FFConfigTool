import enum
import imp
from operator import truediv
from pickle import LIST
from typing import Iterator
from typing import List
from typing import Tuple

import csv
from re import L
import re

class DataFrame:
    titles : List[str]
    rows : List[dict]
    def __init__(self) -> None:
        self.titles = []
        self.rows = []


def number_to_column_letter(number , columnA = 0) -> str:
    ab = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = number - columnA
    x = n % 26
    if n >= 26:
        n = int(n / 26)
        return number_to_column_letter(n, 1) + ab[x + 1]
    else:
        return ab[x + 1]

def str_to_cell_xy(cellstr : str) -> Tuple[ int , int ]:
    return -1,-1
    
class WorkSheet:
    path : str
    dataArray : List[List[str]]
    dataFrame : DataFrame
    sheet_value : dict
    encoding : str
    def __init__(self):
        self.sheet_value = {}
        self.dataArray = []
        self.dataFrame = DataFrame()
    def __getitem__(self , key):
        return self.sheet_value[key]

    def __setitem__(self , key , value):
        self.sheet_value[key] = value
    
    def get_rows(self) -> Iterator[List[str]]:
        for i in self.dataArray:
            yield i
            
    def get_indexed_rows(self) -> Tuple[int ,  Iterator[List[str]] ]:
        for index , i in enumerate(self.dataArray):
            yield index , i
    
    def init_SheetValue(self):
        self.sheet_value = {}
        for index_row , line in enumerate(self.dataArray):
            for index_column , cell in enumerate(line):
                cellname : str = number_to_column_letter(index_column) + str(index_row+1)
                self[ cellname ] = cell
        #print(self.sheet_value)
        
    def init_dataFarme(self , has_desc = True):
        self.dataFrame = DataFrame()
        self.dataFrame.titles = self.dataArray[0]
        startrow = 2 if has_desc else 1
        for index ,  row in enumerate(self.dataArray[startrow:]):
            new_item = {}
            new_item["index"] = index
            for cell_index , cell in enumerate(row):
                new_item[ self.dataFrame.titles[cell_index] ] = cell
            self.dataFrame.rows.append(new_item)
        #print(self.dataFrame.titles , self.dataFrame.rows)

    def save(self , path : str = ""):
        if(path == ""):  
            path = self.path
        if(path == ""):
            return
        with open(path , "w+" , encoding=self.encoding , newline="") as csvfile:
            writer = csv.writer(csvfile)
            for row in self.dataArray:
                writer.writerow(row)
        pass
    
    def append(self , newrow:List[str]):
        self.dataArray.append(newrow)

def Open(path : str , encoding : str = "utf-8") ->(WorkSheet):
    newWorkSheet = WorkSheet()
    
    newWorkSheet.path = path
    newWorkSheet.encoding = encoding
    reader =  csv.reader(open(path , encoding = encoding))
    for index_row , line in enumerate(reader):
        newWorkSheet.dataArray.append(line)
        newWorkSheet.init_SheetValue()
        newWorkSheet.init_dataFarme()
    return newWorkSheet
