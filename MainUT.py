import csv
from telnetlib import PRAGMA_HEARTBEAT
from typing import Iterator
from typing import List
from P4 import P4
import openpyxl
from os.path import *

import sys


p = dirname(abspath(__file__))
if(not p in sys.path):
    sys.path.append(p)
import FF_Config_Tool
from FF_Config_Tool.CSVUtility import WorkSheet

class CSV_LINE_LOCATION_BASE:
    def get_line_index(self) -> Iterator[int]:
        for item in range(0,10):
            yield item
        return
        
class CSV_LINE_OPERATE_BASE:
    def get_new_line(self,old_line:List[int]) -> List[int]:
        return [old_line]
    
class CSV_FILE_OPERATE:
    pass

if __name__ == "__main__":
    
    test_cmd_manager = FF_Config_Tool.CMD_Utility.CSV_CMD_MANAGER()
    
    test_cmd_manager.initP4(
        port = '*****',
        user = '*****',
        password = '*****',
        client = '******',
        no_connection=True
    )
    
    test_cmd_manager.local_path = "D:\p4vspace\DTS\Dev\Config"
    test_cmd_manager.rglist =['BR'  , 'EUROPE' , 'ID' , 'IND' , 'ME' , 'NA' , 'PK' , 'RU' , 'SAC' , 'TH' , 'TW' , 'US' , 'VN' , 'ZA' , 'BD', 'SG']
    
    #test_cmd_manager.add_CMD(
    #    FF_Config_Tool.CMD_Utility.CSV_CMD(
    #        FF_Config_Tool.FileLocate.Locate_by_Name("a_xx.csv" , "xx"),
    #        FF_Config_Tool.FileOperate.Add_File_With_Line([
    #            ["t1" , "t2"],
    #            [123 , 321]
    #        ])
    #    )
    #)
    #
    #test_cmd_manager.run_all_CMD()
    
    sheet : WorkSheet = FF_Config_Tool.CSVUtility.Open("TestChart.csv")
    
    