import os
import random
import time
import torch
import glob
import numpy as np
from torch.autograd import Variable
from sklearn.metrics.pairwise import cosine_similarity
from model import SpeechEmbedder
from utils import mfccs_and_spec

model_path = 'weights/epoch_3450_iteration_1487381_EER_0.05986112356185913.pth'

embedder_net = SpeechEmbedder()
embedder_net.load_state_dict(torch.load(model_path))

#speakers = ['付立', '刘子涵', '操镭', '李思琪', '李潇潇', '王润宇', '罗明双', '资礼波', '赵晴']
speakers = ['fuli', 'lzh', 'cl', 'lsq', 'lxx', 'wry', 'lms', 'zlb', 'zq']
enroll_wav_path = 'data_eng'
dict_spkid_embeddings = {}

enroll_nums = 5
for speaker in speakers:
    #print(speaker)
    speaker_wavs = glob.glob(os.path.join(enroll_wav_path, speaker, '*.wav'))
    length = len(speaker_wavs)
    print(speaker, speaker_wavs)
    speaker_embeddings = np.zeros((length, 256),dtype=float)
    for i in range(length):
    #for wav in speaker_wavs:
        embeddings = []
        _, mel_db, _ = mfccs_and_spec(speaker_wavs[i], wav_process=True)
        embeddings.append(mel_db)
        embeddings = torch.Tensor(embeddings)
        embeddings = torch.FloatTensor(np.transpose(embeddings, axes=(0,1,2)))
        embeddings = embedder_net(embeddings)
        embeddings = embeddings.cpu().detach().numpy()
        speaker_embeddings[i] = embeddings
    print(speaker_embeddings.shape)
    dict_spkid_embeddings[speaker] = speaker_embeddings

np.save('enroll_9_.npy', dict_spkid_embeddings)
        
