import cv2 as cv
import matplotlib.pyplot as plt
import trainDF
import math
import os

class SamplingImage():
    """"""
    def __init__(self, path):
        """"""
        self.path = path
    def imgShow(self, col_len, fig_size, arr_dict = None, arr_list = None, arr_tuple = None):
        """"""
        if arr_dict != None:
            dict_len = len(arr_dict)
            row_len = math.ceil(dict_len/col_len)
            
            label = list(arr_dict.keys())
            img_list = list(arr_dict.values())

            fig, ax = plt.subplots(row_len, col_len, figsize = fig_size)
            for i in range(row_len):
                for j in range(col_len):
                    img = cv.imread(self.path+img_list[col_len*i+j])
                    ax[i][j].imshow(img[:,:,::-1])
                    ax[i][j].set_title(label[col_len*i+j])
            plt.tight_layout()
            plt.show()

    def imgSave(self, cls_arr, arr_dict):
        """"""
        for idx in range(len(cls_arr)):
            img_dict = arr_dict[cls_arr[idx]]
            key = list(img_dict.keys())
            for state_key in key:
                value = img_dict[state_key]
                for i in range(len(value)):
                    img_path = '../data/label_train/' + cls_arr[idx] + '/'
                    title = state_key
                    img_name = value[i]
                    try:
                        if not os.path.exists(img_path + title):
                            os.makedirs(img_path + title)
                    except:
                        print(title)
                        pass
                    img = cv.imread(self.path + img_name)
                    cv.imwrite(img_path + title + '/' + title + '_' + img_name[:-4] + '.png', img)
