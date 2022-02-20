from . import FileLocate
from . import FileOperate

from typing import Iterator
from typing import List
from P4 import P4

class CSV_CMD:
    cmd_name : str = "defalut"
    file_loc : FileLocate.Locate_Base
    file_operate : FileOperate.File_Operate_Base
    def doCMD(self , region ,  local_path , p4:P4) -> str:
        for file in self.file_loc.get_file_name(region , local_path):
            self.file_operate.run_operate(file , p4 )
    def __init__(self,file_loc : FileLocate.Locate_Base , file_operate : FileOperate) -> None:
        self.file_loc = file_loc
        self.file_operate = file_operate
        
class CSV_CMD_MANAGER:
    P4 : P4
    CMDList : List[CSV_CMD]
    local_path : str
    rglist : List[str]
    def initP4(self , port:str , user:str , password:str , client:str , no_connection : bool = False):
        self.P4 = P4()
        self.P4.port = port
        self.P4.user = user
        self.P4.password = password
        self.P4.client = client
        if(not no_connection):
            self.P4.connect()
        
    def run_all_CMD(self):
        for rg in self.rglist:
            for cmd in self.CMDList:
                cmd.doCMD(local_path = self.local_path , region = rg , p4=self.P4) 
    def add_CMD(self , CMD : CSV_CMD):
        self.CMDList.append(CMD)
    def __init__(self) -> None:
        self.CMDList = []