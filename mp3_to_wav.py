from os import path
from pydub import AudioSegment

# files                                                                         
# src = "test.wav"
# dst = "test_out.wav"

# # convert wav to mp3                                                            
# sound = AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")

import os
import glob

src = 'data'
dst = 'data_change'

speakers = ['付立', '刘子涵', '操镭', '李思琪', '李潇潇', '王润宇', '罗明双', '资礼波', '赵晴']
for speaker in speakers:
    mp3_files = glob.glob(os.path.join(src, speaker, '*.wav'))
    dst_final = os.path.join(dst, speaker)
    if not os.path.exists(dst_final): os.mkdir(dst_final)
    for file in mp3_files:
        mp3_name = file.split('\\')[-1].split('.')[0]
        print(mp3_name)
        sound = AudioSegment.from_mp3(file)
        dst_name = os.path.join(dst_final, mp3_name+'.wav')
        sound.export(dst_name, format='wav')
        
