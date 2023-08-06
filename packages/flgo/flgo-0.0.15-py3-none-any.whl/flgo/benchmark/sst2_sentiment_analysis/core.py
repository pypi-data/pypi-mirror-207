from ..toolkits.nlp.classification import DataPipeTaskPipe, DataPipeGenerator
from ..toolkits.cv.classification import GeneralCalculator
from torchtext.datasets import SST2
import os
import flgo.benchmark

path = os.path.join(flgo.benchmark.path, 'RAW_DATA','SST2')

def build_datapipes(root:str, split:str='train'):
    dp = SST2(root=root, split=split)
    return dp

class TaskGenerator(DataPipeGenerator):
    def __init__(self, rawdata_path:str=path):
        super(TaskGenerator, self).__init__(benchmark=os.path.split(os.path.dirname(__file__))[-1], rawdata_path=rawdata_path, build_datapipes=build_datapipes)
        self.build_datapipes = build_datapipes
        self.additional_option = {}
        self.train_additional_option = {'root':self.rawdata_path, 'split': 'train'}
        self.test_additional_option = {'root':self.rawdata_path, 'split':'dev'}

class TaskPipe(DataPipeTaskPipe):
    def __init__(self, task_path):
        super(TaskPipe, self).__init__(task_path, build_datapipes)

TaskCalculator = GeneralCalculator