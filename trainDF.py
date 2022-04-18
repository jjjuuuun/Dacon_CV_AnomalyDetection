import pandas as pd

class ColumnCollection():

    def __init__(self, df):
        """"""
        self.df = df
        self.cols = list(df.columns)
        self.length = len(df)

    # array를 dictionary로 변환
    def col2Dict(self, col):
        """Column의 unique한 값들을 dictionary로 return"""
        dictionary = {}
        array = self.colUnique(col)
        for i in range(len(array)):
            dictionary[array[i]] = i
        return dictionary

    def colUnique(self, col):
        """Column에서 unique한 값들을 list로 return"""
        array = self.col2Array(col)
        return list(set(array))

    def col2Array(self, col):
        """Column의 값들을 list로 return"""
        return list(self.df[col])
        
class matchingElement():
    def __init__(self, df):
        """"""
        self.df = df

    def rowElement(self, element, dimension = True):
        """
        dimension == True : 1차원 return
        dimension == False : 2차원 return
        """
        if dimension == True:
            return self.df.loc[element]
        else:
            return self.df.loc[[element]]