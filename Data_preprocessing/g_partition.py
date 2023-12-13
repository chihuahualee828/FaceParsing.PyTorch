import os
import shutil
import pandas as pd
from shutil import copyfile
from utils import make_folder

#### source data path
s_label = 'CelebAMaskHQ-mask'
s_img = 'CelebA-HQ-img'
#### destination training data path
d_train_label = 'train_label'
d_train_img = 'train_img'
#### destination testing data path
d_test_label = 'test_label'
d_test_img = 'test_img'
#### val data path
d_val_label = 'val_label'
d_val_img = 'val_img'

#### make folder
make_folder(d_train_label)
make_folder(d_train_img)
make_folder(d_test_label)
make_folder(d_test_img)
# make_folder(d_val_label)
# make_folder(d_val_img)

#### calculate data counts in destination folder
train_count = 0
test_count = 0
val_count = 0

image_list = pd.read_csv('CelebA-HQ-to-CelebA-mapping.txt', delim_whitespace=True, header=0)
# f_train = open('train_list.txt', 'w')
# f_val = open('val_list.txt', 'w')
# f_test = open('test_list.txt', 'w')

train_list = pd.read_csv('train.txt', delim_whitespace=True, header=None)
test_list = pd.read_csv('test.txt', delim_whitespace=True, header=None)

for x in train_list.iloc[:, 0]:
    print ('processing: ', x)
    copyfile(os.path.join(s_label, str(x)+'.png'), os.path.join(d_train_label, str(x)+'.png'))
    copyfile(os.path.join(s_img, str(x)+'.jpg'), os.path.join(d_train_img, str(x)+'.jpg'))        
    train_count += 1

for x in test_list.iloc[:, 0]:
    print ('processing: ', x)
    copyfile(os.path.join(s_label, str(x)+'.png'), os.path.join(d_test_label, str(x)+'.png'))
    copyfile(os.path.join(s_img, str(x)+'.jpg'), os.path.join(d_test_img, str(x)+'.jpg'))        
    test_count += 1


print ('Total Num: ', train_count + test_count)

