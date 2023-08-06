from typing import Union

class BaseProduct(object):
    def __init__(self, idx, name: str, model: str, start_process:Union[list,int]):
        self.id = idx
        self.name = name
        self.model = model  # 产品类型
        self.start_process = start_process
        self.end_process = -1
        self.next_processes = {}  # 所需要工序 {process_id: [下到工序]}
        self.pre_processes = {}  # 所需要工序 {process_id: [上到工序]}
