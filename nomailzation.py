import numpy as np
import torchvision.transforms as transforms
from torchvision import datasets
import os

def get_mean_std(data_dir):

    transform=transforms.Compose([
        transforms.Resize((1024,1024)),
        transforms.ToTensor()
    ])

    dataset=datasets.ImageFolder(os.path.join(f'{data_dir}'),transform)

    meanRGB=[np.mean(x.numpy(),axis=(1,2)) for x,_ in dataset]
    stdRGB=[np.std(x.numpy(),axis=(1,2)) for x,_ in dataset]

    meanR=np.mean([m[0] for m in meanRGB])
    meanG=np.mean([m[1] for m in meanRGB])
    meanB=np.mean([m[2] for m in meanRGB])

    stdR=np.mean([s[0] for s in stdRGB])
    stdG=np.mean([s[1] for s in stdRGB])
    stdB=np.mean([s[2] for s in stdRGB])

    return [[meanR,meanG,meanB],[stdR,stdG,stdB]]
    

## 클래스 종류
cls_arr=['transistor', 'tile', 'pill', 'wood', 'hazelnut', 'capsule', 'carpet', 'metal_nut', 'leather', 'zipper', 'toothbrush', 'grid', 'bottle', 'screw', 'cable'] 
cls_nomalization_value={}
for cls in cls_arr:
    print(cls)

    ## 파일 위치 입력
    data_dir=f"C:/Users/PC/Desktop/test/dacon/data/label_train/{cls}/"
    cls_nomalization_value[cls]= get_mean_std(data_dir)

print(cls_nomalization_value)