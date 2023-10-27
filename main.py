import os
import time

def trans(path, savepath):
    pathDir = os.listdir(path)

    print('$ Time: ' + time.strftime("%a %b %d %H:%M %Y", time.localtime()) + '\n')
    print('---------- Start ----------' + '\n')

    for allDir in pathDir:
        saveDir = allDir
        saveDir = saveDir.replace('.flac', '_recode.flac')
        saveDir = saveDir.replace('.mp3', '_recode.flac')
        saveDir = saveDir.replace('.m4a', '_recode.flac')
        cmd = 'ffmpeg -y -i "' + path + allDir + '" "' + savepath + saveDir + '"'
        print('$ Time: ' + time.strftime("%a %b %d %H:%M %Y", time.localtime()) + '\n')
        print('# ' + cmd + ' Start!' + '\n')
        os.system(cmd)
        print('# ' + allDir + ' Done!' + '\n')
        print('---------- Next ----------' + '\n')

    print('$ Time: ' + time.strftime("%a %b %d %H:%M %Y", time.localtime()) + '\n')
    print('---------- End ----------' + '\n')
    print("Done!")

if __name__ == '__main__':
    path = input('Please input dir path: ')
    savepath = input('Please input save path: ')
    trans(path, savepath)