import pandas as pd

class TrainDF():

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

    def file2Dict(self, cls_arr):
        """file_name을 label별로 분류"""
        file_dict = {}
        for i in range(len(cls_arr)):
            idx = self.df.index[(self.df['class'] == cls_arr[i])]
            cls_df = self.df.loc[idx]
            labelList = list(set(cls_df['label']))
            for state in labelList:
                idx = cls_df.index[(cls_df['label'] == state)]
                file_dict[state] = cls_df.loc[idx]['file_name'].tolist()
        return file_dict

    def rowElement(self, element, dimension = True):
        """
        dimension == True : 1차원 return
        dimension == False : 2차원 return
        """
        if dimension == True:
            return self.df.loc[element]
        else:
            return self.df.loc[[element]]
    
