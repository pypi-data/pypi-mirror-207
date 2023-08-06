def namaste(name):
    print('Pedha Manishiki Pranamaalu...')
    print(name+' garu....koodu maesinaara?')
import numpy as np
import librosa
# from sklearn.metrics.pairwise import cosine_similarity

def compute_cumshot(audio_file):
    # speaker_name = (audio_file.split('/')[-1]).split('.')[0]
    # Apply PCA to reduce the dimensionality of the MFCC features
#     mfcc_features=mfcc_features.reshape(-1,1)
#     st.write(mfcc_features.shape)
    audio, sr = librosa.load(audio_file, sr=48000)
    # print(speaker_name," : ",sr)
    frame_length = int(sr * 0.025)  # 25 ms
    hop_length = int(sr * 0.010)  # 10 ms
    n_fft = 512
    n_mels = 40
    n_components = 10

    

    S = librosa.feature.melspectrogram(y=audio, sr=sr, n_fft=n_fft,hop_length=hop_length, n_mels=n_mels)

    # Compute the d-vector by averaging the normalized PCA-transformed MFCC features
    S = np.log(S + 1e-9)

# compute delta and delta-delta
    delta = librosa.feature.delta(S, width=3)
    delta_delta = librosa.feature.delta(S, order=2, width=3)

# concatenate features
    # mean = np.mean(features, axis=1)

    features = np.concatenate((S, delta, delta_delta), axis=0)
    cov = np.cov(features)
    
    U, s, Vh = np.linalg.svd(cov)
    A = np.dot(np.dot(U, np.diag(np.sqrt(s))), U.T)
    x = np.mean(features, axis=1)
    d=np.dot(A, U.T)
    d = np.dot(np.dot(A, U.T), (x))
    print(d)