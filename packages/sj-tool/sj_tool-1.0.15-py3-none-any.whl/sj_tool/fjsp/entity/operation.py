from typing import List, Tuple, Dict, Union


class BaseOperation:
    def __init__(
        self,
        idx: Union[int, str],
        job_id: Union[int, str],
        demand: Union[int, float],
        process_id: int,
        machine_times: dict,
        pre_ops: list = [],
        next_ops: list = [],

    ):
        """

        :param idx: 工序id
        :param job_id: 工单id

        """
        self.id = idx
        self.job_id = job_id
        # process related
        self.process_id = process_id
        self.pre_ops = pre_ops
        self.next_ops = next_ops
        self.machine_times = machine_times # 设备处理单位数量所需时间 {"machine_id":float/int}
        self.available_machines = list(machine_times.keys())
        self.demand = demand
