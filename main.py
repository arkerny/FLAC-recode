import os

def trans(path):
    pathDir = os.listdir(path)
    for allDir in pathDir:
        saveDir = allDir.replace('.flac', '.wav')
        saveDir = saveDir.replace('.mp3', '.wav')
        cmd = "ffmpeg -i " + path + allDir + ' ' + path + saveDir
        print(cmd)
        # os.system(cmd)

if __name__ == '__main__':
    path = input('Please input dir path: ')
    trans(path)