import trainDF
import pandas as pd
import cv2 as cv
import matplotlib.pyplot as plt
from image import SamplingImage

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
one_img_file = td.file2Dict(cls_arr, False)

si = SamplingImage('../data/train/')

# # 모든 image 파일 class별로 분류
# si.imgSave('../data/label_train/', cls_arr, img_file)

# # class별로 하나씩 분류
# si.imgSave('./label_train/', cls_arr, one_img_file)

# # 모든 image 파일 class별로 분류(Gray scale)
# si.imgSave('../data/label_train_gray/', cls_arr, img_file, colorful=False)

# # class별로 하나씩 분류(Gray scale)
# si.imgSave('./label_train_gray/', cls_arr, one_img_file, colorful=False)

# img = cv.imread('./label_train/bottle/bottle-broken_large/bottle-broken_large_10204.png')
# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# canny = cv.Canny(img_gray, 50, 150)
# images = [img_gray, canny]
# titles = ['Original', 'Ttitle']
# fig, ax = plt.subplots(1,2,figsize=(10,8))
# for i in range(2):
#     ax[i].imshow(images[i], cmap = 'gray')
#     ax[i].set_title(titles[i])
# plt.show()

print(len(train_df))