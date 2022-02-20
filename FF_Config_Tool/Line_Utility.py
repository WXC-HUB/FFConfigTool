from typing import Iterator
from typing import List

class CSV_LINE_LOCATION_BASE:
    def get_line_index(self) -> Iterator[int]:
        for item in range(0,10):
            yield item
        return
        
class CSV_LINE_OPERATE_BASE:
    def get_new_line(self,old_line:List[int]) -> List[int]:
        return [old_line]