from . import Line_Utility
from . import CSVUtility
from typing import Iterator
from typing import List
from P4 import P4
import time

class File_Operate_Base:
    def run_operate(self , target_file:CSVUtility.WorkSheet , p4:P4):
        pass
    
class Operate_By_Line(File_Operate_Base):
    line_loc : Line_Utility.CSV_LINE_LOCATION_BASE
    line_operate : Line_Utility.CSV_LINE_OPERATE_BASE
    def __init__(self , line_loc : Line_Utility.CSV_LINE_LOCATION_BASE , line_operate : Line_Utility.CSV_LINE_OPERATE_BASE) -> None:
        super().__init__()
        self.line_loc = line_loc
        self.line_operate = line_operate
    def run_operate(self, target_file: CSVUtility.WorkSheet, p4: P4):
        file = CSVUtility.Open(target_file)
        for index in self.line_loc.get_line_index(sheet=file):
            self.line_operate.run_operate(index=index , sheet=file)
        p4.run("edit" , target_file)
        file.save()
        time.sleep(0.5)
        
class Add_File_With_Line(File_Operate_Base):
    New_Lines : List[List]
    def run_operate(self , target_file:str , p4:P4):
        print("add " + target_file)
        print(self.New_Lines)
    def __init__(self , New_Lines : List[List]) -> None:
        super().__init__()
        self.New_Lines = New_Lines
        