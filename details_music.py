#IMPORT LIBROSA
try:
    import librosa
    import librosa.display
except ModuleNotFoundError: print('<ERROR>: Download pip module "librosa"')

class CheckMusic:
    def __init__(self, path_music = None):
        self.path_music = path_music
        self.tonal_index = 0
        
    def Tonality(self):
        print('__Search_tonality__')
        
        tonality_map = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        y, sr = librosa.load(self.path_music) #Load-File
        chroma = librosa.feature.chroma_stft(y = y, sr = sr)
        chroma_mean = chroma.mean(axis=1)
        tonal_class = chroma_mean.argmax()
        
        self.tonal_index = tonal_class
        
        return tonality_map[tonal_class]
    
    def Num_tonality(self):
        tonality_byte_num = [0.3, 0.3, 0.2, 0.2, 0.15, 0.1, 0.1, 0.2, 0.2, 0.2, 0.1, 0.3] #[0.3, 0.3, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.3, 0.3]
        
        return tonality_byte_num[self.tonal_index] 

    def BMP(self):
        print('__Search_BMP__')
    
        y, sr = librosa.load(self.path_music)
        tempo, _ = librosa.beat.beat_track(y = y, sr = sr)
        
        return tempo