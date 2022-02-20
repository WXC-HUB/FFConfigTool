
from typing import Iterator

class Locate_Base:
    t = "t"
    def get_file_name(self , region , local_path) -> Iterator[str]:
        a = ["filename"]
        for item in a:
            yield a
        return
    
class Locate_by_Path(Locate_Base):
    filepath : str
    def __init__(self , path) -> None:
        super().__init__()
        self.filepath = path
    def get_file_name(self, region , local_path) -> Iterator[str]:
        file_list = []
        file_list.append(local_path + "\\" + region + "\\" + self.filepath)
        for i in file_list:
            yield i