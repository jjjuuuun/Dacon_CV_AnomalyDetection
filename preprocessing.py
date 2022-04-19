import trainDF
import pandas as pd
import cv2 as cv
import matplotlib.pyplot as plt
from image import SamplingImage
import os
train_df = pd.read_csv('../data/train_df.csv')
train_df.drop(['index'], axis = 1, inplace = True)

td = trainDF.TrainDF(train_df)
file_col, cls_col, state_col, label_col = td.cols

cls_arr = td.colUnique(cls_col)
state_arr = td.colUnique(state_col)
label_arr = td.colUnique(label_col)

cls_dict = td.col2Dict(cls_col)
state_dict = td.col2Dict(state_col)
label_dict = td.col2Dict(label_col)

img_file = td.file2Dict(cls_arr, True)

si = SamplingImage('../data/train/')
si.imgSave(cls_arr, img_file)