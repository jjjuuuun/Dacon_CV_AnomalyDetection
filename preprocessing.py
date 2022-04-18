import trainDF
import pandas as pd
import cv2 as cv
import matplotlib.pyplot as plt

train_df = pd.read_csv('./data/train_df.csv')
train_df.drop(['index'], axis = 1, inplace = True)

mc = trainDF.ColumnCollection(train_df)
file_col, cls_col, state_col, label_col = mc.cols

cls_arr = mc.colUnique(file_col)
cls_arr = mc.colUnique(cls_col)
state_arr = mc.colUnique(state_col)
label_arr = mc.colUnique(label_col)

# cls_dict = mc.col2Dict(file_col)
cls_dict = mc.col2Dict(cls_col)
state_dict = mc.col2Dict(state_col)
label_dict = mc.col2Dict(label_col)

img = cv.imread('./data/train/10000.png')
# cv.imshow('img', img)
# cv.waitKey()
# cv.destroyAllWindows()
plt.imshow(img[:,:,::-1])
plt.show()