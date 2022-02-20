from . import Line_Utility
from typing import Iterator
from typing import List
from P4 import P4

class File_Operate_Base:
    def run_operate(self , target_file:str , p4:P4):
        pass
    
class Operate_By_Line(File_Operate_Base):
    line_loc : Line_Utility.CSV_LINE_LOCATION_BASE
    line_operate : Line_Utility.CSV_LINE_OPERATE_BASE
    
class Add_File_With_Line(File_Operate_Base):
    New_Lines : List[List]
    def run_operate(self , target_file:str , p4:P4):
        print("add")
        print(self.New_Lines)
    def __init__(self , New_Lines : List[List]) -> None:
        super().__init__()
        self.New_Lines = New_Lines