import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

path = 'data_change'

import numpy as np
import glob
import options as opt
import os

labels = [] 

ivectors = glob.glob(os.path.join(path, '*', '*.npy'))

length = len(ivectors)

dim = 256

ivector_np = np.zeros((length, dim))

print(ivector_np.shape)

targets = []
#labels = ['付立', '刘子涵', '操镭', '李思琪', '李潇潇', '王润宇', '罗明双', '资礼波', '赵晴']
labels = ['fuli', 'lzh', 'cl', 'lsq', 'lxx', 'wry', 'lms', 'zlb', 'zq']
for i in range(length):

    ivector_np[i] = np.load(ivectors[i])
    #print(ivectors[i])
    print(ivectors[i])
    speaker_name = ivectors[i].split('\\')[-2]
    
    #print(labels, speaker_name)
    if speaker_name not in labels:
        print('bad')
    #print(speaker_name)
    speaker_name = labels.index(speaker_name)
    targets.append(speaker_name)

'''t-SNE'''
tsne = manifold.TSNE(n_components=2, init='pca', random_state=501)
X_tsne = tsne.fit_transform(ivector_np.data)

print("Org data dimension is {}, Embedded data dimension is {}".format(ivector_np.shape[-1], X_tsne.shape[-1]))

'''嵌入空间可视化'''
x_min, x_max = X_tsne.min(0), X_tsne.max(0)
X_norm = (X_tsne - x_min) / (x_max - x_min)  # 归一化
plt.title('{}'.format('-'.join(labels)))
#plt.figure(num='{}'.format('-'.join(labels)), figsize=(6, 6))
for i in range(X_norm.shape[0]):
    plt.text(X_norm[i, 0], X_norm[i, 1], str(targets[i]), color=plt.cm.Set1(targets[i]), 
             fontdict={'weight': 'bold', 'size': 9})

plt.xticks([])
plt.yticks([])
plt.show()