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

    def file2Dict(self, cls_arr, all = True):
        """file_name을 label별로 분류"""
        file_dict = {}
        for i in range(len(cls_arr)):
            idx = self.df.index[(self.df['class'] == cls_arr[i])]
            cls_df = self.df.loc[idx]
            labelList = list(set(cls_df['label']))
            cls_dict = {}
            for state in labelList:
                idx = cls_df.index[(cls_df['label'] == state)]
                cls_dict[state] = cls_df.loc[idx]['file_name'].tolist()
            file_dict[cls_arr[i]] = cls_dict
        if all == True:
            return file_dict
        else:
            one_file_dict = {}
            for key, value in file_dict.items():
                one_cls_dict = {}
                for v_key, v_value in value.items():
                    one_cls_dict[v_key] = [v_value[0]]
                one_file_dict[key] = one_cls_dict
            return one_file_dict

    def selectRow(self, idx, dimension = True):
        """
        dimension == True : 1차원 return
        dimension == False : 2차원 return
        """
        if dimension == True:
            return self.df.loc[idx]
        else:
            return self.df.loc[[idx]]
    
