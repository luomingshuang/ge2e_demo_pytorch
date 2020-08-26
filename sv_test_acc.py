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
data = 'test_wavs_one_speaker'

def get_centroid(embeddings, utterance_num):
    centroid = 0
    for utterance_id, utterance in enumerate(embeddings):
        if utterance_id <= (utterance_num-1):
            #print(utterance.shape)
            centroid = centroid + utterance 
        else: break
    centroid = centroid/utterance_num
    return centroid

embedder_net = SpeechEmbedder()
embedder_net.load_state_dict(torch.load(model_path))

speakers = ['lms','zq', 'wry', 'fuli', 'zlb', 'lzh', 'lxx', 'lsq', 'cl']
enroll_wav_path = 'media'
dict_spkid_embeddings = {}
'''
enroll_nums = 5
for speaker in speakers:
    #print(speaker)
    speaker_wavs = glob.glob(os.path.join(enroll_wav_path, speaker+'_*.wav'))[:enroll_nums]
    print(speaker, speaker_wavs)
    speaker_embeddings = []
    for wav in speaker_wavs:
        _, mel_db, _ = mfccs_and_spec(wav, wav_process=True)
        speaker_embeddings.append(mel_db)
    speaker_embeddings = torch.Tensor(speaker_embeddings)
    num_utterances = len(speaker_wavs)
    print(speaker_embeddings.size())
    speaker_embeddings = torch.FloatTensor(np.transpose(speaker_embeddings, axes=(0,1,2)))
    speaker_embeddings = embedder_net(speaker_embeddings)
    enroll_centroid_embeddings = get_centroid(speaker_embeddings, num_utterances)
    enroll_centroid_embeddings = torch.unsqueeze(enroll_centroid_embeddings, 0)
    dict_spkid_embeddings[speaker] = enroll_centroid_embeddings
'''
enroll_centroid_embeddings = 'enroll_9.npy'
enroll_centroid_embeddings = np.load(enroll_centroid_embeddings, allow_pickle=True).item()
print(enroll_centroid_embeddings.keys())

a = 0
total = 0
score = -10
name = 'Who?'

#speakers = ['付立', '刘子涵', '操镭', '李思琪', '李潇潇', '王润宇', '罗明双', '资礼波', '赵晴']
speakers = ['fuli', 'lzh', 'cl', 'lsq', 'lxx', 'wry', 'lms', 'zlb', 'zq']
data = 'media'
for speaker in speakers:
    test_wavs = glob.glob(os.path.join(data, '{}_*.wav'.format(speaker)))
    #print(test_wavs)
    x = 0
    y = 0
    for test_wav in test_wavs:
        scores= {}
        test_mel = []
        _, mel_db_test, _ = mfccs_and_spec(test_wav, wav_process=True)
        test_mel.append(mel_db_test)
        test_inputs = torch.Tensor(test_mel)
        #  print(test_inputs.size())
        test_inputs = torch.FloatTensor(np.transpose(test_inputs, axes=(0,1,2)))
        #print(test_inputs.size())
        test_output = embedder_net(test_inputs).cpu()
        for speaker_name in enroll_centroid_embeddings.keys():
            #print(enroll_centroid_embeddings[speaker_name].shape)
            speaker_centroid_enroll = get_centroid(enroll_centroid_embeddings[speaker_name], len(enroll_centroid_embeddings[speaker_name]))
            #print(speaker_centroid_enroll.shape)
            score_speaker = cosine_similarity(speaker_centroid_enroll.reshape(1,-1), test_output.detach().numpy())
            #print('speaker: ', speaker_name, 'score: ', score_speaker)
            scores[speaker_name] = score_speaker
            #print(score_speaker, score)
            if score_speaker > score :
                score = score_speaker
                name = speaker_name
                #print('speaker: ', name)
                #print('score: ', score)
        #print(scores)
        #name = max(scores, key=scores.get)
        print('test_wav: ', test_wav, 'predict speaker: ', name, 'predict score: ', scores)
        #print(speaker, name)
        if name == speaker:
            a += 1
            y += 1
    total += len(test_wavs)
    print('speaker {}, {}/{}'.format(speaker, y, len(test_wavs)))

print('test_speaker_recognition is: ', a/total)
        