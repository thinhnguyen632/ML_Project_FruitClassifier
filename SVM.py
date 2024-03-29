# -*- coding: utf-8 -*-
"""SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nvTvafNTw_Z_pugyPteMA57JqTwdAekH
"""

import pandas as pd
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
#đường dẫn vào tệp dữ liệu 
os.listdir('/content/drive/MyDrive/Training/Training')[0:10]

#Chọn 1 hình trong tập dữ liệu 
path = '/content/drive/MyDrive/Training/Training/Bap/0_100.jpg'
#xử lý ảnh 
im = cv2.imread(path)
#hiển thị
plt.imshow(im)
plt.savefig('a.png')

#chuyển sang dạng mảng 
grayim = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
grayim

#Giảm chiều dữ liệu đưa về 0 và 1
grayim = grayim.astype('float')/255

#Kéo dãn 
grayim = grayim.flatten()
#Đưa về dạng chuỗi 
grayim = pd.Series(grayim)
grayim

path = '/content/drive/MyDrive/Training/Training/'
# 
cols = np.arange(grayim.shape[0])
# 
df = pd.DataFrame(columns = cols)
labelcol = []

fruitlist = os.listdir(path)
x = 0

for folder in fruitlist[0:9] : 
  #Gán đường dẫn cho folder
    fruitpath = os.path.join(path,folder)
  #Gán imagelist bằng đường dẫn
    imagelist = os.listdir(fruitpath)
    
    for imag in imagelist:
 #Gán đường dẫn cho ảnh
        imagepath = os.path.join(fruitpath,imag)
    #Đọc ảnh
        image = cv2.imread(imagepath)
    #Tách hệ màu
        b,g,r = cv2.split(image)
    #Gộp màu theo thứ tự RGB
        image = cv2.merge([r,g,b])
    #Chuyển sang màu xám
        imagegray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    #Giảm chiều dữ liệu đưa về dạng 0;1 
        imagegray = imagegray.astype('float')/255
    #Kéo dãn 
        imagegray = imagegray.flatten()
    
        df.loc[x] = imagegray
    
        x = df.shape[0] + 1
        #Bổ sung dữ liệu vào chỗ trống cuối danh sách dưới dạng 0;1
        labelcol.append(folder)

#Gắn nhãn dữ liệu
df['label'] = labelcol
#Chuẩn hóa dữ liệu
df['label'].value_counts(normalize = True)

df = shuffle(df).reset_index(drop = True)
df

# transpose data set and shuffle
#không xài random vì các biến ngẫu nhiên có thể sẽ trùng nhau
#Xáo trộn dữ liệu
df_t = shuffle(df.transpose())
# transpose back to normal
# Đưa về kiểu dữ liệu chuẩn hóa *normal
df = df_t.transpose()

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report

# Create X and Y variables
X = df.drop('label',axis = 1)
y = df['label']

# create our test and training set
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state = 0,stratify = y)

from sklearn.svm import SVC
#Sử dụng SVM để tiến hành training model
svm_model = SVC().fit(X_train,y_train)
trainscore = svm_model.score(X_train,y_train)
testscore = svm_model.score(X_test,y_test)
#Hàm dự đoán
y_pred = svm_model.predict(X_test)

print("CLASSIFICATION REPORT FOR SVM")
# print("Confusion MAtrix:")
# print(confusion_matrix(y_test,y_pred))
# print()
# print(classification_report(y_test,y_pred))
print("train score:",trainscore)
print("test_score",testscore)

X_test[0]

