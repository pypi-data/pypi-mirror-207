from typing import Dict


class BaseProcess(object):
    def __init__(self, process_id: int, name: str, standing_time: float):
        self.process_id = process_id  # 工序id
        self.name = name  # 工序名称
        self.standing_time = standing_time  # 工序静置时间
