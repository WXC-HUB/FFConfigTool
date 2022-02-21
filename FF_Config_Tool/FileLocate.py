
from typing import Iterator

class Locate_Base:
    t = "t"
    def get_file_name(self , region , local_path) -> Iterator[str]:
        a = ["filename"]
        for item in a:
            yield a
        return
    
class Locate_by_Name(Locate_Base):
    filename : str
    fileplaceholder : str
    def __init__(self , name , placeholder) -> None:
        super().__init__()
        self.filename = name
        self.fileplaceholder = placeholder
    def get_file_name(self, region , local_path) -> Iterator[str]:
        file_list = []
        file_list.append(local_path + "\\" + region + "\\" + self.filename.replace(self.fileplaceholder , region))
        for i in file_list:
            yield i