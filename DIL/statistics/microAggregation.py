import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from util import DataSetting

class MicroAggregation(DataSetting):
    def mean(self, column:str, currentIndex:int):
        meanValue = int(self.datas[column].mean())
        self.datas.at[currentIndex, column] = meanValue

    def max(self, column:str, currentIndex:int):
        maxValue = self.datas[column].max()
        self.datas.at[currentIndex, column] = maxValue

    def min(self, column:str, currentIndex:int):
        minValue = self.datas[column].min()
        self.datas.at[currentIndex, column] = minValue

    def mode(self, column:str, currentIndex:int):
        modeValue = list(self.datas[column].mode())[-1]
        self.datas.at[currentIndex, column] = modeValue

    def median(self, column:str, currentIndex:int):
        medianValue = int(self.datas[column].median())
        self.datas.at[currentIndex, column] = medianValue