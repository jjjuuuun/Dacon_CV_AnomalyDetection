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
        # os.chdir('../data/one_train/')
        for idx in range(len(cls_arr)):
            key = list(arr_dict[cls_arr[idx]].keys())
            value = list(arr_dict[cls_arr[idx]].values())
            try:
                if not os.path.exists('../data/one_train/' + cls_arr[idx]):
                    os.makedirs('../data/one_train/' + cls_arr[idx])
            except:
                print(cls_arr[idx])
                pass
            for i in range(len(key)):
                img_path = '../data/one_train/' + cls_arr[idx] + '/'
                title = key[i]
                img_name = value[i]
                try:
                    if not os.path.exists(img_path + title):
                        os.makedirs(img_path + title)
                except:
                    print(title)
                    pass
                # print(self.path + img_name)
                img = cv.imread(self.path + img_name)
                cv.imwrite(img_path + title + '/' + title + '_' + img_name[:-4] + '.png', img)
