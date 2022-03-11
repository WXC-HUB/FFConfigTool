from typing import Iterator
from typing import List
from . import CSVUtility

class CSV_LINE_LOCATION_BASE:
    def get_line_index(self ,  sheet : CSVUtility.WorkSheet) -> Iterator[int]:
        pass
    def get_line_value(self ,  sheet : CSVUtility.WorkSheet) -> List[str]:
        pass
        
class CSV_LINE_OPERATE_BASE:
    def __init__(self) -> None:
        pass
    def run_operate(self ,  sheet : CSVUtility.WorkSheet , index : int):
        pass

class Loc_Line_With_Key_Value(CSV_LINE_LOCATION_BASE):
    keyname : str
    keyvalue : str
    def __init__(self  ,  keyname : str , keyvalue : str) -> None:
        self.keyname = keyname
        self.keyvalue = keyvalue
        super().__init__()
    def get_line_index(self, sheet: CSVUtility.WorkSheet) -> Iterator[int]:
        print(sheet.path)
        i = sheet.dataArray[0].index(self.keyname)
        for index , row in sheet.get_indexed_rows():
            if(row[i] == self.keyvalue):
                yield index
        
class Add_Line_And_Change_Key_Value_By_Index(CSV_LINE_OPERATE_BASE):
    keyname : str
    keyvalue : str
    def __init__(self  ,  keyname : str , keyvalue : str) -> None:
        self.keyname = keyname
        self.keyvalue = keyvalue
        super().__init__()
    def run_operate(self, sheet: CSVUtility.WorkSheet, index: int):
        i = sheet.dataArray[0].index(self.keyname)
        row = sheet.dataArray[index].copy()
        row[i] = self.keyvalue
        sheet.append(row)