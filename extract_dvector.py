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
#data = './test_tisv/speaker2.npy'
data = 'data_change'

if (__name__=='__main__'):
    print('Load model successfully.')
    embedder_net = SpeechEmbedder()
    embedder_net.load_state_dict(torch.load(model_path))

    inputs_wavs = glob.glob(os.path.join(data, '*', '*.wav'))

    for wav in inputs_wavs:
        _, mel_db, _ = mfccs_and_spec(wav, wav_process=True)
        inputs = torch.Tensor(mel_db)

        print(inputs.shape)
        inputs = inputs.unsqueeze(0)
        inputs = torch.FloatTensor(np.transpose(inputs, axes=(0,1,2)))
        outputs = embedder_net(inputs)
        mel_db = outputs.detach().numpy()
        output_path = wav[:-4]+'.npy'
        np.save(output_path, mel_db)